from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
PROMPTS_DIR = ROOT / "prompts"
WORKFLOWS_DIR = ROOT / "workflows"
OVERVIEW_NAME = "overview.md"

class CustomDumper(yaml.Dumper):
    pass

def represent_str(dumper, data):
    if '\n' in data:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(str, represent_str, Dumper=CustomDumper)

def load_yaml(path: Path) -> dict:
    """Safe load YAML with error handling."""
    try:
        if not path.exists():
            return {}
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return {}

def dump_yaml_str(data: dict) -> str:
    """Dump dictionary to YAML string with custom formatting for multiline strings."""
    return yaml.dump(data, Dumper=CustomDumper, default_flow_style=False, sort_keys=False, allow_unicode=True, width=120)

def iter_prompt_files(root: Path = PROMPTS_DIR):
    """Yield all prompt files recursively (skips macOS ._ resource forks)."""
    if not root.exists():
        return
    for ext in ("*.prompt.yaml", "*.prompt.yml"):
        for p in root.rglob(ext):
            if not p.name.startswith("._"):
                yield p

def iter_workflow_files(root: Path = WORKFLOWS_DIR):
    """Yield all workflow files recursively (skips macOS ._ resource forks)."""
    if not root.exists():
        return
    for p in root.rglob("*.workflow.yaml"):
        if not p.name.startswith("._"):
            yield p
