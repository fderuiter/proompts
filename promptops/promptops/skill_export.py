import os
import json
from pathlib import Path
from typing import Dict, Any, Set, List
import jinja2.meta
from jinja2.sandbox import SandboxedEnvironment
import jinja2.exceptions
import yaml
from pydantic import ValidationError

from promptops.validation import PromptSchema

def extract_undeclared_variables(text: str) -> Set[str]:
    env = SandboxedEnvironment()
    try:
        ast = env.parse(text)
        return jinja2.meta.find_undeclared_variables(ast)
    except jinja2.exceptions.TemplateSyntaxError as e:
        raise e
    except Exception:
        return set()

def generate_skill_content(data: Dict[str, Any], raw_data: Dict[str, Any], raw_content: str, variables: Set[str] = None) -> str:
    description = data.get("description", "")

    if variables is None:
        variables = extract_undeclared_variables(raw_content)

    messages_text = []

    messages = raw_data.get("messages", [])
    if not messages:
        messages = data.get("messages", [])

    for msg in messages:
        content = msg.get("content", "")
        role = msg.get("role", "unknown")
        messages_text.append(f"[{role.upper()}]\n{content.strip()}")

    instructions = "\n\n".join(messages_text)

    defined_vars = {v.get("name"): v for v in data.get("variables", [])}

    input_lines = []
    for var in sorted(variables):
        var_info = defined_vars.get(var, {})
        desc = var_info.get("description", "No description provided.")
        req = "required" if var_info.get("required", True) else "optional"
        input_lines.append(f"- {var} ({req}): {desc}")

    input_def = "\n".join(input_lines)

    skill_md = f"""<context>
{description}
</context>

<instructions>
{instructions}
</instructions>

<input>
{input_def}
</input>
"""
    return skill_md

def read_prompt_file(path: Path) -> str:
    """Reads text from a prompt file, returns raw_content or raises."""
    return path.read_text(encoding='utf-8')

def parse_prompt_yaml(raw_content: str) -> tuple:
    """Returns (raw_data, errors_list) where errors come from YAML parse exceptions."""
    errors = []
    raw_data = None
    try:
        raw_data = yaml.safe_load(raw_content)
    except yaml.YAMLError as e:
        problem_mark = getattr(e, 'problem_mark', None)
        line = problem_mark.line + 1 if problem_mark is not None else "N/A"
        errors.append({
            "type": "YAML Parsing Error",
            "message": str(e),
            "line": line
        })
    except Exception as e:
        errors.append({
            "type": "Unknown Error",
            "message": str(e),
            "line": "N/A"
        })
    return (raw_data, errors)

def detect_skill(raw_content: str, raw_data: Any) -> bool:
    """Implements 'skill' detection logic, returns bool."""
    is_skill = False
    if raw_data and isinstance(raw_data, dict):
        metadata = raw_data.get("metadata", {})
        tags = metadata.get("tags", [])
        if "skill" in tags:
            is_skill = True
    else:
        if "skill" in raw_content:
            is_skill = True
    return is_skill

def validate_prompt_schema(raw_data: Any) -> List[Dict[str, Any]]:
    """Runs PromptSchema validation, returns validation errors list."""
    errors = []
    if raw_data is not None and isinstance(raw_data, dict):
        try:
            PromptSchema(**raw_data)
        except ValidationError as e:
            for err in e.errors():
                loc = ".".join(map(str, err["loc"]))
                errors.append({
                    "type": "Validation Error",
                    "message": f"{loc}: {err['msg']}",
                    "line": "N/A"
                })
    return errors

def render_skill(raw_content: str, raw_data: Any) -> tuple:
    """Sets up SandboxedEnvironment, checks Jinja parsing, calls generate_skill_content, returns (skill_content, errors_list)."""
    errors = []
    skill_content = None
    try:
        env = SandboxedEnvironment()
        ast = env.parse(raw_content)
        variables = jinja2.meta.find_undeclared_variables(ast)

        if raw_data and isinstance(raw_data, dict):
            skill_content = generate_skill_content(raw_data, raw_data, raw_content, variables)
    except jinja2.exceptions.TemplateSyntaxError as e:
        errors.append({
            "type": "Jinja2 Syntax Error",
            "message": e.message,
            "line": e.lineno
        })
    except Exception as e:
        errors.append({
            "type": "Skill Generation Error",
            "message": str(e),
            "line": "N/A"
        })
    return (skill_content, errors)

def write_skill_file(prompts_path: Path, docs_path: Path, path: Path, skill_content: str):
    """Handles clean_name, directories, SKILL.md equality check and write."""
    out_skills_dir = docs_path / "skills"
    clean_name = path.name.replace('.prompt.yaml', '').replace('.yaml', '')
    rel_to_prompts = path.relative_to(prompts_path)
    skill_dir = out_skills_dir / rel_to_prompts.parent / clean_name
    skill_dir.mkdir(parents=True, exist_ok=True)

    skill_file = skill_dir / "SKILL.md"

    if skill_file.exists():
        existing_content = skill_file.read_text(encoding='utf-8')
        if existing_content == skill_content:
            return

    skill_file.write_text(skill_content, encoding='utf-8')

def generate_health_dashboard(docs_path: Path, health_report: List[Dict[str, Any]]):
    dashboard_path = docs_path / "skill_health.md"

    lines = [
        "---",
        "title: Skill Health",
        "---",
        "",
        "# Skill Health Dashboard",
        "",
        "This dashboard highlights parsing and validation errors across all exported skills.",
        ""
    ]

    if not health_report:
        lines.append("🎉 **All skills are healthy!**")
    else:
        for report in health_report:
            lines.append(f"## `{report['file']}`")
            for err in report["errors"]:
                lines.append(f"- **{err['type']}**: {err['message']} (Line: {err.get('line', 'N/A')})")
            lines.append("")

    dashboard_path.write_text("\n".join(lines), encoding='utf-8')

def process_skills(prompts_path: Path, docs_path: Path):
    from promptops.utils import iter_prompt_files

    health_report = []

    for path in iter_prompt_files(str(prompts_path)):
        errors = []

        try:
            raw_content = read_prompt_file(path)
        except Exception as e:
            health_report.append({
                "file": str(path.relative_to(prompts_path)),
                "errors": [{
                    "type": "File Read Error",
                    "message": str(e),
                    "line": "N/A"
                }]
            })
            continue

        raw_data, parse_errors = parse_prompt_yaml(raw_content)
        errors.extend(parse_errors)

        if not detect_skill(raw_content, raw_data):
            continue

        validation_errors = validate_prompt_schema(raw_data)
        errors.extend(validation_errors)

        skill_content, render_errors = render_skill(raw_content, raw_data)
        errors.extend(render_errors)

        if errors:
            health_report.append({
                "file": str(path.relative_to(prompts_path)),
                "errors": errors
            })

        if skill_content:
            write_skill_file(prompts_path, docs_path, path, skill_content)

    generate_health_dashboard(docs_path, health_report)
