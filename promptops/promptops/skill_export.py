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

def generate_skill_content(data: Dict[str, Any], raw_data: Dict[str, Any], raw_content: str, variables: Set[str] = None) -> str:
    description = data.get("description", "")

    if variables is None:
        variables = extract_undeclared_variables(raw_content)

    messages_text = []

    messages = raw_data.get("messages", [])
    if not messages:
        messages = data.get("messages", [])

    for msg in messages:
        role = msg.get("role", "unknown")
        
        content = msg.get("content")
        content_str = ""
        if isinstance(content, list):
            content_str = yaml.dump(content, sort_keys=False).strip()
        elif content is not None:
            content_str = str(content).strip()
            
        if content_str:
            messages_text.append(f"[{role.upper()}]\n{content_str}")
            
        tool_calls = msg.get("tool_calls")
        if tool_calls:
            tc_yaml = yaml.dump(tool_calls, sort_keys=False, default_flow_style=False).strip()
            messages_text.append(f"[TOOL_CALL]\n```yaml\n{tc_yaml}\n```")

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
    from promptops.tags import extract_tags, extract_tags_from_text
    
    if raw_data and isinstance(raw_data, dict):
        tags = extract_tags(raw_data)
        if "skill" in tags:
            return True
            
    # Fallback to raw text extraction
    text_tags = extract_tags_from_text(raw_content)
    if "skill" in text_tags:
        return True
        
    return False

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
    """
    Render a skill from raw prompt content and parsed YAML data.
    
    Parameters:
        raw_content (str): The raw prompt file content (Jinja2 template text) to analyze for undeclared variables.
        raw_data (Any): Parsed YAML content for the prompt (expected to be a dict when a skill should be generated).
    
    Returns:
        tuple: A pair (skill_content, errors) where:
            - skill_content (str | None): Generated skill markdown when rendering succeeds and `raw_data` is a dict; otherwise `None`.
            - errors (List[Dict[str, Any]]): A list of error objects. Each error dict contains:
                - `type` (str): Error category (e.g., "Jinja2 Syntax Error", "Skill Generation Error").
                - `message` (str): Human-readable error message.
                - `line` (int | str): Line number associated with the error when available, otherwise "N/A".
    """
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

def write_skill_file(prompts_path: Path, docs_path: Path, path: Path, skill_content: str, reconciler: 'DirectoryReconciler' = None):
    """
    Write or delegate writing of a skill's SKILL.md file into the docs skills directory for a given prompt file.
    
    Constructs the destination directory under `docs_path/skills` using `path` relative to `prompts_path` and a cleaned file name (removing `.prompt.yaml` or `.yaml`). If a `reconciler` is provided, delegates the write to `reconciler.write_file`; otherwise it ensures the target directory exists, skips writing when the existing SKILL.md content is identical to `skill_content`, and writes `skill_content` to SKILL.md when different or missing.
    
    Parameters:
        prompts_path (Path): Root directory containing prompt source files.
        docs_path (Path): Root directory for generated documentation.
        path (Path): Path to the source prompt file that produced `skill_content`.
        skill_content (str): The content to write into the SKILL.md file.
        reconciler (DirectoryReconciler, optional): If provided, used to queue or manage file writes via its `write_file` method.
    """
    out_skills_dir = docs_path / "skills"
    clean_name = path.name.replace('.prompt.yaml', '').replace('.yaml', '')
    rel_to_prompts = path.relative_to(prompts_path)
    skill_dir = out_skills_dir / rel_to_prompts.parent / clean_name
    
    skill_file = skill_dir / "SKILL.md"

    if reconciler:
        reconciler.write_file(skill_file, skill_content)
    else:
        skill_dir.mkdir(parents=True, exist_ok=True)
        if skill_file.exists():
            existing_content = skill_file.read_text(encoding='utf-8')
            if existing_content == skill_content:
                return

        skill_file.write_text(skill_content, encoding='utf-8')

def generate_health_dashboard(docs_path: Path, health_report: List[Dict[str, Any]]):
    """
    Create or update a markdown dashboard summarizing parsing and validation errors for exported skills.
    
    Parameters:
        docs_path (Path): Directory where the dashboard file `skill_health.md` will be written.
        health_report (List[Dict[str, Any]]): A list of report objects, each with keys:
            - `file` (str): Path or name of the prompt file.
            - `errors` (List[Dict[str, Any]]): List of error objects, each containing:
                - `type` (str): Error category (e.g., "YAML Parsing Error", "Validation Error").
                - `message` (str): Human-readable error message.
                - `line` (Union[int, str], optional): Line number associated with the error or "N/A".
    """
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
    """
    Process prompt files under prompts_path and generate skill documentation and a health dashboard.
    
    Iterates over prompt files discovered under prompts_path, parses and validates each prompt, renders skill content when the prompt is identified as a skill, and writes per-skill SKILL.md files into docs_path/skills using a DirectoryReconciler. Accumulates parsing, validation, and rendering errors into a health report and writes a consolidated skill_health.md to docs_path. Files that cannot be read are recorded as file-read errors; prompts that are not skills are skipped.
    
    Parameters:
        prompts_path (Path): Root directory containing prompt files to process.
        docs_path (Path): Output documentation directory where skills and the health dashboard are written.
    """
    from promptops.utils import iter_prompt_files
    from promptops.sync import DirectoryReconciler

    health_report = []
    
    out_skills_dir = docs_path / "skills"
    reconciler = DirectoryReconciler(out_skills_dir, manage_pattern="SKILL.md")

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

        is_skill = detect_skill(raw_content, raw_data)

        # If it's not a skill AND it has no YAML errors, we can safely skip it.
        # But if it has YAML errors, we should report them because it might be a broken skill!
        if not is_skill and not parse_errors:
            continue

        if is_skill:
            validation_errors = validate_prompt_schema(raw_data)
            errors.extend(validation_errors)

            skill_content, render_errors = render_skill(raw_content, raw_data)
            errors.extend(render_errors)
        else:
            skill_content = None

        if errors:
            health_report.append({
                "file": str(path.relative_to(prompts_path)),
                "errors": errors
            })

        if skill_content:
            write_skill_file(prompts_path, docs_path, path, skill_content, reconciler)

    reconciler.reconcile(prune_empty_dirs=False)
    generate_health_dashboard(docs_path, health_report)
