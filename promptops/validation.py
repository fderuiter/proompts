import os
import re
from enum import Enum
from pathlib import Path
from typing import Any, List, Optional, Dict

from pydantic import BaseModel, ValidationError, field_validator, model_validator, Field
from promptops.utils import load_yaml, iter_prompt_files

VAR_PATTERN = re.compile(r'\{\{([^}]+)\}\}')

class ComplexityLevel(str, Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

class Message(BaseModel):
    role: Optional[str] = Field(None)
    content: str = Field(...)

class ModelParameters(BaseModel):
    temperature: float = Field(...)
    max_tokens: Optional[int] = Field(None)
    top_p: Optional[float] = Field(None)
    frequency_penalty: Optional[float] = Field(None)
    presence_penalty: Optional[float] = Field(None)

class InputVariable(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    required: bool = Field(True)
    default: Optional[Any] = Field(None)

class PromptMetadata(BaseModel):
    domain: str = Field(...)
    complexity: ComplexityLevel = Field(...)
    tags: List[str] = Field([])
    requires_context: bool = Field(False)

class PromptSchema(BaseModel):
    name: str = Field(...)
    version: str = Field("0.1.0")
    description: str = Field(...)
    metadata: Optional[PromptMetadata] = Field(None)
    variables: List[InputVariable] = Field([])
    model: str = Field(...)
    safety_opt_out: bool = Field(False)
    modelParameters: ModelParameters = Field(...)
    messages: List[Message] = Field(...)
    testData: List[Any] = Field(...)
    evaluators: List[Any] = Field(...)
    output_schema: Optional[Dict[str, Any]] = Field(None)
    last_modified: Optional[str] = Field(None)

    @field_validator("evaluators")
    @classmethod
    def check_evaluators_logic(cls, v: List[Any]) -> List[Any]:
        if v is None:
            return v
        for evaluator in v:
            if not isinstance(evaluator, dict):
                continue
            valid_keys = {"python", "rule", "regex", "model", "type", "string", "includes_all", "regex_match", "string_match", "string_contains", "evaluator", "description"}
            if not any(k in evaluator for k in valid_keys):
                raise ValueError(f"Evaluator '{evaluator.get('name', 'Unknown')}' must map to executable logic.")
        return v

    @field_validator("messages")
    @classmethod
    def check_messages_length(cls, v: List[Message]) -> List[Message]:
        if len(v) < 2:
            raise ValueError("messages list must have at least 2 items")
        return v

    @model_validator(mode='after')
    def check_variables_match_content(self):
        found_vars: set[str] = set()
        invalid_vars: set[str] = set()
        
        for msg in self.messages:
            for match in VAR_PATTERN.findall(msg.content):
                valid_match = re.match(r'^\s*([a-zA-Z0-9_.-]+)\s*$', match)
                if valid_match:
                    found_vars.add(valid_match.group(1))
                else:
                    invalid_vars.add(match)

        if invalid_vars:
            raise ValueError(f"Migration Required: Variables contain invalid characters: {invalid_vars}")

        defined_vars = {v.name for v in self.variables}
        unused = defined_vars - found_vars
        if unused:
            print(f"Warning: Variables defined but not used in prompt: {unused}")

        undefined = found_vars - defined_vars
        if undefined:
            raise ValueError(f"Variables used in messages but NOT defined in 'variables' section: {undefined}")

        return self

def validate_prompts(directory: str, strict: bool = False) -> bool:
    ok = True
    seen_names = {}
    dir_path = os.environ.get('PROMPTOPS_REGISTRY', directory)
    
    for file_path in iter_prompt_files(dir_path):
        content = load_yaml(str(file_path))
        if not content:
            ok = False
            continue
            
        try:
            PromptSchema(**content)
        except ValidationError as e:
            print(f"Validation error in {file_path}:\n{e}")
            ok = False
            continue

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

        name = content.get('name')
        if name:
            if name in seen_names:
                print(f"Error: Duplicate name '{name}' found in:\n  - {seen_names[name]}\n  - {file_path}")
                ok = False
            else:
                seen_names[name] = str(file_path)

    return ok
