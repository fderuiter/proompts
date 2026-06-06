import os
from pathlib import Path
from typing import Dict, Any, Set
import jinja2.meta
from jinja2.sandbox import SandboxedEnvironment

def extract_undeclared_variables(text: str) -> Set[str]:
    env = SandboxedEnvironment()
    try:
        ast = env.parse(text)
        return jinja2.meta.find_undeclared_variables(ast)
    except Exception:
        return set()

def generate_skill_content(data: Dict[str, Any], raw_data: Dict[str, Any], raw_content: str) -> str:
    description = data.get("description", "")
    
    # Extract variables from the entire raw_content using Jinja parser
    variables = extract_undeclared_variables(raw_content)
    
    messages_text = []
    
    # Use raw_data for unrendered instructions
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

def process_skills(prompts_path: Path, docs_path: Path):
    from promptops.utils import iter_prompt_files, load_yaml
    
    out_skills_dir = docs_path / "skills"
    
    for path in iter_prompt_files(str(prompts_path)):
        data = load_yaml(str(path))
        if not data:
            continue
            
        metadata = data.get("metadata", {})
        tags = metadata.get("tags", [])
        
        if "skill" in tags:
            import yaml
            try:
                raw_content = path.read_text(encoding='utf-8')
                raw_data = yaml.safe_load(raw_content)
            except Exception:
                raw_content = ""
                raw_data = data
                
            skill_content = generate_skill_content(data, raw_data, raw_content)
            
            # Create directory for skill
            clean_name = path.name.replace('.prompt.yaml', '').replace('.yaml', '')
            rel_to_prompts = path.relative_to(prompts_path)
            skill_dir = out_skills_dir / rel_to_prompts.parent / clean_name
            skill_dir.mkdir(parents=True, exist_ok=True)
            
            skill_file = skill_dir / "SKILL.md"
            
            # Idempotent write
            if skill_file.exists():
                existing_content = skill_file.read_text(encoding='utf-8')
                if existing_content == skill_content:
                    continue
                    
            skill_file.write_text(skill_content, encoding='utf-8')
