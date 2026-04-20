"""
Shared utilities for repository scripts.

WHAT:
Provides shared constants (like directory paths) and helper functions for
parsing and interacting with prompt and workflow files safely.

WHY:
Centralizing these operations reduces cognitive load and ensures consistency across
scripts, preventing duplicate bugs (like processing macOS resource forks).

HOW:
Import constants or helper functions from this module in other python scripts.
Example: `from utils import PROMPTS_DIR, iter_prompt_files, load_yaml`
"""

import re
from pathlib import Path
import yaml
from typing import Iterator, Dict, Any, List, Set

ROOT: Path = Path(__file__).resolve().parents[2]
PROMPTS_DIR: Path = ROOT / "prompts"
WORKFLOWS_DIR: Path = ROOT / "workflows"
OVERVIEW_NAME: str = "overview.md"

def load_yaml(path: Path) -> Dict[str, Any]:
    """
    Safely load a YAML file and return its contents as a dictionary.

    WHAT: Wrapper around yaml.safe_load that includes text decoding and basic error handling.
    WHY: Prevents scripts from crashing completely if a single YAML file is malformed.
    HOW: Pass a pathlib.Path object pointing to the YAML file.

    Args:
        path (Path): The file path to read.

    Returns:
        Dict[str, Any]: The parsed YAML data, or an empty dict if parsing fails.
    """
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return {}

def iter_prompt_files(root: Path = PROMPTS_DIR) -> Iterator[Path]:
    """
    Recursively yield all valid prompt YAML files within a directory.

    WHAT: An iterator for prompt files (`*.prompt.yaml` or `*.prompt.yml`).
    WHY: Provides a single source of truth for finding valid prompts, skipping
         problematic hidden files like macOS `._*` resource forks which cause parsing errors,
         as well as build directories like `site/`.
    HOW: Call in a for loop to process prompts across the codebase.

    Args:
        root (Path): The base directory to search. Defaults to PROMPTS_DIR.

    Yields:
        Iterator[Path]: Path objects for valid prompt files.
    """
    for ext in ("*.prompt.yaml", "*.prompt.yml"):
        for p in root.rglob(ext):
            if not p.name.startswith("._") and "site/" not in str(p):
                yield p

def iter_workflow_files(root: Path = WORKFLOWS_DIR) -> Iterator[Path]:
    """
    Recursively yield all valid workflow YAML files within a directory.

    WHAT: An iterator for workflow files (`*.workflow.yaml`).
    WHY: Provides a consistent way to find workflows while ignoring `._*` resource forks.
    HOW: Call in a for loop to process workflows across the codebase.

    Args:
        root (Path): The base directory to search. Defaults to WORKFLOWS_DIR.

    Yields:
        Iterator[Path]: Path objects for valid workflow files.
    """
    for p in root.rglob("*.workflow.yaml"):
        if not p.name.startswith("._"):
            yield p

def extract_template_vars(content: Dict[str, Any]) -> List[str]:
    """
    Extract all Jinja-style variable patterns `{{var}}` from prompt messages.

    WHAT: Scans the 'messages' block of a prompt dictionary and extracts variables.
    WHY: Used by validation scripts to ensure all declared variables are actually utilized
         in the prompt, and vice versa.
    HOW: Pass the loaded YAML dictionary to this function.

    Args:
        content (Dict[str, Any]): The loaded prompt dictionary containing 'messages'.

    Returns:
        List[str]: A sorted list of unique variable names found in the template.
    """
    found: Set[str] = set()
    for msg in content.get("messages", []):
        text = msg.get("content", "")
        if isinstance(text, str):
            found.update(re.findall(r'\{\{([^}]+)\}\}', text))
    return sorted(list(found))
