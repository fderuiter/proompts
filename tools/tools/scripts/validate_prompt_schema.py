#!/usr/bin/env python3
"""
Validate Prompt Schema & Generate JSON Schema

## Table of Contents
- [What is this?](#what-is-this)
- [Why use it?](#why-use-it)
- [How to use it?](#how-to-use-it)
  - [Usage Examples](#usage-examples)
  - [Example Valid `testData` Section](#example-valid-testdata-section)

---

## What is this?
This script validates that prompt YAML files adhere to the strict Pydantic schema
defined in `PromptSchema`. It ensures that all required fields are present and
correctly typed.

It can also generate a JSON Schema for use in IDEs (like VS Code) to provide
intellisense and validation while editing `.prompt.yaml` files.

---

## Why use it?
- **Ensures consistency:** Validates that all prompts have required fields like `name`, `model`, and `messages`.
- **Prevents broken workflows:** Verifies that variables used in `messages` (e.g., `{{input}}`) are declared in the `variables` block.
- **Enables autocomplete:** Generates `prompt.schema.json`, which gives real-time feedback in modern IDEs.
- **Enforces quality (Strict mode):** Checks that prompts include meaningful `testData` and `evaluators`.

---

## How to use it?

### Usage Examples

> [!NOTE]
> Run this script from the root of the repository. It does not accept individual file paths as arguments; it validates all prompts in the repository.

1. **Basic Validation** (Checks all required schema fields):
   ```bash
   python3 tools/scripts/validate_prompt_schema.py
   ```

2. **Strict Validation** (Warns if `testData` or `evaluators` are empty):
   ```bash
   python3 tools/scripts/validate_prompt_schema.py --strict
   ```

3. **Generate JSON Schema** (Outputs schema for IDE intellisense):
   ```bash
   python3 tools/scripts/validate_prompt_schema.py --json-schema > docs/schemas/prompt.schema.json
   ```

### Example Valid `testData` Section
```yaml
testData:
  - inputs:
      user_input: "Hello world"
    expected: "Hello! How can I help you today?"
evaluators:
  - rule: "Output must contain 'Hello'"
```
"""

from __future__ import annotations

import argparse
import json
import re
from promptops.validation import PromptSchema
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
            issues.append("no evaluators (note: evaluator blocks are required for schema compliance but are bypassed during simulation)")
        
        if issues:
            print(f"Warning: {file_path} has {', '.join(issues)}")

    return content


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

    ok = True
    seen_names: dict[str, str] = {}  # name -> file_path

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
                seen_names[name] = str(file_path)

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
