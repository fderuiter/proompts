#!/usr/bin/env python3
"""Create overview.md files for prompt directories if missing."""

from pathlib import Path
import sys
import json

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE_DIRS = {"docs", "scripts", ".github"}


def title_from_json(path: Path) -> str:
    """Return prompt title from a JSON file or fallback to filename."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        title = data.get("title")
        if title:
            return str(title).strip()
    except Exception:
        pass
    name = path.stem
    if name.split("_", 1)[0].isdigit():
        name = name.split("_", 1)[1]
    return name.replace("_", " ").title()


def generate_overview(directory: Path) -> str:
    title = directory.name.replace("_", " ").title()
    lines = [f"# {title} Overview", ""]
    for file in sorted(directory.glob("*.json")):
        heading = title_from_json(file)
        lines.append(f"- [{heading}]({file.name})")
    return "\n".join(lines).rstrip() + "\n"


def ensure_overview(directory: Path) -> bool:
    path = directory / "overview.md"
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
