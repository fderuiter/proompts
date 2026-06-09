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
    """
    Render a skill markdown document from a prompt's raw template content and parsed YAML data.
    
    Parses `raw_content` as a Jinja template to discover undeclared template variables and, when `raw_data` is a dict, generates the skill markdown using those variables and the parsed data. Collects parsing or generation problems as structured error records rather than raising.
    
    Parameters:
        raw_content (str): The raw prompt template text (Jinja-compatible).
        raw_data (Any): The parsed YAML data for the prompt (expected to be a dict when valid).
    
    Returns:
        tuple:
            skill_content (str | None): Generated skill markdown when generation succeeds, otherwise `None`.
            errors (List[Dict[str, Any]]): A list of error records; each record contains:
                - `type` (str): A short error category (e.g., "Jinja2 Syntax Error", "Skill Generation Error").
                - `message` (str): Human-readable error message.
                - `line` (int | "N/A"): Line number related to the error when available, otherwise `"N/A"`.
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

def write_skill_file(prompts_path: Path, docs_path: Path, path: Path, skill_content: str) -> Path:
    """
    Create or update a SKILL.md file for a prompt, preserving the prompts directory structure under docs/skills.
    
    The function determines a cleaned skill directory name from `path`, replicates the path's parent structure relative to `prompts_path` under `docs_path/skills`, ensures the target directory exists, and writes `skill_content` to `SKILL.md`. If an existing SKILL.md already contains identical content, the file is not rewritten.
    
    Parameters:
        prompts_path (Path): Root directory containing source prompt files.
        docs_path (Path): Root documentation directory where `skills/` will be created.
        path (Path): Path to the source prompt file being exported.
        skill_content (str): Markdown content to write into `SKILL.md`.
    
    Returns:
        Path: The path to the existing or newly written `SKILL.md`.
    """
    out_skills_dir = docs_path / "skills"
    clean_name = path.name.replace('.prompt.yaml', '').replace('.yaml', '')
    rel_to_prompts = path.relative_to(prompts_path)
    skill_dir = out_skills_dir / rel_to_prompts.parent / clean_name
    skill_dir.mkdir(parents=True, exist_ok=True)

    skill_file = skill_dir / "SKILL.md"

    if skill_file.exists():
        existing_content = skill_file.read_text(encoding='utf-8')
        if existing_content == skill_content:
            return skill_file

    skill_file.write_text(skill_content, encoding='utf-8')
    return skill_file

def generate_health_dashboard(docs_path: Path, health_report: List[Dict[str, Any]]):
    """
    Write a Markdown dashboard summarizing parsing and validation errors for exported skills.
    
    Creates or overwrites the file `skill_health.md` in `docs_path`. The dashboard contains YAML frontmatter and a header; if `health_report` is empty it includes a success message, otherwise it emits a section per reported file and lists each error as "- **{type}**: {message} (Line: {line})".
    
    Parameters:
        docs_path (Path): Directory where `skill_health.md` will be written.
        health_report (List[Dict[str, Any]]): List of per-file reports. Each report should have a `"file"` key with the file name and an `"errors"` key containing a list of error objects; each error object should include `"type"` and `"message"`, and may include `"line"`.
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

def cleanup_orphaned_skills(docs_path: Path, active_skills: Set[Path]):
    """
    Remove SKILL.md files under the docs_path/skills tree that are not in the provided active_skills set and prune any empty directories left behind.
    
    The function:
    - Treats entries in `active_skills` as resolved filesystem paths and preserves any SKILL.md whose resolved path matches an active path.
    - Walks the docs_path/skills directory bottom-up, deletes SKILL.md files not present in `active_skills`, and removes directories that become empty as long as they are not the root skills directory.
    - Silently ignores filesystem errors when attempting to remove directories and returns immediately if the skills directory does not exist.
    
    Parameters:
        docs_path (Path): Root documentation directory containing the "skills" subdirectory.
        active_skills (Set[Path]): Set of Paths (typically SKILL.md files) that should be kept; paths are resolved before comparison.
    """
    out_skills_dir = docs_path / "skills"
    if not out_skills_dir.exists():
        return

    active_paths = {p.resolve() for p in active_skills}

    # Find all SKILL.md files
    for root, dirs, files in os.walk(out_skills_dir, topdown=False):
        for file in files:
            if file == "SKILL.md":
                file_path = Path(root) / file
                if file_path.resolve() not in active_paths:
                    file_path.unlink()
        
        # Now check if the directory is empty
        try:
            if Path(root).resolve() != out_skills_dir.resolve() and not os.listdir(root):
                Path(root).rmdir()
        except OSError:
            pass

def process_skills(prompts_path: Path, docs_path: Path):
    """
    Process all prompt files under `prompts_path`, export detected skills to `docs_path/skills`, generate a health dashboard, and remove orphaned skill files.
    
    Reads each prompt file, parses and validates its YAML, renders skill content for prompts tagged as skills, and writes/updates a corresponding SKILL.md while tracking exported files. Accumulates parsing/validation/rendering errors into a health report written to `docs_path/skill_health.md`. After exporting, removes any existing SKILL.md files under `docs_path/skills` that were not produced during this run.
    """
    from promptops.utils import iter_prompt_files

    health_report = []
    active_skills: Set[Path] = set()

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
            skill_file = write_skill_file(prompts_path, docs_path, path, skill_content)
            if skill_file:
                active_skills.add(skill_file)

    generate_health_dashboard(docs_path, health_report)
    cleanup_orphaned_skills(docs_path, active_skills)
