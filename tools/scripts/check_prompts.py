#!/usr/bin/env python3
"""
Repository Checks for Prompt Files

## What is this?
This script performs structural and naming validation on the `prompts/` and `workflows/`
directories to ensure repository consistency. It enforces that prompts follow required
naming patterns and that every directory has documentation.

## Why use it?
- **Prevents Documentation Debt:** Ensures every prompt directory contains an `overview.md` file.
- **Enforces Consistency:** Validates that meta-prompts follow the `L<num>_` naming pattern.
- **Catches Stray Files:** Identifies unrecognized files that don't belong in prompt directories.

> [!NOTE]
> This script is primarily focused on file structure and names. For deep YAML schema validation,
> use `validate_prompt_schema.py`.

## How to use it?

### Usage Example
Run this script from the root of the repository:

```bash
python3 tools/scripts/check_prompts.py
```

If successful, it exits with code 0. If it finds missing `overview.md` files or invalid names,
it prints the errors to stdout and exits with code 1.
"""

from __future__ import annotations

import re
from pathlib import Path

try:
    from utils import PROMPTS_DIR, WORKFLOWS_DIR, load_yaml, iter_prompt_files, iter_workflow_files, OVERVIEW_NAME
except ImportError:
    # Allow running from root or scripts dir
    import sys
    sys.path.append(str(Path(__file__).parent))
    from utils import PROMPTS_DIR, WORKFLOWS_DIR, load_yaml, iter_prompt_files, iter_workflow_files, OVERVIEW_NAME


NAMING_RULES = {
    "meta": re.compile(r"^L\d+_.*\.prompt\.ya?ml$", re.IGNORECASE),
}


def check_overview(directory: Path) -> bool:
    if not (directory / OVERVIEW_NAME).exists():
        print(f"Missing {OVERVIEW_NAME} in {directory}")
        return False
    return True


def check_directory_contents(directory: Path) -> bool:
    """Check for unrecognized files in the directory."""
    ok = True
    for file in directory.iterdir():
        if not file.is_file() or file.name.startswith('.'):
            continue
        name = file.name
        if name.lower() in {OVERVIEW_NAME, "readme.md"} or name.lower().endswith(".workflow.md"):
            continue

        lower_name = name.lower()
        is_yaml = (
            lower_name.endswith(".prompt.yaml")
            or lower_name.endswith(".prompt.yml")
            or lower_name.endswith(".workflow.yaml")
            or lower_name.endswith(".workflow.yml")
        )

        if not is_yaml:
            print(f"{file} is not a recognised prompt or workflow file")
            ok = False
            continue

    return ok


def check_prompt_file(file: Path) -> bool:
    """Validate a single prompt file."""
    ok = True
    if not load_yaml(file):
        print(f"Failed to parse {file}")
        ok = False

    directory = file.parent
    if directory.name in NAMING_RULES and not file.name.endswith(".workflow.yaml") and not file.name.endswith(".workflow.yml"):
        pattern = NAMING_RULES[directory.name]
        if not pattern.match(file.name):
            print(f"{file} does not match required pattern for {directory.name}")
            ok = False

    return ok


def main() -> int:
    success = True

    # 1. Identify all directories containing prompts (recursively)
    #    and check all prompt files.
    dirs_to_check = set()

    for prompt_file in iter_prompt_files(PROMPTS_DIR):
        if not check_prompt_file(prompt_file):
            success = False

        # Collect directory and all parents up to PROMPTS_DIR
        path = prompt_file.parent
        while path != PROMPTS_DIR:
             dirs_to_check.add(path)
             if path == path.parent: # Safety break
                 break
             path = path.parent

    for workflow_file in iter_workflow_files(WORKFLOWS_DIR):
        if not check_prompt_file(workflow_file):
            success = False

        # Collect directory and all parents up to WORKFLOWS_DIR
        path = workflow_file.parent
        while path != WORKFLOWS_DIR:
             dirs_to_check.add(path)
             if path == path.parent: # Safety break
                 break
             path = path.parent

    # 2. Check each directory for overview and stray files
    for directory in dirs_to_check:
        if not check_overview(directory):
            success = False
        if not check_directory_contents(directory):
            success = False

    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
