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
ROOT: Path = Path(__file__).resolve().parents[1]
PROMPTS_DIR: Path = ROOT / "prompts"
WORKFLOWS_DIR: Path = ROOT / "workflows"
OVERVIEW_NAME: str = "overview.md"
DOMAIN_TAG_PREFIX: str = "domain:"

_jinja_envs = {}

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

def load_yaml(path: Union[str, Path]) -> Dict[str, Any]:
    path_obj = Path(path)
    try:
        text = path_obj.read_text(encoding="utf-8")
        # To match identical validation and execution inheritance, we use PROMPTS_DIR as base
        # for prompts, or the file's parent for generic files.
        # But tools/scripts/utils.py used PROMPTS_DIR directly for all inheritance:
        # env = _get_jinja_env()  (which hardcodes PROMPTS_DIR)
        env = get_jinja_env(PROMPTS_DIR)
        template = env.from_string(text)
        rendered_text = template.render()
        return yaml.safe_load(rendered_text) or {}
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
    tags: List[str] = []
    metadata = content.get("metadata")
    if isinstance(metadata, dict):
        meta_tags = metadata.get("tags")
        if isinstance(meta_tags, list):
            tags.extend(t for t in meta_tags if isinstance(t, str))

    legacy_tags = content.get("tags")
    if isinstance(legacy_tags, list):
        tags.extend(t for t in legacy_tags if isinstance(t, str))

    return [tag.strip() for tag in tags if tag.strip()]

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
