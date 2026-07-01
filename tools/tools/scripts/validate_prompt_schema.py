#!/usr/bin/env python3
"""
Validate Prompt Schema & Generate JSON Schema
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from promptops.validation import PromptSchema, validate_prompts
from promptops.utils import PROMPTS_DIR, WORKFLOWS_DIR


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate prompt YAML files or generate JSON Schema.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Enable strict mode with warnings for empty testData/evaluators"
    )
    parser.add_argument(
        "--json-schema",
        action="store_true",
        help="Output the JSON Schema for the PromptSchema to stdout and exit."
    )
    args = parser.parse_args()

    if args.json_schema:
        print(json.dumps(PromptSchema.model_json_schema(), indent=2))
        return 0

    success_prompts = validate_prompts(str(PROMPTS_DIR), strict=args.strict)
    success_workflows = validate_prompts(str(WORKFLOWS_DIR), strict=args.strict)
    return 0 if (success_prompts and success_workflows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
