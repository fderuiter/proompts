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
    from promptops.utils import ROOT
    from promptops.persistence import update_yaml
except ImportError:
    sys.path.append(str(Path(__file__).parent.parent.parent))
    from promptops.utils import ROOT
    from promptops.persistence import update_yaml

def update_file(file_path: Path, check: bool = False) -> bool:
    """Update last_modified field in the file.
       Returns True if file was changed (or would be changed), False otherwise.
    """
    now_iso = datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')

    if check:
        # Just check if it needs update
        try:
            from promptops.utils import load_yaml
            content = load_yaml(file_path)
            if content.get('last_modified') != now_iso:
                return True
            return False
        except Exception:
            return False

    modified = False
    with update_yaml(file_path) as data:
        if data.get('last_modified') != now_iso:
            if 'last_modified' not in data:
                # To insert after name, we can use insert on CommentedMap
                if hasattr(data, 'insert') and 'name' in data:
                    pos = list(data.keys()).index('name') + 1
                    data.insert(pos, 'last_modified', now_iso)
                else:
                    data['last_modified'] = now_iso
            else:
                data['last_modified'] = now_iso
            modified = True

    return modified

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
