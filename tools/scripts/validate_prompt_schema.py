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

    # Validate with strict checks (e.g., warns on empty testData)
    python3 tools/scripts/validate_prompt_schema.py --strict

    # Generate JSON Schema for IDEs
    python3 tools/scripts/validate_prompt_schema.py --json-schema > docs/schemas/prompt.schema.json
"""

from __future__ import annotations

import argparse
import json
import re
from enum import Enum
from pathlib import Path
from typing import Any, List, Optional

from pydantic import BaseModel, ValidationError, field_validator, model_validator, Field

try:
    from utils import ROOT, iter_prompt_files, load_yaml
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).parent))
    from utils import ROOT, iter_prompt_files, load_yaml


# ---------------------------------------------------------------------------
# Constants & Regex
# ---------------------------------------------------------------------------

VAR_PATTERN = re.compile(r'\{\{([^}]+)\}\}')


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
    role: Optional[str] = Field(None, description="The role of the message sender (e.g., 'system', 'user', 'assistant').")
    content: str = Field(..., description="The content of the message. Can contain Jinja2 variables like {{var}}.")


class ModelParameters(BaseModel):
    temperature: float = Field(..., description="The temperature parameter for the model, controlling randomness (0.0 to 1.0).")
    max_tokens: Optional[int] = Field(None, description="The maximum number of tokens to generate.")
    top_p: Optional[float] = Field(None, description="The nucleus sampling probability.")
    frequency_penalty: Optional[float] = Field(None, description="The frequency penalty parameter.")
    presence_penalty: Optional[float] = Field(None, description="The presence penalty parameter.")


class InputVariable(BaseModel):
    name: str = Field(..., description="The name of the variable as used in the template (e.g., 'input_text').")
    description: str = Field(..., description="A description of what this variable represents.")
    required: bool = Field(True, description="Whether this variable is mandatory.")
    default: Optional[Any] = Field(None, description="A default value for the variable if not provided.")


class PromptMetadata(BaseModel):
    domain: str = Field(..., description="The business domain (e.g., 'clinical', 'technical').")
    complexity: ComplexityLevel = Field(..., description="The complexity level of the prompt.")
    tags: List[str] = Field([], description="A list of tags for categorization and search.")
    requires_context: bool = Field(False, description="Whether this prompt requires external context or previous conversation history.")


# ---------------------------------------------------------------------------
# Main schema
# ---------------------------------------------------------------------------

class PromptSchema(BaseModel):
    """
    Schema definition for a Prompt file.
    """
    name: str = Field(..., description="A short, descriptive name for the prompt.")
    version: str = Field("0.1.0", description="Semantic version of the prompt.")
    description: str = Field(..., description="A detailed description of the prompt's purpose and usage.")
    metadata: Optional[PromptMetadata] = Field(None, description="Metadata for organization and categorization.")
    variables: List[InputVariable] = Field([], description="List of input variables used in the prompt template.")
    model: str = Field(..., description="The ID of the LLM model to use (e.g., 'gpt-4', 'claude-3-opus').")
    modelParameters: ModelParameters = Field(..., description="Configuration parameters for the model.")
    messages: List[Message] = Field(..., description="The sequence of messages that form the prompt.")
    testData: List[Any] = Field(..., description="List of test cases with inputs and expected outputs.")
    evaluators: List[Any] = Field(..., description="List of evaluators to validate the model's output.")
    last_modified: Optional[str] = Field(None, description="Timestamp of the last modification (ISO 8601).")

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
            found_vars.update(VAR_PATTERN.findall(msg.content))

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
