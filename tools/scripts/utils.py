"""
utils.py: Core Shared Utilities

WHAT:
This module contains shared constants and helper functions used by multiple scripts
across the tools directory. It defines common file paths and provides utilities for
reading and iterating over prompt and workflow files.

WHY:
It centralizes core functionality to reduce code duplication and maintain consistency.
For example, it ensures that all scripts skip macOS `._` resource forks when iterating
over files, avoiding parsing errors.

HOW TO USE:
Import constants and functions directly into other scripts:
```python
from utils import PROMPTS_DIR, iter_prompt_files, load_yaml

for prompt_file in iter_prompt_files():
    data = load_yaml(prompt_file)
```
"""

import re
from pathlib import Path
import yaml
from typing import Iterator, Dict, Any, List

ROOT = Path(__file__).resolve().parents[2]
PROMPTS_DIR = ROOT / "prompts"
WORKFLOWS_DIR = ROOT / "workflows"
OVERVIEW_NAME = "overview.md"


def load_yaml(path: Path) -> Dict[str, Any]:
    """
    WHAT: Safely loads and parses a YAML file into a Python dictionary.
    WHY: Handles encoding and parsing errors gracefully so that one bad file doesn't crash a bulk script.
    HOW TO USE:
    ```python
    data = load_yaml(Path("my_file.yaml"))
    if data:
        process(data)
    ```
    """
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return {}


def iter_prompt_files(root: Path = PROMPTS_DIR) -> Iterator[Path]:
    """
    WHAT: Recursively yields all prompt files (`*.prompt.yaml` or `*.prompt.yml`) in a directory tree.
    WHY: Standardizes how scripts discover prompt files, ensuring they skip macOS metadata files (`._*`) and output directories (`site/`).
    HOW TO USE:
    ```python
    for file_path in iter_prompt_files():
        print(f"Found prompt: {file_path}")
    ```
    """
    for ext in ("*.prompt.yaml", "*.prompt.yml"):
        for p in root.rglob(ext):
            if not p.name.startswith("._") and "site/" not in str(p):
                yield p


def iter_workflow_files(root: Path = WORKFLOWS_DIR) -> Iterator[Path]:
    """
    WHAT: Recursively yields all workflow files (`*.workflow.yaml`) in a directory tree.
    WHY: Standardizes how scripts discover workflow files, ensuring they skip macOS metadata files (`._*`).
    HOW TO USE:
    ```python
    for file_path in iter_workflow_files():
        print(f"Found workflow: {file_path}")
    ```
    """
    for p in root.rglob("*.workflow.yaml"):
        if not p.name.startswith("._"):
            yield p


def extract_template_vars(content: Dict[str, Any]) -> List[str]:
    """
    WHAT: Extracts all template variables (patterns like `{{var}}`) from the `messages` array in a prompt object.
    WHY: Used by validation scripts to ensure all variables used in messages are properly defined in the prompt's `variables` block.
    HOW TO USE:
    ```python
    prompt_data = load_yaml(Path("my_prompt.yaml"))
    vars_used = extract_template_vars(prompt_data)
    # vars_used might be ['input_text', 'user_name']
    ```
    """
    found: set[str] = set()
    for msg in content.get("messages", []):
        text = msg.get("content", "")
        found.update(re.findall(r'\{\{([^}]+)\}\}', text))
    return sorted(found)
