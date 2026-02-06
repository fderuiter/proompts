#!/usr/bin/env python3
"""Run all repository validation checks."""

from __future__ import annotations

import subprocess
import sys

from check_prompts import main as check_prompts_main
from update_docs_index import main as update_docs_index_main
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
        "check_prompts": check_prompts_main,
        "validate_prompt_schema": validate_prompt_schema_main,
        "update_docs_index": update_docs_index_main,
        "yamllint": lambda: run_command(["yamllint", "."]),
    }

    failed = []
    for name, check_func in checks.items():
        print(f"Running {name}...")
        if name == "update_docs_index":
            # This is a temporary workaround until the script is refactored
            # to not use argparse
            sys.argv = ["", "--check"]
            if check_func() != 0:
                print(f"{name} failed.")
                failed.append(name)
            else:
                print(f"{name} passed.")
            sys.argv = [""]
        elif check_func() != 0:
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
