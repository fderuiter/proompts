#!/usr/bin/env python3
"""Wrapper script for repository-level prompt checks."""

import os
import sys
from pathlib import Path

# Add the tools/scripts directory to the path so we can import everything correctly
current_dir = Path(__file__).parent.resolve()
tools_scripts_dir = current_dir.parent / "tools" / "scripts"
sys.path.insert(0, str(tools_scripts_dir))

try:
    from check_prompts import main
except ImportError as e:
    print(f"Error: Could not import check_prompts from {tools_scripts_dir}")
    print(f"Details: {e}")
    sys.exit(1)

if __name__ == "__main__":
    sys.exit(main())
