#!/usr/bin/env python3
"""Repository checks for prompt files.

This utility checks YAML-based prompts (``*.prompt.yaml`` and
``*.prompt.yml``) for basic syntax and naming conventions.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

OVERVIEW_NAME = "overview.md"  # documentation stays Markdown

ROOT = Path(__file__).resolve().parents[2]
PROMPTS_DIR = ROOT / "prompts"


NUMERIC_RE = re.compile(r"^\d\d_.*\.prompt\.ya?ml$", re.IGNORECASE)
LEVEL_RE = re.compile(r"^L\d+_.*\.prompt\.ya?ml$", re.IGNORECASE)


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

        try:
            text = file.read_text(encoding="utf-8")
            yaml.safe_load(text)
        except Exception as exc:  # pragma: no cover - simple validation
            print(f"Failed to parse {file}: {exc}")
            ok = False
            continue
        if directory.name == "agentic_coding" and not NUMERIC_RE.match(name):
            print(f"{file} does not follow numeric prefix naming")
            ok = False
        if directory.name == "meta" and not LEVEL_RE.match(name):
            print(f"{file} does not follow L#_ naming")
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
