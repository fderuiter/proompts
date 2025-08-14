#!/usr/bin/env python3
"""Validate required fields in prompt YAML files."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, Tuple, Union

import yaml

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS: Tuple[Tuple[Union[str, int], ...], ...] = (
    ("name",),
    ("description",),
    ("model",),
    ("modelParameters", "temperature"),
    ("messages", 0, "content"),
    ("messages", 1, "content"),
    ("testData",),
    ("evaluators",),
)


def iter_prompt_files() -> Iterable[Path]:
    """Yield all prompt files in the repository."""
    patterns = ("*.prompt.yaml", "*.prompt.yml")
    for pattern in patterns:
        for path in ROOT.rglob(pattern):
            if path.is_file():
                yield path


def has_path(data: object, path: Tuple[Union[str, int], ...]) -> bool:
    """Check if ``data`` has ``path`` nested keys/indexes."""
    try:
        for key in path:
            if isinstance(key, int):
                data = data[key]
            else:
                data = data[key]
    except (KeyError, IndexError, TypeError):
        return False
    return True


def validate_file(file_path: Path) -> bool:
    """Validate a single prompt file and report missing keys."""
    try:
        content = yaml.safe_load(file_path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - simple validation
        print(f"Failed to parse {file_path}: {exc}")
        return False

    missing = [".".join(map(str, p)) for p in REQUIRED_PATHS if not has_path(content, p)]
    if missing:
        print(f"{file_path}: missing {', '.join(missing)}")
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
