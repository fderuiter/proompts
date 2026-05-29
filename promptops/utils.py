import re
import os
from pathlib import Path
import yaml
from typing import Iterator, Dict, Any, List, Optional, Set

from jinja2.sandbox import SandboxedEnvironment
from jinja2 import FileSystemLoader, Undefined

class KeepUndefined(Undefined):
    def __getattr__(self, name):
        return KeepUndefined(name=f"{self._undefined_name}.{name}")
        
    def __getitem__(self, key):
        return KeepUndefined(name=f"{self._undefined_name}['{key}']")
        
    def __str__(self):
        return f"{{{{ {self._undefined_name} }}}}"

_jinja_envs = {}

def get_jinja_env(base_dir: str):
    if base_dir not in _jinja_envs:
        _jinja_envs[base_dir] = SandboxedEnvironment(
            loader=FileSystemLoader(str(base_dir)),
            undefined=KeepUndefined
        )
    return _jinja_envs[base_dir]

def load_yaml(path: str) -> Dict[str, Any]:
    path_obj = Path(path)
    try:
        text = path_obj.read_text(encoding="utf-8")
        base_dir = path_obj.parent
        env = get_jinja_env(str(base_dir))
        template = env.from_string(text)
        rendered_text = template.render()
        return yaml.safe_load(rendered_text) or {}
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return {}

def iter_prompt_files(root: str) -> Iterator[Path]:
    root_path = Path(root)
    for ext in ("*.prompt.yaml", "*.prompt.yml"):
        for p in root_path.rglob(ext):
            if not p.name.startswith("._") and "site/" not in str(p):
                yield p

def derive_prompt_category(path: Path, root_dir: Path, content: Optional[Dict[str, Any]] = None) -> str:
    DOMAIN_TAG_PREFIX: str = "domain:"
    
    def _format_category(raw: str) -> str:
        cleaned = raw.strip().replace("_", " ").replace("-", " ").replace("/", " ")
        return " ".join(word.capitalize() for word in cleaned.split())

    def _domain_root(value: str) -> str:
        return value.strip().split("/", 1)[0].strip()
        
    data = content or {}
    tags = []
    metadata = data.get("metadata")
    if isinstance(metadata, dict):
        meta_tags = metadata.get("tags")
        if isinstance(meta_tags, list):
            tags.extend(t for t in meta_tags if isinstance(t, str))
            
    legacy_tags = data.get("tags")
    if isinstance(legacy_tags, list):
        tags.extend(t for t in legacy_tags if isinstance(t, str))
        
    tags = [tag.strip() for tag in tags if tag.strip()]

    for tag in tags:
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


def iter_workflow_files(root: str) -> Iterator[Path]:
    root_path = Path(root)
    for p in root_path.rglob("*.workflow.yaml"):
        if not p.name.startswith("._") and "site/" not in str(p):
            yield p
