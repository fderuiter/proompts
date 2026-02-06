#!/usr/bin/env python3
"""Create ``overview.md`` files for prompt directories if missing."""

from __future__ import annotations

from pathlib import Path
import sys

import yaml

OVERVIEW_NAME = "overview.md"  # documentation remains in Markdown

ROOT = Path(__file__).resolve().parents[2]
PROMPTS_DIR = ROOT / "prompts"


def title_from_prompt(path: Path) -> str:
    """Return prompt title from a YAML file or fallback to filename."""
    try:
        text = path.read_text(encoding="utf-8")
        data = yaml.safe_load(text) or {}
        title = data.get("name") or data.get("title")
        if title:
            return str(title).strip()
    except Exception:
        pass
    name = path.name
    for ext in (".prompt.yaml", ".prompt.yml"):
        if name.lower().endswith(ext):
            name = name[: -len(ext)]
            break
    if name.split("_", 1)[0].isdigit():
        name = name.split("_", 1)[1]
    return name.replace("_", " ").title()


def generate_overview(directory: Path) -> str:
    title = directory.name.replace("_", " ").title()
    lines = [f"# {title} Overview", ""]
    prompt_files = []
    for pattern in ("*.prompt.yaml", "*.prompt.yml"):
        prompt_files.extend(directory.glob(pattern))
    for file in sorted(prompt_files):
        heading = title_from_prompt(file)
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
    for category_dir in PROMPTS_DIR.iterdir():
        if not category_dir.is_dir():
            continue
        # For meta prompts, they are directly in the category dir
        if category_dir.name == "meta":
            if ensure_overview(category_dir):
                print(f"Generated overview for {category_dir}")
                changed = True
            continue

        for prompt_dir in category_dir.iterdir():
            if not prompt_dir.is_dir():
                continue
            if ensure_overview(prompt_dir):
                print(f"Generated overview for {prompt_dir}")
                changed = True
    return 0 if changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
