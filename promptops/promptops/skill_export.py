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

def generate_skill_content(data: Dict[str, Any], raw_data: Dict[str, Any], raw_content: str) -> str:
    description = data.get("description", "")
    
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
    
    out_skills_dir = docs_path / "skills"
    health_report = []
    
    for path in iter_prompt_files(str(prompts_path)):
        errors = []
        raw_content = ""
        raw_data = None
        
        try:
            raw_content = path.read_text(encoding='utf-8')
        except Exception as e:
            continue
            
        try:
            raw_data = yaml.safe_load(raw_content)
        except yaml.YAMLError as e:
            line = getattr(e, 'problem_mark', None) and e.problem_mark.line + 1 or "N/A"
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
            
        is_skill = False
        if raw_data and isinstance(raw_data, dict):
            metadata = raw_data.get("metadata", {})
            tags = metadata.get("tags", [])
            if "skill" in tags:
                is_skill = True
        else:
            if "skill" in raw_content:
                is_skill = True
                
        if not is_skill:
            continue
            
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
        
        skill_content = None
        try:
            env = SandboxedEnvironment()
            env.parse(raw_content)
            
            if raw_data and isinstance(raw_data, dict):
                skill_content = generate_skill_content(raw_data, raw_data, raw_content)
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
            
        if errors:
            health_report.append({
                "file": str(path.relative_to(prompts_path)),
                "errors": errors
            })
            
        if skill_content:
            clean_name = path.name.replace('.prompt.yaml', '').replace('.yaml', '')
            rel_to_prompts = path.relative_to(prompts_path)
            skill_dir = out_skills_dir / rel_to_prompts.parent / clean_name
            skill_dir.mkdir(parents=True, exist_ok=True)
            
            skill_file = skill_dir / "SKILL.md"
            
            if skill_file.exists():
                existing_content = skill_file.read_text(encoding='utf-8')
                if existing_content == skill_content:
                    continue
                    
            skill_file.write_text(skill_content, encoding='utf-8')
            
    generate_health_dashboard(docs_path, health_report)
