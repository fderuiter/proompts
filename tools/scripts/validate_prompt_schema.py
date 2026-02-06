#!/usr/bin/env python3
"""Validate required fields in prompt YAML files."""

from __future__ import annotations

from pathlib import Path
from typing import Any, List, Optional

from pydantic import BaseModel, ValidationError, field_validator

try:
    from utils import ROOT, iter_prompt_files, load_yaml
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).parent))
    from utils import ROOT, iter_prompt_files, load_yaml


class Message(BaseModel):
    role: Optional[str] = None
    content: str


class ModelParameters(BaseModel):
    temperature: float


class PromptSchema(BaseModel):
    name: str
    description: str
    model: str
    modelParameters: ModelParameters
    messages: List[Message]
    testData: List[Any]
    evaluators: List[Any]

    @field_validator("messages")
    @classmethod
    def check_messages_length(cls, v: List[Message]) -> List[Message]:
        if len(v) < 2:
            raise ValueError("messages list must have at least 2 items")
        return v


def validate_file(file_path: Path) -> bool:
    """Validate a single prompt file and report missing keys."""
    content = load_yaml(file_path)
    # If parsing failed, load_yaml prints an error and returns {}.
    # We continue to check schema, which will fail if content is empty.

    try:
        PromptSchema(**content)
    except ValidationError as e:
        print(f"Validation error in {file_path}:\n{e}")
        return False

    return True


def main() -> int:
    ok = True
    for file_path in iter_prompt_files(ROOT):
        if not validate_file(file_path):
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
