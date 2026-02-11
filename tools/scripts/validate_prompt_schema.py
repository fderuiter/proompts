#!/usr/bin/env python3
"""Validate required fields in prompt YAML files."""

from __future__ import annotations

import argparse
import re
from enum import Enum
from pathlib import Path
from typing import Any, List, Optional

from pydantic import BaseModel, ValidationError, field_validator, model_validator

try:
    from utils import ROOT, iter_prompt_files, load_yaml
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).parent))
    from utils import ROOT, iter_prompt_files, load_yaml


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class ComplexityLevel(str, Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'


# ---------------------------------------------------------------------------
# Sub-models
# ---------------------------------------------------------------------------

class Message(BaseModel):
    role: Optional[str] = None
    content: str


class ModelParameters(BaseModel):
    temperature: float


class InputVariable(BaseModel):
    name: str
    description: str
    required: bool = True
    default: Optional[Any] = None


class PromptMetadata(BaseModel):
    domain: str
    complexity: ComplexityLevel
    tags: List[str] = []
    requires_context: bool = False


# ---------------------------------------------------------------------------
# Main schema
# ---------------------------------------------------------------------------

class PromptSchema(BaseModel):
    name: str
    version: str = "0.1.0"
    description: str
    metadata: Optional[PromptMetadata] = None
    variables: List[InputVariable] = []
    model: str
    modelParameters: ModelParameters
    messages: List[Message]
    testData: List[Any]
    evaluators: List[Any]
    last_modified: Optional[str] = None

    @field_validator("messages")
    @classmethod
    def check_messages_length(cls, v: List[Message]) -> List[Message]:
        if len(v) < 2:
            raise ValueError("messages list must have at least 2 items")
        return v

    @model_validator(mode='after')
    def check_variables_match_content(self):
        """Cross-check {{var}} usage in messages against defined variables."""
        found_vars: set[str] = set()
        for msg in self.messages:
            found_vars.update(re.findall(r'\{\{([^}]+)\}\}', msg.content))

        defined_vars = {v.name for v in self.variables}

        # Warn about defined-but-unused variables
        unused = defined_vars - found_vars
        if unused:
            print(f"Warning: Variables defined but not used in prompt: {unused}")

        # Error on used-but-undefined variables
        undefined = found_vars - defined_vars
        if undefined:
            raise ValueError(
                f"Variables used in messages but NOT defined in "
                f"'variables' section: {undefined}"
            )

        return self


def validate_file(file_path: Path, strict: bool = False) -> Optional[dict]:
    """Validate a single prompt file and report missing keys.
       Returns content dict if valid, None if invalid.
    """
    content = load_yaml(file_path)
    # If parsing failed, load_yaml prints an error and returns {}.
    # We continue to check schema, which will fail if content is empty.

    try:
        PromptSchema(**content)
    except ValidationError as e:
        print(f"Validation error in {file_path}:\n{e}")
        return None

    # In strict mode, warn about empty testData or evaluators (best practice)
    if strict:
        issues = []
        if not content.get('testData') or len(content.get('testData', [])) == 0:
            issues.append("no testData")
        elif len(content.get('testData', [])) == 1:
            issues.append("only 1 test case")
        
        if not content.get('evaluators') or len(content.get('evaluators', [])) == 0:
            issues.append("no evaluators")
        
        if issues:
            print(f"Warning: {file_path} has {', '.join(issues)}")

    return content


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate prompt YAML files")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Enable strict mode with warnings for empty testData/evaluators"
    )
    args = parser.parse_args()

    ok = True
    seen_names = {}  # name -> file_path

    for file_path in iter_prompt_files(ROOT):
        content = validate_file(file_path, strict=args.strict)
        if content is None:
            ok = False
            continue

        name = content.get('name')
        if name:
            if name in seen_names:
                print(f"Error: Duplicate name '{name}' found in:\n  - {seen_names[name]}\n  - {file_path}")
                ok = False
            else:
                seen_names[name] = file_path

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
