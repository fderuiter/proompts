import re
import os
from pathlib import Path
import yaml
from typing import Iterator, Dict, Any, List, Optional, Set, Union

from jinja2.sandbox import SandboxedEnvironment
from jinja2 import FileSystemLoader, Undefined, meta, Environment

class KeepUndefined(Undefined):
    def __getattr__(self, name):
        return KeepUndefined(name=f"{self._undefined_name}.{name}")
        
    def __getitem__(self, key):
        return KeepUndefined(name=f"{self._undefined_name}['{key}']")
        
    def __str__(self):
        return f"{{{{ {self._undefined_name} }}}}"

# Centralized Path Registry
def _find_root() -> Path:
    current = Path.cwd().resolve()
    while current != current.parent:
        if (current / "prompts").exists() and (current / "workflows").exists():
            return current
        current = current.parent
    # Fallback to file-relative if running in an editable install but not from repo
    fallback = Path(__file__).resolve().parents[2]
    if (fallback / "prompts").exists():
        return fallback
    return Path.cwd().resolve()

ROOT: Path = _find_root()
PROMPTS_DIR: Path = ROOT / "prompts"
WORKFLOWS_DIR: Path = ROOT / "workflows"
OVERVIEW_NAME: str = "overview.md"
DOMAIN_TAG_PREFIX: str = "domain:"


def load_yaml(path: Union[str, Path]) -> Dict[str, Any]:
    path_obj = Path(path)
    try:
        text = path_obj.read_text(encoding="utf-8")
        # To match identical validation and execution inheritance, we use PROMPTS_DIR as base
        # for prompts, or the file's parent for generic files.
        # But tools/scripts/utils.py used PROMPTS_DIR directly for all inheritance:
        # env = _get_jinja_env()  (which hardcodes PROMPTS_DIR)
        from promptops.engine import get_jinja_env
        env = get_jinja_env(base_dir=str(PROMPTS_DIR))
        template = env.from_string(text)
        rendered_text = template.render()
        
        if rendered_text.startswith("---"):
            parts = rendered_text.split("---", 2)
            if len(parts) >= 3:
                data = yaml.safe_load(parts[1]) or {}
                content = parts[2]
                
                messages = data.get("messages", [])
                blocks = re.split(r'^##\s+(.*)$', content, flags=re.MULTILINE)
                for i in range(1, len(blocks), 2):
                    header = blocks[i].strip()
                    body = blocks[i+1].strip()
                    if not body:
                        continue
                        
                    role = header.lower()
                    if role == 'purpose':
                        role = 'system'
                    elif role == 'instructions':
                        role = 'user'
                        
                    messages.append({"role": role, "content": body})
                data["messages"] = messages
                return data
                
        return yaml.safe_load(rendered_text) or {}
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return {}

def iter_prompt_files(root: Optional[Union[str, Path]] = None) -> Iterator[Path]:
    from promptops.registry import AssetRegistry
    registry = AssetRegistry(root)
    for asset in registry.discover_assets():
        if asset['type'] == 'prompt':
            yield Path(asset['file_path'])

def iter_workflow_files(root: Optional[Union[str, Path]] = None) -> Iterator[Path]:
    from promptops.registry import AssetRegistry
    registry = AssetRegistry(root)
    for asset in registry.discover_assets():
        if asset['type'] == 'workflow':
            yield Path(asset['file_path'])

def _format_category(raw: str) -> str:
    cleaned = raw.strip().replace("_", " ").replace("-", " ").replace("/", " ")
    return " ".join(word.capitalize() for word in cleaned.split())

def _domain_root(value: str) -> str:
    return value.strip().split("/", 1)[0].strip()

def get_prompt_tags(content: Dict[str, Any]) -> List[str]:
    from promptops.tags import extract_tags
    return extract_tags(content)

def derive_prompt_category(path: Path, root_dir: Path, content: Optional[Dict[str, Any]] = None) -> str:
    from promptops.registry import AssetRegistry
    return AssetRegistry.derive_category(content or {}, path)

def extract_template_vars(content: Dict[str, Any]) -> List[str]:
    found: Set[str] = set()
    env = Environment()
    for msg in content.get("messages", []):
        text = msg.get("content", "")
        if isinstance(text, str):
            try:
                ast = env.parse(text)
                vars_in_text = meta.find_undeclared_variables(ast)
                found.update(vars_in_text)
            except Exception as e:
                raise ValueError(f"Failed to parse template for variables: {e}")
    return sorted(list(found))

def iter_skill_manifests(root: Optional[Union[str, Path]] = None) -> Iterator[Path]:
    root_path = Path(root) if root else PROMPTS_DIR
    for p in root_path.rglob("skills.md"):
        if not p.name.startswith("._") and "site/" not in str(p):
            yield p

def parse_skill_manifest(path: Path) -> Dict[str, Any]:
    import json
    text = path.read_text(encoding='utf-8')
    metadata: Dict[str, Any] = {}
    content = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            try:
                metadata = yaml.safe_load(parts[1]) or {}
                content = parts[2]
            except:
                pass
    skills = []
    import re
    # Match skills and metadata
    skill_blocks = re.split(r'## Skill: ', content)[1:]
    for block in skill_blocks:
        lines = block.splitlines()
        name = lines[0].strip()
        body = "\n".join(lines[1:])

        # Extract metadata
        meta_match = re.search(r'<!-- VALIDATION_METADATA: (.*?) -->', body)
        vars_data = []
        if meta_match:
            try:
                vars_data = json.loads(meta_match.group(1))
            except:
                pass

        # Extract core instructions
        instr_match = re.search(r'### Core Instructions\n```text\n(.*?)```', body, re.DOTALL)
        instructions = instr_match.group(1).strip() if instr_match else ""

        # Render instructions using jinja to evaluate any macros (like load_yaml does)
        try:
            from promptops.engine import get_jinja_env
            env = get_jinja_env(base_dir=str(PROMPTS_DIR))
            if 'macros.' in instructions and not '{% import' in instructions:
                instructions = '{% import "common/macros.j2" as macros %}\n' + instructions
            template = env.from_string(instructions)
            instructions = template.render()
        except Exception as e:
            pass

        # Extract description
        desc_match = re.search(r'### Description\n(.*?)(?=\n### |$)', body, re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""

        # Extract Few-Shot Assertions / testData
        test_data = []
        few_shot_match = re.search(r'### Few-Shot Assertions\n(.*)', body, re.DOTALL)
        if few_shot_match:
            few_shots_text = few_shot_match.group(1).strip()
            # simple parser for Input Context: "..." \n Asserted Output: "..."
            import ast
            blocks = re.findall(r'Input Context:\s*"(.*?)"\nAsserted Output:\s*"(.*?)"', few_shots_text, re.DOTALL)
            for inp_str, out_str in blocks:
                try:
                    inp_dict = yaml.safe_load(inp_str)
                    if not isinstance(inp_dict, dict):
                        inp_dict = {"input": inp_str}
                except:
                    inp_dict = {"input": inp_str}
                test_data.append({"inputs": inp_dict, "expected": [out_str]})

        skills.append({
            "name": name,
            "description": description,
            "variables": vars_data,
            "instructions": instructions,
            "testData": test_data,
            "path": path
        })
    return {"metadata": metadata, "skills": skills, "path": path}
