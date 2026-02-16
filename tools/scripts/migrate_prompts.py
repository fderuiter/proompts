#!/usr/bin/env python3
"""Migrate existing prompt YAML files to include version and variables fields."""

from __future__ import annotations

import re
from pathlib import Path

try:
    from utils import ROOT, iter_prompt_files, load_yaml, dump_yaml_str
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).parent))
    from utils import ROOT, iter_prompt_files, load_yaml, dump_yaml_str

import yaml


def extract_template_vars(content: dict) -> list[str]:
    """Extract all {{var}} patterns from messages."""
    found: set[str] = set()
    for msg in content.get("messages", []):
        text = msg.get("content", "")
        found.update(re.findall(r'\{\{([^}]+)\}\}', text))
    return sorted(found)


def migrate_file(file_path: Path, dry_run: bool = False, force: bool = False) -> bool:
    """Add version and variables stubs to a prompt file if missing.

    Returns True if the file was modified.
    """
    content = load_yaml(file_path)
    if not content:
        print(f"  SKIP (empty/unparseable): {file_path}")
        return False

    modified = False

    # Add version if missing
    if "version" not in content:
        content["version"] = "0.1.0"
        modified = True

    # Add variables stubs if missing
    if "variables" not in content:
        vars_in_template = extract_template_vars(content)
        if vars_in_template:
            content["variables"] = [
                {"name": v, "description": "TODO", "required": True}
                for v in vars_in_template
            ]
            modified = True
        else:
            content["variables"] = []
            modified = True

    if force:
        modified = True

    if not modified:
        print(f"  OK (already migrated): {file_path}")
        return False

    if dry_run:
        print(f"  DRY-RUN would update: {file_path}")
        return True

    # Write back — use default_flow_style=False for readable YAML
    yaml_text = dump_yaml_str(content)
    file_path.write_text("---\n" + yaml_text, encoding="utf-8")
    print(f"  UPDATED: {file_path}")
    return True


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Migrate prompt files to new schema")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would change without writing files")
    parser.add_argument("--force", action="store_true",
                        help="Force update even if no changes detected (useful for reformatting)")
    args = parser.parse_args()

    updated = 0
    total = 0
    for file_path in iter_prompt_files(ROOT):
        total += 1
        if migrate_file(file_path, dry_run=args.dry_run, force=args.force):
            updated += 1

    print(f"\n{'DRY-RUN: ' if args.dry_run else ''}Processed {total} files, "
          f"{updated} updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
