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


def ensure_generated_docs_not_tracked() -> int:
    """Ensure generated prompt/workflow docs are not committed to git."""
    generated_paths = [
        "docs/prompts",
        "docs/workflows",
        "docs/index.md",
        "docs/table-of-contents.md",
        "docs/architecture.md",
        "docs/business.md",
        "docs/clinical.md",
        "docs/communication.md",
        "docs/computational.md",
        "docs/google_jules.md",
        "docs/growth.md",
        "docs/languages.md",
        "docs/lifestyle.md",
        "docs/management.md",
        "docs/meta.md",
        "docs/regulatory.md",
        "docs/scientific.md",
        "docs/software_engineering.md",
        "docs/speculative.md",
        "docs/technical.md",
        "docs/testing.md",
        "docs/uncategorized.md",
        "docs/workflows.md",
    ]
    result = subprocess.run(
        ["git", "ls-files", *generated_paths],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print("Error checking tracked generated docs:")
        print(result.stdout)
        print(result.stderr)
        return result.returncode

    tracked = [line for line in result.stdout.splitlines() if line.strip()]
    if tracked:
        print("Generated docs must not be committed to git:")
        for path in tracked[:20]:
            print(f" - {path}")
        if len(tracked) > 20:
            print(f" ... and {len(tracked) - 20} more")
        return 1

    return 0


def main() -> int:
    """Run all checks and return final status."""
    checks = {
        "cleanup_mac_files": lambda: run_command(["find", ".", "-name", "._*", "-delete"]),
        "enforce_generated_docs_untracked": ensure_generated_docs_not_tracked,
        "check_prompts": check_prompts_main,
        "validate_prompt_schema": validate_prompt_schema_main,
        "generate_overviews": lambda: run_command(["python3", "tools/scripts/generate_overviews.py"]),
        "update_docs_index": lambda: update_docs_index_run(check=False),
        "generate_docs": lambda: run_command(["python3", "tools/scripts/generate_docs.py"]),
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
