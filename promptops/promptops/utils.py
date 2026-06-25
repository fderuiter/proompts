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

_jinja_envs: Dict[str, SandboxedEnvironment] = {}

def get_jinja_env(base_dir: Optional[Union[str, Path]] = None) -> SandboxedEnvironment:
    if base_dir is None:
        base_dir = PROMPTS_DIR
    base_dir_str = str(base_dir)
    if base_dir_str not in _jinja_envs:
        _jinja_envs[base_dir_str] = SandboxedEnvironment(
            loader=FileSystemLoader(base_dir_str),
            undefined=KeepUndefined
        )
    return _jinja_envs[base_dir_str]

def _deep_merge(dict1: dict, dict2: dict) -> dict:
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    return result

def load_yaml(path: Union[str, Path]) -> Dict[str, Any]:
    path_obj = Path(path).resolve()
    try:
        text = path_obj.read_text(encoding="utf-8")
        env = get_jinja_env(PROMPTS_DIR)
        template = env.from_string(text)
        rendered_text = template.render()
        data = yaml.safe_load(rendered_text) or {}

        # Only apply inheritance to prompt files
        if path_obj.name.endswith(".prompt.yaml") or path_obj.name.endswith(".prompt.yml"):
            defaults = {}
            current_dir = path_obj.parent
            # Traverse up to PROMPTS_DIR (or stop if we hit root or don't see it)
            dirs_to_check = []
            while current_dir != current_dir.parent:
                dirs_to_check.insert(0, current_dir)
                if current_dir == PROMPTS_DIR or current_dir.name == "prompts":
                    break
                current_dir = current_dir.parent
            
            for d in dirs_to_check:
                defaults_file = d / "defaults.yaml"
                if defaults_file.exists():
                    try:
                        d_text = defaults_file.read_text(encoding="utf-8")
                        d_template = env.from_string(d_text)
                        d_data = yaml.safe_load(d_template.render()) or {}
                        defaults = _deep_merge(defaults, d_data)
                    except Exception as e:
                        print(f"Error reading {defaults_file}: {e}")
            
            # Merge defaults with prompt data (prompt data overrides defaults)
            if defaults:
                data = _deep_merge(defaults, data)

            # Normalize modelParameters aliases to prevent duplicate keys during extra='forbid' validation
            if "modelParameters" in data and isinstance(data["modelParameters"], dict):
                aliases = {
                    "maxTokens": "max_tokens",
                    "topP": "top_p",
                    "frequencyPenalty": "frequency_penalty",
                    "presencePenalty": "presence_penalty"
                }
                for old_key, new_key in aliases.items():
                    if old_key in data["modelParameters"]:
                        if new_key not in data["modelParameters"]:
                            data["modelParameters"][new_key] = data["modelParameters"][old_key]
                        del data["modelParameters"][old_key]

        return data
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return {}

def iter_prompt_files(root: Optional[Union[str, Path]] = None) -> Iterator[Path]:
    root_path = Path(root) if root else PROMPTS_DIR
    for ext in ("*.prompt.yaml", "*.prompt.yml"):
        for p in root_path.rglob(ext):
            if not p.name.startswith("._") and "site/" not in str(p):
                yield p

def iter_workflow_files(root: Optional[Union[str, Path]] = None) -> Iterator[Path]:
    root_path = Path(root) if root else WORKFLOWS_DIR
    for p in root_path.rglob("*.workflow.yaml"):
        if not p.name.startswith("._") and "site/" not in str(p):
            yield p

def _format_category(raw: str) -> str:
    cleaned = raw.strip().replace("_", " ").replace("-", " ").replace("/", " ")
    return " ".join(word.capitalize() for word in cleaned.split())

def _domain_root(value: str) -> str:
    return value.strip().split("/", 1)[0].strip()

def get_prompt_tags(content: Dict[str, Any]) -> List[str]:
    from promptops.tags import extract_tags
    return extract_tags(content)

def derive_prompt_category(path: Path, root_dir: Path, content: Optional[Dict[str, Any]] = None) -> str:
    data = content or {}
    for tag in get_prompt_tags(data):
        if tag.lower().startswith(DOMAIN_TAG_PREFIX):
            value = tag.split(":", 1)[1].strip()
            if value:
                return _format_category(_domain_root(value))

    metadata = data.get("metadata")
    if isinstance(metadata, dict):
        domain = metadata.get("domain")
        if isinstance(domain, str) and domain.strip():
            return _format_category(_domain_root(domain))

    try:
        relative = path.relative_to(root_dir)
        if len(relative.parts) < 2:
            return "Uncategorized"
        return _format_category(relative.parts[0])
    except ValueError:
        return "Uncategorized"

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
            except Exception:
                # Fallback or just skip on parse errors?
                # Using AST could throw TemplateSyntaxError if there's malformed jinja, 
                # but standard execution would also fail. We should ideally just let it pass or extract via regex as fallback?
                # Actually, requirement 2: "Replace regex-based extraction with formal Abstract Syntax Tree (AST) parsing"
                pass
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
        instr_match = re.search(r'### Core Instructions\n```text\n(.*?)\n```', body, re.DOTALL)
        instructions = instr_match.group(1) if instr_match else ""

        skills.append({
            "name": name,
            "variables": vars_data,
            "instructions": instructions,
            "path": path
        })
    return {"metadata": metadata, "skills": skills, "path": path}
