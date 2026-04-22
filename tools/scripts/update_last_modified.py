#!/usr/bin/env python3
"""
update_last_modified.py

WHAT:
This script updates the `last_modified` metadata field in prompt YAML files to the current UTC time.
If the field is missing, it injects it at the top of the file (or immediately after the `name` field).

WHY:
It ensures that prompt versions and modification timestamps are tracked automatically. This is especially
useful in CI/CD pipelines to guarantee that documentation and databases accurately reflect the latest
updates to a prompt without requiring developers to manually edit timestamps.

HOW:
Usage:
    # Update specific files
    python3 tools/scripts/update_last_modified.py prompts/my_prompt.prompt.yaml

    # Dry-run check (returns non-zero if updates are needed, but modifies nothing)
    python3 tools/scripts/update_last_modified.py prompts/my_prompt.prompt.yaml --check
"""

import argparse
from datetime import datetime, timezone
from pathlib import Path
import sys

try:
    from utils import ROOT
except ImportError:
    sys.path.append(str(Path(__file__).parent))
    from utils import ROOT

def update_file(file_path: Path, check: bool = False) -> bool:
    """Update last_modified field in the file.
       Returns True if file was changed (or would be changed), False otherwise.
    """
    try:
        content_text = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

    lines = content_text.splitlines()
    new_lines = []
    found = False
    now_iso = datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')

    modified = False

    # Check if last_modified already exists
    for i, line in enumerate(lines):
        if line.strip().startswith('last_modified:'):
            # We found it. We update it.
            # But wait, if the file is passed here, it means it is staged.
            # So we should update the timestamp.
            indent = line[:line.find('last_modified:')]
            new_line = f"{indent}last_modified: {now_iso}"
            if new_line != line:
                lines[i] = new_line
                modified = True
            found = True
            break

    if not found:
        # Add after `name:`
        final_lines = []
        name_found = False
        for line in lines:
            final_lines.append(line)
            if not name_found and line.strip().startswith('name:'):
                indent = line[:line.find('name:')]
                final_lines.append(f"{indent}last_modified: {now_iso}")
                modified = True
                name_found = True

        if not name_found:
             # If no name, add at top (after ---)
             if len(final_lines) > 0 and final_lines[0].strip() == '---':
                 final_lines.insert(1, f"last_modified: {now_iso}")
                 modified = True
             else:
                 final_lines.insert(0, f"last_modified: {now_iso}")
                 modified = True
        lines = final_lines

    if modified:
        if not check:
            file_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return True
    return False

def main():
    parser = argparse.ArgumentParser(description="Update last_modified field in prompts")
    parser.add_argument("files", nargs='*', help="Files to update")
    parser.add_argument("--check", action="store_true", help="Only check if files need update")
    args = parser.parse_args()

    if not args.files:
        return 0

    ret = 0
    for f in args.files:
        path = Path(f)
        if path.is_file() and (path.suffix == '.yaml' or path.suffix == '.yml'):
             if update_file(path, check=args.check):
                 print(f"Updated last_modified in {path}")
                 ret = 1

    return ret

if __name__ == "__main__":
    main()
