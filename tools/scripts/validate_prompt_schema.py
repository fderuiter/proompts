#!/usr/bin/env python3
"""Validate required fields in prompt YAML files."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, List, Any

import yaml
from pydantic import BaseModel, ValidationError, field_validator

ROOT = Path(__file__).resolve().parents[2]


class Message(BaseModel):
    role: str
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

    @field_validator('messages')
    @classmethod
    def check_messages_length(cls, v: List[Message]) -> List[Message]:
        if len(v) < 2:
            raise ValueError('messages list must contain at least two entries')
        return v


def iter_prompt_files() -> Iterable[Path]:
    """Yield all prompt files in the repository."""
    patterns = ("*.prompt.yaml", "*.prompt.yml")
    for pattern in patterns:
        for path in ROOT.rglob(pattern):
            if path.is_file():
                yield path


def validate_file(file_path: Path) -> bool:
    """Validate a single prompt file and report errors."""
    try:
        content = yaml.safe_load(file_path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover
        print(f"Failed to parse {file_path}: {exc}")
        return False

    if content is None:
        print(f"File is empty: {file_path}")
        return False

    try:
        PromptSchema(**content)
    except ValidationError as e:
        print(f"Validation error in {file_path}:")
        for error in e.errors():
            loc = " -> ".join(map(str, error['loc']))
            msg = error['msg']
            print(f"  - {loc}: {msg}")
        return False

    return True


def main() -> int:
    ok = True
    for file_path in iter_prompt_files():
        if not validate_file(file_path):
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
