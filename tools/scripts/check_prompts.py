#!/usr/bin/env python3
"""Repository checks for prompt files.

This utility checks YAML-based prompts (``*.prompt.yaml`` and
``*.prompt.yml``) for basic syntax and naming conventions.
"""

from __future__ import annotations

import re
from pathlib import Path

try:
    from utils import PROMPTS_DIR, load_yaml, iter_prompt_files, OVERVIEW_NAME
except ImportError:
    # Allow running from root or scripts dir
    import sys
    sys.path.append(str(Path(__file__).parent))
    from utils import PROMPTS_DIR, load_yaml, iter_prompt_files, OVERVIEW_NAME


NAMING_RULES = {}


def check_overview(directory: Path) -> bool:
    if not (directory / OVERVIEW_NAME).exists():
        print(f"Missing {OVERVIEW_NAME} in {directory}")
        return False
    return True


def check_directory_contents(directory: Path) -> bool:
    """Check for unrecognized files in the directory."""
    ok = True
    for file in directory.iterdir():
        if not file.is_file() or file.name.startswith('.'):
            continue
        name = file.name
        if name.lower() in {OVERVIEW_NAME, "readme.md"}:
            continue

        lower_name = name.lower()
        is_yaml = lower_name.endswith(".prompt.yaml") or lower_name.endswith(
            ".prompt.yml"
        )

        if not is_yaml:
            print(f"{file} is not a recognised prompt file")
            ok = False
            continue

    return ok


def check_prompt_file(file: Path) -> bool:
    """Validate a single prompt file."""
    ok = True
    if not load_yaml(file):
        print(f"Failed to parse {file}")
        ok = False

    directory = file.parent
    if directory.name in NAMING_RULES:
        pattern = NAMING_RULES[directory.name]
        if not pattern.match(file.name):
            print(f"{file} does not match required pattern for {directory.name}")
            ok = False

    return ok


def main() -> int:
    success = True

    # 1. Identify all directories containing prompts (recursively)
    #    and check all prompt files.
    dirs_to_check = set()

    for prompt_file in iter_prompt_files(PROMPTS_DIR):
        if not check_prompt_file(prompt_file):
            success = False

        # Collect directory and all parents up to PROMPTS_DIR
        path = prompt_file.parent
        while path != PROMPTS_DIR:
             dirs_to_check.add(path)
             if path == path.parent: # Safety break
                 break
             path = path.parent

    # 2. Check each directory for overview and stray files
    for directory in dirs_to_check:
        if not check_overview(directory):
            success = False
        if not check_directory_contents(directory):
            success = False

    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
