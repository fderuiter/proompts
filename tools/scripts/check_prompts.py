#!/usr/bin/env python3
"""Repository checks for prompt files.

This utility checks YAML-based prompts (``*.prompt.yaml`` and
``*.prompt.yml``) for basic syntax and naming conventions.
"""

from __future__ import annotations

import re
from pathlib import Path

try:
    from utils import PROMPTS_DIR, load_yaml
except ImportError:
    # Allow running from root or scripts dir
    import sys
    sys.path.append(str(Path(__file__).parent))
    from utils import PROMPTS_DIR, load_yaml

OVERVIEW_NAME = "overview.md"  # documentation stays Markdown


NAMING_RULES = {
    "agentic_coding": re.compile(r"^\d\d_.*\.prompt\.ya?ml$", re.IGNORECASE),
    "meta": re.compile(r"^L\d+_.*\.prompt\.ya?ml$", re.IGNORECASE),
}


def check_overview(directory: Path) -> bool:
    if not (directory / OVERVIEW_NAME).exists():
        print(f"Missing {OVERVIEW_NAME} in {directory}")
        return False
    return True


def check_files(directory: Path) -> bool:
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

        if not load_yaml(file):
            print(f"Failed to parse {file}")
            ok = False
            continue
        if directory.name in NAMING_RULES:
            pattern = NAMING_RULES[directory.name]
            if not pattern.match(name):
                print(f"{file} does not match required pattern for {directory.name}")
                ok = False
    return ok


def main() -> int:
    success = True
    for category_dir in PROMPTS_DIR.iterdir():
        if not category_dir.is_dir():
            continue
        if not check_overview(category_dir):
            success = False
        if category_dir.name == "meta":
            if not check_files(category_dir):
                success = False
            continue
        for prompt_dir in category_dir.iterdir():
            if not prompt_dir.is_dir():
                continue
            if not check_overview(prompt_dir):
                success = False
            if not check_files(prompt_dir):
                success = False
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
