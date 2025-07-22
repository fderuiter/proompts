#!/usr/bin/env python3
"""Create ``overview.md`` files for prompt directories if missing."""

from pathlib import Path
import sys

OVERVIEW_NAME = "overview.md"  # documentation remains in Markdown

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE_DIRS = {"docs", "scripts", ".github"}


def heading_from_file(path: Path) -> str:
    """Return first Markdown heading or fallback to filename."""
    try:
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped.startswith("#"):
                    return stripped.lstrip("#").strip()
    except FileNotFoundError:
        pass
    name = path.stem
    if name.split("_", 1)[0].isdigit():
        name = name.split("_", 1)[1]
    return name.replace("_", " ").title()


def generate_overview(directory: Path) -> str:
    title = directory.name.replace("_", " ").title()
    lines = [f"# {title} Overview", ""]
    for file in sorted(directory.glob("*.md")):
        if file.name.lower() in {OVERVIEW_NAME, "readme.md"}:
            continue
        heading = heading_from_file(file)
        lines.append(f"- [{heading}]({file.name})")
    return "\n".join(lines).rstrip() + "\n"


def ensure_overview(directory: Path) -> bool:
    path = directory / OVERVIEW_NAME
    if path.exists():
        return False
    content = generate_overview(directory)
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    changed = False
    for d in ROOT.iterdir():
        if not d.is_dir():
            continue
        if d.name in EXCLUDE_DIRS or d.name.startswith('.'):
            continue
        if ensure_overview(d):
            print(f"Generated overview for {d}")
            changed = True
    return 0 if changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
