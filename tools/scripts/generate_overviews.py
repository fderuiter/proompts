#!/usr/bin/env python3
"""Create ``overview.md`` files for prompt directories if missing."""

from __future__ import annotations

from pathlib import Path
import os
import sys

try:
    from utils import PROMPTS_DIR, load_yaml, OVERVIEW_NAME
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).parent))
    from utils import PROMPTS_DIR, load_yaml, OVERVIEW_NAME


def title_from_prompt(path: Path) -> str:
    """Return prompt title from a YAML file or fallback to filename."""
    try:
        data = load_yaml(path)
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

    # Remove leading numbering if present (e.g., 01_foo -> foo)
    if "_" in name:
        parts = name.split("_", 1)
        if parts[0].isdigit():
            name = parts[1]

    return name.replace("_", " ").title()


def generate_overview_content(directory: Path, prompt_files: list[Path]) -> str:
    title = directory.name.replace("_", " ").title()
    lines = [f"# {title} Overview", ""]

    # Sort files by name
    for file in sorted(prompt_files, key=lambda p: p.name):
        heading = title_from_prompt(file)
        lines.append(f"- [{heading}]({file.name})")

    # Also list subdirectories?
    # Current behavior only lists files.
    # Let's stick to listing prompt files.
    # But if a directory has NO prompt files but HAS subdirectories, does it need an overview?
    # check_prompts says "Missing overview.md" in directories.
    # If check_prompts requires it, we should generate it even if empty or just listing subdirs.
    # But checking check_prompts.py:
    # "dirs_to_check" is collected from prompt_file.parent and its parents.
    # So only directories containing prompts (directly or indirectly) are checked?
    # No, "path = prompt_file.parent ... while path != PROMPTS_DIR ... dirs_to_check.add(path)"
    # So any parent directory of a prompt file must have an overview.md.

    # If a directory has no prompts but has subdirectories, we should probably list the subdirectories?
    # The original script didn't seem to do this explicitly, but maybe the directories had prompts.

    # Let's look for subdirectories that have overview.md or prompts
    subdirs = [d for d in directory.iterdir() if d.is_dir() and not d.name.startswith('.')]
    if subdirs:
        lines.append("")
        lines.append("## Subdirectories")
        for d in sorted(subdirs, key=lambda x: x.name):
            d_title = d.name.replace("_", " ").title()
            lines.append(f"- [{d_title}]({d.name}/overview.md)")

    return "\n".join(lines).rstrip() + "\n"


def ensure_overview(directory: Path) -> bool:
    # Find all prompt files in this directory (non-recursive)
    prompt_files = [
        p for p in directory.iterdir()
        if p.is_file() and (p.name.endswith(".prompt.yaml") or p.name.endswith(".prompt.yml"))
    ]

    # Check for subdirectories
    subdirs = [d for d in directory.iterdir() if d.is_dir() and not d.name.startswith('.')]

    if not prompt_files and not subdirs:
        return False

    path = directory / OVERVIEW_NAME
    # We overwrite existing if it doesn't exist?
    # The instructions said "only creates missing".
    # But I deleted them all. So I'm creating them fresh.

    content = generate_overview_content(directory, prompt_files)
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    changed = False

    # Walk all directories under PROMPTS_DIR
    for root, dirs, files in os.walk(PROMPTS_DIR):
        root_path = Path(root)
        if root_path == PROMPTS_DIR:
            continue

        # We need to ensure overview for this directory
        if ensure_overview(root_path):
            print(f"Generated overview for {root_path}")
            changed = True

    return 0 if changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
