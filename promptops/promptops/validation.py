import os
import re
from enum import Enum
from pathlib import Path
from typing import Any, List, Optional, Dict, Union

from pydantic import BaseModel, ValidationError, field_validator, model_validator, Field
from promptops.utils import load_yaml, iter_prompt_files, iter_workflow_files

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


class WorkflowInput(BaseModel):
    name: str = Field(...)
    description: Optional[str] = Field(None)

class WorkflowEdge(BaseModel):
    target: str = Field(...)
    condition: Optional[str] = Field(None)

class WorkflowStep(BaseModel):
    step_id: str = Field(...)
    prompt_file: str = Field(...)
    map_inputs: Dict[str, Any] = Field(...)
    next: Optional[Union[str, List[Union[str, WorkflowEdge]]]] = Field(None)

class WorkflowMetadata(BaseModel):
    domain: str = Field(...)
    topic: Optional[str] = Field(None)

class WorkflowSchema(BaseModel):
    name: str = Field(...)
    description: Optional[str] = Field(None)
    metadata: Optional[WorkflowMetadata] = Field(None)
    inputs: List[WorkflowInput] = Field([])
    steps: List[WorkflowStep] = Field(...)
    testData: Optional[List[Any]] = Field(None)

def analyze_workflow_dependencies(workflow_file: str, workflow_data: dict, root_dir: str) -> List[str]:
    issues = []
    try:
        wf = WorkflowSchema(**workflow_data)
    except ValidationError as e:
        return [f"Validation error: {e}"]

    # Dependency Graph (Circular & Forward reference detection)
    graph = {}
    step_ids = [step.step_id for step in wf.steps]
    
    for step_id in step_ids:
        graph[step_id] = []

    global_inputs = {inp.name for inp in wf.inputs}

    for i, step in enumerate(wf.steps):
        targets = []
        if step.next is not None:
            if isinstance(step.next, str):
                targets.append(step.next)
            elif isinstance(step.next, list):
                for edge in step.next:
                    if isinstance(edge, str):
                        targets.append(edge)
                    elif isinstance(edge, WorkflowEdge):
                        targets.append(edge.target)
                    elif isinstance(edge, dict):
                        targets.append(edge.get('target'))
        else:
            if i + 1 < len(wf.steps):
                targets.append(wf.steps[i + 1].step_id)
                
        for t in targets:
            if t not in step_ids:
                issues.append(f"Step '{step.step_id}' references undefined next step '{t}'.")
            else:
                graph[step.step_id].append(t)

        for var_name, template in step.map_inputs.items():
            if not isinstance(template, str):
                continue
            # Check inputs.*
            inputs_matches = re.findall(r'\{\{\s*inputs\.([^}\s]+)\s*\}\}', template)
            for inp_match in inputs_matches:
                if inp_match not in global_inputs:
                    issues.append(f"Step '{step.step_id}' mapping '{var_name}' refers to undefined global input '{inp_match}'.")

            # Check steps.*.output
            steps_matches = re.findall(r'\{\{\s*steps\.([^\.\s]+)\.(output|history)\s*\}\}', template)
            for step_match, prop in steps_matches:
                if step_match not in step_ids:
                    issues.append(f"Step '{step.step_id}' mapping '{var_name}' references undefined step '{step_match}'.")

    # Detect disconnected components
    if wf.steps:
        start_node = wf.steps[0].step_id
        visited = set()
        queue = [start_node]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                queue.extend(graph[node])
                
        unreachable = set(step_ids) - visited
        if unreachable:
            issues.append(f"Disconnected component(s) detected. The following steps are unreachable: {unreachable}")

    # Check Variable Contract
    for step in wf.steps:
        prompt_path = os.path.join(root_dir, step.prompt_file)
        if not os.path.exists(prompt_path):
            issues.append(f"Step '{step.step_id}' references missing prompt file: {step.prompt_file}")
            continue
            
        prompt_content = load_yaml(prompt_path)
        if not prompt_content:
            issues.append(f"Failed to load prompt file: {step.prompt_file}")
            continue
            
        try:
            prompt_schema = PromptSchema(**prompt_content)
        except ValidationError:
            issues.append(f"Step '{step.step_id}' references invalid prompt file: {step.prompt_file}")
            continue
            
        required_vars = {v.name for v in prompt_schema.variables if v.required}
        
        def flatten_keys(d, parent_key=''):
            items = []
            for k, v in d.items():
                new_key = f"{parent_key}.{k}" if parent_key else k
                if isinstance(v, dict):
                    items.extend(flatten_keys(v, new_key))
                else:
                    items.append(new_key)
            return items
            
        mapped_vars = set(flatten_keys(step.map_inputs))

        
        missing_vars = required_vars - mapped_vars
        if missing_vars:
            issues.append(f"Step '{step.step_id}' is missing mappings for required prompt variables: {missing_vars}")
            
    return issues

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


    # Validate Workflows
    for file_path in iter_workflow_files(dir_path):
        content = load_yaml(str(file_path))
        if not content:
            ok = False
            continue
            
        issues = analyze_workflow_dependencies(str(file_path), content, dir_path)
        if issues:
            print(f"Validation error in workflow {file_path}:")
            for issue in issues:
                print(f"  - {issue}")
            ok = False

    return ok

