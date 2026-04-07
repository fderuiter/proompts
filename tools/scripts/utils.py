import re
from pathlib import Path
import yaml
from typing import Iterator, Dict, Any, List

ROOT = Path(__file__).resolve().parents[2]
PROMPTS_DIR = ROOT / "prompts"
WORKFLOWS_DIR = ROOT / "workflows"
OVERVIEW_NAME = "overview.md"

def load_yaml(path: Path) -> Dict[str, Any]:
    """Safe load YAML with error handling."""
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return {}

def iter_prompt_files(root: Path = PROMPTS_DIR) -> Iterator[Path]:
    """Yield all prompt files recursively (skips macOS ._ resource forks and site/ directory)."""
    for ext in ("*.prompt.yaml", "*.prompt.yml"):
        for p in root.rglob(ext):
            if not p.name.startswith("._") and "site/" not in str(p):
                yield p

def iter_workflow_files(root: Path = WORKFLOWS_DIR) -> Iterator[Path]:
    """Yield all workflow files recursively (skips macOS ._ resource forks)."""
    for p in root.rglob("*.workflow.yaml"):
        if not p.name.startswith("._"):
            yield p

def extract_template_vars(content: Dict[str, Any]) -> List[str]:
    """Extract all {{var}} patterns from messages."""
    found: set[str] = set()
    for msg in content.get("messages", []):
        text = msg.get("content", "")
        found.update(re.findall(r'\{\{([^}]+)\}\}', text))
    return sorted(found)
