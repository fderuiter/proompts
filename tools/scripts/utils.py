"""Shared utilities for repository scripts.

This module provides common constants and helper functions used across
maintenance and validation scripts, such as path resolution and YAML loading.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Generator

import yaml

# Repository root directory
ROOT = Path(__file__).resolve().parents[2]

# Standard prompts directory
PROMPTS_DIR = ROOT / "prompts"


def load_yaml(path: Path) -> dict[str, Any]:
    """
    Safely load a YAML file with error handling.

    Args:
        path: The path to the YAML file.

    Returns:
        The parsed YAML content as a dictionary, or an empty dict if the file
        could not be read or parsed.
    """
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return {}


def iter_prompt_files(root: Path = PROMPTS_DIR) -> Generator[Path, None, None]:
    """
    Yield all prompt files recursively from a directory.

    Searches for files ending in `.prompt.yaml` or `.prompt.yml`.

    Args:
        root: The root directory to search. Defaults to the repository's
              prompts directory.

    Yields:
        Path objects for each found prompt file.
    """
    for ext in ("*.prompt.yaml", "*.prompt.yml"):
        yield from root.rglob(ext)
