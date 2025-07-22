#!/usr/bin/env python3
"""Repository checks for prompt files."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE_DIRS = {"docs", "scripts", ".github", "prompt_tools"}


NUMERIC_RE = re.compile(r"^\d\d_.*\.json$")
LEVEL_RE = re.compile(r"^L\d+_.*\.json$")


def check_overview(directory: Path) -> bool:
    if not (directory / "overview.md").exists():
        print(f"Missing overview.md in {directory}")
        return False
    return True


def check_files(directory: Path) -> bool:
    ok = True
    for file in directory.iterdir():
        if not file.is_file() or file.name.startswith('.'):
            continue
        name = file.name
        if name.lower() in {"overview.md", "readme.md"}:
            continue
        if file.suffix.lower() != ".json":
            print(f"{file} is not a JSON file")
            ok = False
            continue
        if directory.name == "agentic_coding" and not NUMERIC_RE.match(name):
            print(f"{file} does not follow numeric prefix naming")
            ok = False
        if directory.name == "meta_prompts" and not LEVEL_RE.match(name):
            print(f"{file} does not follow L#_ naming")
            ok = False
    return ok


def main() -> int:
    success = True
    for d in ROOT.iterdir():
        if not d.is_dir():
            continue
        if d.name in EXCLUDE_DIRS or d.name.startswith('.'):
            continue
        if not check_overview(d):
            success = False
        if not check_files(d):
            success = False
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
