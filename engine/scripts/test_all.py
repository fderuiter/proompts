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
python3 engine/scripts/test_all.py
```
"""

from __future__ import annotations

import subprocess
import sys

from check_prompts import main as check_prompts_main
from update_docs_index import run_update as update_docs_index_run
from validate_prompt_schema import main as validate_prompt_schema_main

MAX_DISPLAYED_TRACKED_FILES = 20
STATIC_TOP_LEVEL_DOCS = {
    "docs/BEST_PRACTICES.md",
    "docs/QUICKSTART.md",
    "docs/USAGE.md",
    "docs/claude_prompting_guide.md",
    "docs/google_prompting_guide.md",
    "docs/gpt_5_2_prompting_guide.md",
    "docs/json_to_yaml_migration.md",
    "docs/overview.md",
    "docs/system_architecture.md",
    "docs/workflow_guide.md",
    "docs/workflows_usage.md",
}


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
    generated_paths = ["docs"]
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
    generated_tracked = []
    for path in tracked:
        if path.startswith("docs/prompts/") or path.startswith("docs/workflows/"):
            generated_tracked.append(path)
            continue
        if path in {"docs/index.md", "docs/table-of-contents.md"}:
            generated_tracked.append(path)
            continue
        if is_top_level_docs_markdown_file(path) and path not in STATIC_TOP_LEVEL_DOCS:
            generated_tracked.append(path)

    if generated_tracked:
        print("Generated docs must not be committed to git:")
        for path in generated_tracked[:MAX_DISPLAYED_TRACKED_FILES]:
            print(f" - {path}")
        if len(generated_tracked) > MAX_DISPLAYED_TRACKED_FILES:
            print(f" ... and {len(generated_tracked) - MAX_DISPLAYED_TRACKED_FILES} more")
        return 1

    return 0


def is_top_level_docs_markdown_file(path: str) -> bool:
    """Return True when the path points to a Markdown file directly under docs/."""
    return path.startswith("docs/") and path.count("/") == 1 and path.endswith(".md")


def main() -> int:
    """Run all checks and return final status."""
    checks = {
        "cleanup_mac_files": lambda: run_command(["find", ".", "-name", "._*", "-delete"]),
        "enforce_generated_docs_untracked": ensure_generated_docs_not_tracked,
        "check_prompts": check_prompts_main,
        "validate_prompt_schema": validate_prompt_schema_main,
        "generate_compliance_manifest": lambda: run_command(["python3", "engine/scripts/governance_manifest_generator.py"]),
        "generate_overviews": lambda: run_command(["python3", "engine/scripts/generate_overviews.py"]),
        # Docs are build artifacts now, so we generate them before running integrity checks.
        "update_docs_index": lambda: run_command(["python3", "engine/scripts/update_docs_index.py"]),
        "update_docs_index_check": lambda: update_docs_index_run(check=True),
        "generate_docs": lambda: run_command(["python3", "engine/scripts/generate_docs.py"]),
        "generate_docs_check": lambda: run_command(["python3", "engine/scripts/generate_docs.py", "--check"]),
        "check_broken_links": lambda: run_command(["python3", "engine/scripts/check_broken_links.py"]),
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
