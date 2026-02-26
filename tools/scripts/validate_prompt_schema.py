#!/usr/bin/env python3
"""
Validate Prompt Schema & Generate JSON Schema

This script validates that prompt YAML files adhere to the strict Pydantic schema
defined in `PromptSchema`. It ensures that all required fields are present and
correctly typed.

It can also generate a JSON Schema for use in IDEs (like VS Code) to provide
intellisense and validation while editing `.prompt.yaml` files.

Usage:
    # Validate all prompts
    python3 tools/scripts/validate_prompt_schema.py

    # Validate specific file(s)
    python3 tools/scripts/validate_prompt_schema.py path/to/file.prompt.yaml

    # Validate with strict checks (e.g., warns on empty testData)
    python3 tools/scripts/validate_prompt_schema.py --strict

    # Generate JSON Schema for IDEs
    python3 tools/scripts/validate_prompt_schema.py --json-schema > docs/schemas/prompt.schema.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, List, Optional

from pydantic import BaseModel, ValidationError, Field

# Add current directory to path to allow importing utils
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

try:
    from utils import ROOT, iter_prompt_files, load_yaml
except ImportError:
    # Fallback if running from root
    sys.path.append(str(current_dir.parent.parent))
    from tools.scripts.utils import ROOT, iter_prompt_files, load_yaml


# ---------------------------------------------------------------------------
# Schema Definitions
# ---------------------------------------------------------------------------

class Message(BaseModel):
    role: Optional[str] = Field(None, description="The role of the message sender (e.g., 'system', 'user', 'assistant').")
    content: str = Field(..., description="The content of the message.")

class PromptSchema(BaseModel):
    name: str = Field(..., description="A short, descriptive name for the prompt.")
    description: str = Field(..., description="A detailed description of the prompt's purpose.")
    model: str = Field(..., description="The ID of the LLM model to use.")
    messages: List[Message] = Field(..., description="The sequence of messages.")
    testData: Optional[List[Any]] = Field(None, description="List of test cases.")
    evaluators: Optional[List[Any]] = Field(None, description="List of evaluators.")


def validate_file(file_path: Path, strict: bool = False) -> bool:
    """Validate a single prompt file. Returns True if valid."""
    print(f"Validating {file_path}...")
    content = load_yaml(file_path)
    if content is None:
        print(f"Error: Could not load {file_path}")
        return False

    try:
        PromptSchema(**content)
    except ValidationError as e:
        print(f"Validation error in {file_path}:")
        for error in e.errors():
            print(f"  - {error['loc']}: {error['msg']}")
        return False

    if strict:
        if not content.get('testData'):
            print(f"Warning: {file_path} has no testData")
        if not content.get('evaluators'):
            print(f"Warning: {file_path} has no evaluators")

    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate prompt YAML files.")
    parser.add_argument("files", nargs="*", help="Specific files to validate (optional)")
    parser.add_argument("--strict", action="store_true", help="Enable strict mode warnings")
    parser.add_argument("--json-schema", action="store_true", help="Output JSON Schema")

    args = parser.parse_args()

    if args.json_schema:
        print(json.dumps(PromptSchema.model_json_schema(), indent=2))
        return 0

    ok = True

    if args.files:
        # Validate specific files
        for f in args.files:
            if not validate_file(Path(f), strict=args.strict):
                ok = False
    else:
        # Validate all files in repo
        for file_path in iter_prompt_files(ROOT):
            if not validate_file(file_path, strict=args.strict):
                ok = False

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
