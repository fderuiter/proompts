"""Module docstring."""
import os
import json
import re
from pathlib import Path
from typing import Dict, Any, Set, List, Optional
import yaml
from pydantic import ValidationError

# To avoid circular imports, we don't import PromptSchema here if not needed
# or we import it inside functions.

def _redact(text: str) -> str:
    """Missing docstring."""
    if not isinstance(text, str):
        return text
    text = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', '[REDACTED]', text)
    text = re.sub(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', '[REDACTED_EMAIL]', text)
    text = re.sub(r'(?:\+\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', '[REDACTED_PHONE]', text)
    text = re.sub(r'\b(?:\d{4}[-/]\d{1,2}[-/]\d{1,2}|\d{1,2}[-/]\d{1,2}[-/]\d{2,4})\b', '[REDACTED_DATE]', text)
    return text

def _generate_skill_description(prompt_data: Dict[str, Any]) -> str:
    """Missing docstring."""
    fallback_desc = prompt_data.get("description", "No description provided.")
    api_key = os.environ.get("LLM_API_KEY_SHADOW") or os.environ.get("LLM_API_KEY")
    if not api_key:
        return fallback_desc

    context_data = {
        "name": prompt_data.get("name", "Unnamed Skill"),
        "variables": prompt_data.get("variables", []),
        "messages": prompt_data.get("messages", [])
    }
    
    system_msg = (
        "You are an expert technical documentation specialist. "
        "Analyze the provided prompt instructions, tool calls, and variables. "
        "Generate a concise, objective, and technically accurate summary of the prompt's behavior "
        "and execution context. This description will be used in a skills.md manifest. "
        "Return ONLY the description text, with no markdown code blocks, quotes, or conversational filler."
    )
    
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": json.dumps(context_data, indent=2)}
        ],
        "temperature": 0.0
    }
    
    import urllib.request
    import urllib.error
    
    req = urllib.request.Request(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        data=json.dumps(payload).encode("utf-8")
    )
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            result = json.loads(response.read().decode("utf-8"))
            content = result["choices"][0]["message"]["content"]
            content = content.strip().strip('"').strip("'").strip()
            if content:
                return content
    except Exception as e:
        print(f"LLM API call failed for description generation: {e}")
        pass
        
    return fallback_desc

def generate_skill_section(prompt_data: Dict[str, Any]) -> str:
    """Generate a single skill section for a prompt."""
    name = prompt_data.get("name", "Unnamed Skill")
    description = _generate_skill_description(prompt_data)
    
    metadata = prompt_data.get("metadata", {})
    autonomy = metadata.get("autonomy")
    maturity = metadata.get("maturity")
    
    badges = []
    if autonomy:
        badges.append(f"![Autonomy: {autonomy}](https://img.shields.io/badge/Autonomy-{autonomy}-blue)")
    if maturity:
        badges.append(f"![Maturity: {maturity}](https://img.shields.io/badge/Maturity-{maturity}-green)")
    
    badge_str = " " + " ".join(badges) if badges else ""
    
    # Inputs table
    variables = prompt_data.get("variables", [])
    input_table = "| Variable | Type | Description | Required |\n| :--- | :--- | :--- | :--- |\n"
    if not variables:
        input_table += "| None | | | |\n"
    for v in variables:
        v_name = v.get("name", "")
        v_type = "String"
        v_desc = v.get("description", "No description provided.")
        v_req = "Yes" if v.get("required", True) else "No"
        input_table += f"| `{v_name}` | {v_type} | {v_desc} | {v_req} |\n"

    # Core Instructions
    messages = prompt_data.get("messages", [])
    instructions_blocks = []
    for msg in messages:
        role = msg.get("role", "unknown").upper()
        content = msg.get("content")
        if isinstance(content, list):
            content_str = yaml.dump(content, sort_keys=False).strip()
        elif content is not None:
            content_str = str(content).strip()
        else:
            content_str = ""
            
        if content_str:
            instructions_blocks.append(f"[{role}]\n{content_str}")
            
        tool_calls = msg.get("tool_calls")
        if tool_calls:
            tc_yaml = yaml.dump(tool_calls, sort_keys=False, default_flow_style=False).strip()
            instructions_blocks.append(f"[TOOL_CALL]\n```yaml\n{tc_yaml}\n```")

    instructions = _redact("\n\n".join(instructions_blocks))

    # Response Mapping
    response_mapping = "Expected JSON/YAML structure matching the schema rules."
    if "metadata" in prompt_data and isinstance(prompt_data["metadata"], dict):
        if "response_mapping" in prompt_data["metadata"]:
             response_mapping = prompt_data["metadata"]["response_mapping"]

    # Few-Shot Assertions
    few_shots = []
    test_data = prompt_data.get("testData", [])
    for test in test_data:
        inputs = test.get("vars", test.get("input", {}))
        expected = test.get("expected", "")
        if isinstance(inputs, dict):
            input_ctx = yaml.dump(inputs, sort_keys=False, default_flow_style=True).strip()
        else:
            input_ctx = str(inputs)
        few_shots.append(f"**Input Context:**\n```yaml\n{_redact(input_ctx)}\n```\n**Asserted Output:**\n```text\n{_redact(str(expected))}\n```")

    few_shot_text = "\n\n".join(few_shots) if few_shots else "None provided."

    # Store structured variables for runtime in a hidden comment block or similar?
    # Better to have it parseable.
    validation_data = {
        "variables": variables,
        "metadata": metadata
    }
    vars_json = _redact(json.dumps(validation_data))

    section = f"""## Skill: {name}{badge_str}
<!-- VALIDATION_METADATA: {vars_json} -->
### Description
{description}

### Execution Context (Inputs)
{input_table}

### Core Instructions
```text
{instructions.strip()}
```

### Response Mapping (Outputs)
{response_mapping}

### Few-Shot Assertions
{few_shot_text}
"""
    return section

def generate_skills_md(directory: Path, prompts_path: Path, prompts_data: List[Dict[str, Any]]) -> str:
    """Generate the full skills.md content for a directory."""
    rel_path = directory.relative_to(prompts_path)
    domain_name = " ".join(word.capitalize() for word in str(rel_path).replace("_", " ").split("/"))
    namespace = str(rel_path).replace("/", ".")

    all_tags = set()
    from promptops.tags import extract_tags
    for data in prompts_data:
        all_tags.update(extract_tags(data))

    front_matter = ""
    if all_tags:
        front_matter = "---\n"
        front_matter += "tags:\n"
        for tag in sorted(all_tags):
            front_matter += f"  - {tag}\n"
        front_matter += "---\n\n"

    header = f"# Domain Agent Skills: {domain_name}\n\n"
    metadata = f"""## Metadata
- **Domain Namespace:** {namespace}
- **Target Runtime:** PromptOps / MCP Server
- **Validation Schema:** docs/schemas/prompt.schema.json

---
"""
    sections = [generate_skill_section(data) for data in prompts_data]
    return front_matter + header + metadata + "\n" + "\n---\n\n".join(sections)

def detect_skill(raw_content: str, raw_data: Any) -> bool:
    """Missing docstring."""
    from promptops.tags import extract_tags, extract_tags_from_text
    if raw_data and isinstance(raw_data, dict):
        if "skill" in extract_tags(raw_data):
            return True
    return "skill" in extract_tags_from_text(raw_content)

def process_skills(prompts_path: Path, docs_path: Optional[Path] = None):
    """Missing docstring."""
    print('DEBUG: Entering process_skills')
    from promptops.utils import iter_prompt_files, load_yaml, walk_workspace
    from promptops.sync import DirectoryReconciler
    
    print('DEBUG: Start iter_prompt_files')
    prompts_by_dir: Dict[Path, List[Path]] = {}
    for path in iter_prompt_files(str(prompts_path)):
        try:
            data = load_yaml(path)
            raw_content = path.read_text(encoding='utf-8')
            if not detect_skill(raw_content, data):
                continue
            parent = path.parent
            if parent not in prompts_by_dir:
                prompts_by_dir[parent] = []
            prompts_by_dir[parent].append(path)
        except Exception as e:
            print(f"Error processing {path}: {e}")

    print('DEBUG: Finished iter_prompt_files')
    docs_reconciler = DirectoryReconciler(docs_path / "skills", manage_pattern="skills.md") if docs_path else None

    # Migration: consolidate any remaining loose files into skills.md and purge them
    print('DEBUG: Starting migration loop')
    for directory, prompt_paths in prompts_by_dir.items():
        print(f'DEBUG: Migrating {directory}'); import time; t0=time.time()
        prompts_data = [load_yaml(p) for p in prompt_paths]
        skills_content = generate_skills_md(directory, prompts_path, prompts_data); print(f'DEBUG: generate_skills_md took {time.time()-t0:.2f}s')
        skills_file = directory / "skills.md"
        skills_file.write_text(skills_content, encoding='utf-8'); print(f'DEBUG: wrote file took {time.time()-t0:.2f}s')
        
        # Mandatory purge
        for p in prompt_paths:
            print(f"Purging source file: {p}")
            p.unlink()
            
    # For docs, copy the persistent manifest files
    if docs_reconciler and docs_path:
        for root, dirs, files in walk_workspace(prompts_path):
            # Exclude standard directories and prevent infinite traversal into docs_path
            dirs[:] = [
                d for d in dirs
                if d not in (".git", "venv", ".venv", "__pycache__")
                and (Path(root) / d).resolve() != docs_path.resolve()
            ]
            if "skills.md" in files:
                directory = Path(root)
                rel = directory.relative_to(prompts_path)
                out_dir = docs_path / "skills" / rel
                skills_content = (directory / "skills.md").read_text(encoding='utf-8')
                
                # Dynamically inject badges for MkDocs
                from promptops.utils import parse_skill_manifest
                try:
                    manifest = parse_skill_manifest(directory / "skills.md")
                    
                    # Also append tags for MkDocs search indexing if any skill has tags
                    doc_tags = set()
                    
                    for skill in manifest.get("skills", []):
                        meta = skill.get("metadata", {})
                        autonomy = meta.get("autonomy")
                        maturity = meta.get("maturity")
                        
                        if autonomy: doc_tags.add(autonomy)
                        if maturity: doc_tags.add(maturity)
                        
                        badges = []
                        if autonomy:
                            badges.append(f"![Autonomy: {autonomy}](https://img.shields.io/badge/Autonomy-{autonomy}-blue)")
                        if maturity:
                            badges.append(f"![Maturity: {maturity}](https://img.shields.io/badge/Maturity-{maturity}-green)")
                            
                        if badges:
                            badge_str = " " + " ".join(badges)
                            # Replace the header for this skill to include the badge
                            old_header = f"## Skill: {skill['name']}"
                            if old_header in skills_content:
                                skills_content = skills_content.replace(old_header, old_header + badge_str)
                    
                    if doc_tags:
                        tags_block = "tags:\n" + "\n".join(f"  - {t}" for t in doc_tags)
                        import re
                        if re.search(r'^---\n', skills_content, re.MULTILINE):
                            # Inject into existing frontmatter
                            skills_content = re.sub(r'^---\n', f"---\n{tags_block}\n", skills_content, count=1, flags=re.MULTILINE)
                        else:
                            skills_content = f"---\n{tags_block}\n---\n\n" + skills_content
                                
                except Exception as e:
                    print(f"Error injecting badges into {directory / 'skills.md'}: {e}")
                
                docs_reconciler.write_file(out_dir / "skills.md", skills_content)
        docs_reconciler.reconcile()
