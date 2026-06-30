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
   python3 tools/tools/scripts/migrate_prompts.py --dry-run
   ```

2. **Migrate All Prompts**:
   ```bash
   python3 tools/tools/scripts/migrate_prompts.py
   ```
"""

from __future__ import annotations

from pathlib import Path

from promptops.utils import ROOT, extract_template_vars, iter_prompt_files, load_yaml

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
        try:
            vars_in_template = extract_template_vars(content)
        except ValueError as e:
            print(f"  SKIP (invalid syntax): {file_path}\n  {e}")
            return False
            
        if vars_in_template:
            content["variables"] = [
                {"name": v, "description": "TODO", "required": True}
                for v in vars_in_template
            ]
            modified = True
        else:
            content["variables"] = []
            modified = True

    # Ensure model and modelParameters exist
    if "model" not in content:
        content["model"] = "gpt-4o-mini"
        modified = True
    if "modelParameters" not in content:
        content["modelParameters"] = {"temperature": 0.7}
        modified = True

    # Add testData and evaluators stubs if missing
    if "testData" not in content:
        content["testData"] = []
        modified = True
    if "evaluators" not in content:
        content["evaluators"] = []
        modified = True

    # Add 'skill' tag if missing and in target pilots
    target_pilots = ["google_jules", "cdisc_compliance_workflow"]
    if any(pilot in str(file_path) for pilot in target_pilots):
        metadata = content.get("metadata", {})
        if not isinstance(metadata, dict):
             metadata = {}
        tags = metadata.get("tags", [])
        if not isinstance(tags, list):
             tags = []
        if "skill" not in tags:
            tags.append("skill")
            metadata["tags"] = tags
            content["metadata"] = metadata
            modified = True

    if file_path.suffix in ('.yaml', '.yml'):
        modified = True

    if not modified:
        print(f"  OK (already migrated): {file_path}")
        return False

    if dry_run:
        print(f"  DRY-RUN would update: {file_path}")
        return True

    try:
        from promptops.validation import PromptSchema
        PromptSchema(**content)
    except Exception as e:
        print(f"  SKIP (invalid schema or syntax after migration): {file_path}\n  {e}")
        return False

    # Remove messages from YAML content
    messages = content.pop("messages", [])
    md_lines = []
    for msg in messages:
        role = msg.get("role", "system")
        md_content = msg.get("content", "")
        if isinstance(md_content, list):
            md_content = " ".join([str(c) for c in md_content])
        elif not md_content and msg.get("tool_calls"):
            md_content = str(msg.get("tool_calls"))
            
        md_content = md_content.strip()
        if role == "system":
            md_lines.append(f"## Purpose\n{md_content}\n")
        elif role == "user":
            md_lines.append(f"## Instructions\n{md_content}\n")
        else:
            md_lines.append(f"## {role.capitalize()}\n{md_content}\n")

    # Write back — use default_flow_style=False for readable YAML
    yaml_text = yaml.dump(content, default_flow_style=False, sort_keys=False,
                          allow_unicode=True, width=120)
    
    new_text = f"---\n{yaml_text}---\n\n" + "\n".join(md_lines)
    
    # Write to new .md file and remove old .yaml file if different
    new_file_path = file_path
    if file_path.suffix in ('.yaml', '.yml'):
        new_file_path = file_path.with_name(file_path.name.replace(".prompt.yaml", ".prompt.md").replace(".prompt.yml", ".prompt.md"))
        
    new_file_path.write_text(new_text, encoding="utf-8")
    if new_file_path != file_path:
        file_path.unlink()
        
    print(f"  UPDATED: {new_file_path}")
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
