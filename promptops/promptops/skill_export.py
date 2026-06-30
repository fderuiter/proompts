import os
import json
from pathlib import Path
from typing import Dict, Any, Set, List, Optional
import yaml
from pydantic import ValidationError

# To avoid circular imports, we don't import PromptSchema here if not needed
# or we import it inside functions.

def generate_skill_section(prompt_data: Dict[str, Any]) -> str:
    """Generate a single skill section for a prompt."""
    name = prompt_data.get("name", "Unnamed Skill")
    description = prompt_data.get("description", "No description provided.")
    
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

    instructions = "\n\n".join(instructions_blocks)

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
        few_shots.append(f"Input Context: \"{input_ctx}\"\nAsserted Output: \"{expected}\"")

    few_shot_text = "\n\n".join(few_shots) if few_shots else "None provided."

    # Store structured variables for runtime in a hidden comment block or similar?
    # Better to have it parseable.
    vars_json = json.dumps(variables)

    section = f"""## Skill: {name}
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
    from promptops.tags import extract_tags, extract_tags_from_text
    if raw_data and isinstance(raw_data, dict):
        if "skill" in extract_tags(raw_data):
            return True
    return "skill" in extract_tags_from_text(raw_content)

def process_skills(prompts_path: Path, docs_path: Optional[Path] = None):
    from promptops.utils import iter_prompt_files, load_yaml
    from promptops.sync import DirectoryReconciler
    
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

    docs_reconciler = DirectoryReconciler(docs_path / "skills", manage_pattern="skills.md") if docs_path else None

    # Migration: consolidate any remaining loose files into skills.md and purge them
    for directory, prompt_paths in prompts_by_dir.items():
        prompts_data = [load_yaml(p) for p in prompt_paths]
        skills_content = generate_skills_md(directory, prompts_path, prompts_data)
        skills_file = directory / "skills.md"
        skills_file.write_text(skills_content, encoding='utf-8')
        
        # Mandatory purge
        for p in prompt_paths:
            print(f"Purging source file: {p}")
            p.unlink()
            
    # For docs, copy the persistent manifest files
    if docs_reconciler and docs_path:
        for root, dirs, files in os.walk(prompts_path):
            if "skills.md" in files:
                directory = Path(root)
                rel = directory.relative_to(prompts_path)
                out_dir = docs_path / "skills" / rel
                skills_content = (directory / "skills.md").read_text(encoding='utf-8')
                docs_reconciler.write_file(out_dir / "skills.md", skills_content)
        docs_reconciler.reconcile()
