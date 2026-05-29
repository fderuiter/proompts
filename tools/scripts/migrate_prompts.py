#!/usr/bin/env python3
"""
Migrate Prompts - Schema Evolution Script

## What is this?
This script migrates older prompt YAML files to the latest schema standard by
automatically inserting missing structural fields such as `version` and `variables`.

## Why use it?
- **Reduces Cognitive Load:** Eliminates the need to manually update legacy prompts
  when new schema requirements are introduced.
- **Maintains Consistency:** Ensures all prompts follow the strict Pydantic schema
  rules defined in `validate_prompt_schema.py`.

> [!NOTE]
> This script performs structural updates only. For `variables`, it extracts variable
> names from template strings (e.g., `{{var_name}}`) and adds them to the `variables`
> block with a placeholder description (`TODO`). Use `enrich_prompts.py` afterwards
> to auto-generate those descriptions.

## How to use it?

### Usage Examples

1. **Dry Run** (Preview changes without modifying files):
   ```bash
   python3 tools/scripts/migrate_prompts.py --dry-run
   ```

2. **Migrate All Prompts**:
   ```bash
   python3 tools/scripts/migrate_prompts.py
   ```
"""

from __future__ import annotations

from pathlib import Path

try:
    from promptops.utils import ROOT, extract_template_vars, iter_prompt_files, load_yaml
    from promptops.persistence import update_yaml
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).parent.parent.parent))
    from promptops.utils import ROOT, extract_template_vars, iter_prompt_files, load_yaml
    from promptops.persistence import update_yaml

import yaml


# Configure yaml to use block scalars for multiline strings
def str_presenter(dumper, data):
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(str, str_presenter)


def migrate_file(file_path: Path, dry_run: bool = False) -> bool:
    """Add version and variables stubs to a prompt file if missing.

    Returns True if the file was modified.
    """
    # Quick check without locking to see if we need modifications
    content = load_yaml(file_path)
    if not content:
        print(f"  SKIP (empty/unparseable): {file_path}")
        return False

    needs_version = "version" not in content
    needs_variables = "variables" not in content

    if not needs_version and not needs_variables:
        print(f"  OK (already migrated): {file_path}")
        return False

    if dry_run:
        print(f"  DRY-RUN would update: {file_path}")
        return True

    # Perform lossless update
    with update_yaml(file_path) as data:
        if "version" not in data:
            data["version"] = "0.1.0"
        
        if "variables" not in data:
            vars_in_template = extract_template_vars(data)
            if vars_in_template:
                data["variables"] = [
                    {"name": v, "description": "TODO", "required": True}
                    for v in vars_in_template
                ]
            else:
                data["variables"] = []

    print(f"  UPDATED: {file_path}")
    return True


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description="Migrate prompt files to new schema")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would change without writing files")
    args = parser.parse_args()

    updated = 0
    total = 0
    for file_path in iter_prompt_files(ROOT):
        total += 1
        if migrate_file(file_path, dry_run=args.dry_run):
            updated += 1

    print(f"\n{'DRY-RUN: ' if args.dry_run else ''}Processed {total} files, "
          f"{updated} updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
