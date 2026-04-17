#!/usr/bin/env python3
"""
Test All Script - The Master Runner

## What is this?
This is the master validation script that orchestrates the execution of all
repository validation checks in sequence. It ensures the repository remains
healthy, documentation is up-to-date, and prompt schemas are valid.

## Why use it?
- **Reduces Cognitive Load:** Instead of running 7 different maintenance scripts
  manually, this script executes them all in the correct order.
- **Prevents CI Failures:** Running this locally before committing helps catch
  schema violations, broken links, and formatting issues early.
- **Ensures Documentation Fidelity:** It runs scripts that rebuild the `docs/`
  indexes based on current YAML content.

## How to use it?
Run this script from the root of the repository before committing changes.

```bash
python3 tools/scripts/test_all.py
```
"""

from __future__ import annotations

import subprocess
import sys

from check_prompts import main as check_prompts_main
from update_docs_index import run_update as update_docs_index_run
from validate_prompt_schema import main as validate_prompt_schema_main


def run_command(command: list[str]) -> int:
    """Run a command and return its exit code."""
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running {' '.join(command)}:")
        print(result.stdout)
        print(result.stderr)
    return result.returncode


def main() -> int:
    """Run all checks and return final status."""
    checks = {
        "cleanup_mac_files": lambda: run_command(["find", ".", "-name", "._*", "-delete"]),
        "check_prompts": check_prompts_main,
        "validate_prompt_schema": validate_prompt_schema_main,
        "update_docs_index": lambda: update_docs_index_run(check=True),
        "generate_docs": lambda: run_command(["python3", "tools/scripts/generate_docs.py", "--check"]),
        "check_broken_links": lambda: run_command(["python3", "tools/scripts/check_broken_links.py"]),
        "yamllint": lambda: run_command(["yamllint", "."]),
    }

    failed = []
    for name, check_func in checks.items():
        print(f"Running {name}...")
        if check_func() != 0:
            print(f"{name} failed.")
            failed.append(name)
        else:
            print(f"{name} passed.")

    if failed:
        print(f"\nThe following checks failed: {', '.join(failed)}")
        return 1

    print("\nAll checks passed!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
