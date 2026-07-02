import os
import re
import jinja2
from enum import Enum
from pathlib import Path
from typing import Any, List, Optional, Dict, Union

from pydantic import BaseModel, ValidationError, field_validator, model_validator, Field
from promptops.utils import load_yaml, iter_prompt_files, iter_workflow_files
from promptops.engine import run_workflow
from promptops import console

VAR_PATTERN = re.compile(r'\{\{([^}]+)\}\}')

class ComplexityLevel(str, Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

class ToolCall(BaseModel):
    id: str = Field(...)
    type: str = Field("function")
    function: Dict[str, Any] = Field(...)

class Message(BaseModel):
    role: Optional[str] = Field(None)
    content: Optional[Union[str, List[Any]]] = Field(None)
    tool_calls: Optional[List[ToolCall]] = Field(None)
    tool_call_id: Optional[str] = Field(None)
    name: Optional[str] = Field(None)

    @model_validator(mode='after')
    def check_content_or_tool_calls(self):
        # Allow content to be missing/null if tool_calls is provided
        """
        Ensure a Message has either `content` or `tool_calls` unless its role is "tool" or "tool_result".
        
        Returns:
            self: The validated Message instance.
        
        Raises:
            ValueError: If both `content` and `tool_calls` are missing or empty for messages whose role is not "tool" or "tool_result".
        """
        if not self.content and not self.tool_calls and self.role != "tool" and self.role != "tool_result":
            raise ValueError(
                f"Message with role '{self.role}' must have either 'content' or 'tool_calls'. "
                "Both are missing or empty."
            )
        return self

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
    autonomy: Optional[str] = Field(None)
    maturity: Optional[str] = Field(None)

class InputSchema(BaseModel):
    type: str = Field("object")
    properties: Optional[Dict[str, Any]] = Field(None)
    required: Optional[List[str]] = Field(None)

class MCPTool(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    inputSchema: InputSchema = Field(...)

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
    tools: Optional[List[MCPTool]] = Field(None)
    testData: List[Any] = Field(...)
    evaluators: List[Any] = Field(...)
    output_schema: Optional[Dict[str, Any]] = Field(None)
    last_modified: Optional[str] = Field(None)

    @field_validator("evaluators")
    @classmethod
    def check_evaluators_logic(_cls, v: List[Any]) -> List[Any]:
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
    def check_messages_length(_cls, v: List[Message]) -> List[Message]:
        if len(v) < 2:
            raise ValueError("messages list must have at least 2 items")
        return v

    @model_validator(mode='after')
    def check_variables_match_content(self):
        """
        Validate that template variables referenced in message content or tool-call payloads are syntactically valid and match the prompt's declared variables.
        
        This validator:
        - Checks the Jinja2 syntax of each message content. Raises ValueError if the syntax is invalid.
        - Extracts template variables from each message using Jinja2 AST parsing.
        - Ensures each variable name matches the pattern `^[a-zA-Z0-9_.-]+$`; raises ValueError if any invalid variable names are found.
        - Prints a warning for variables declared in `variables` but not used in any message.
        - Raises ValueError if any variables are used in messages but not declared in `variables`.
        
        Returns:
            self (PromptSchema): The validated model instance.
        """
        found_vars: set[str] = set()
        invalid_vars: set[str] = set()
        
        env = jinja2.Environment()
        
        for msg in self.messages:
            content_str = ""
            if isinstance(msg.content, str):
                content_str = msg.content
            elif isinstance(msg.content, list):
                content_str = " ".join([str(c) for c in msg.content])
            elif not msg.content and msg.tool_calls:
                content_str = str(msg.tool_calls)

            try:
                ast = env.parse(content_str)
                vars_in_text = jinja2.meta.find_undeclared_variables(ast)
                found_vars.update(vars_in_text)
            except jinja2.exceptions.TemplateSyntaxError as e:
                raise ValueError(f"Jinja2 syntax error: {e.message} at line {e.lineno}")

            for var in vars_in_text:
                valid_match = re.match(r'^[a-zA-Z0-9_.-]+$', var)
                if not valid_match:
                    invalid_vars.add(var)

        if invalid_vars:
            raise ValueError(f"Migration Required: Variables contain invalid characters: {invalid_vars}")

        defined_vars = {v.name for v in self.variables}
        unused = defined_vars - found_vars
        if unused:
            console.warn(f"Variables defined but not used in prompt: {unused}")

        undefined = found_vars - defined_vars
        if undefined:
            raise ValueError(f"Variables used in messages but NOT defined in 'variables' section: {undefined}")

        return self

    @model_validator(mode='after')
    def check_test_data_types(self):
        """Warn if testData contains non-string types that will be coerced to strings."""
        if not self.testData:
            return self
            
        for case in self.testData:
            if isinstance(case, dict):
                # Check inputs
                inputs = case.get('inputs', {})
                if isinstance(inputs, dict):
                    for k, v in inputs.items():
                        if not isinstance(v, str):
                            console.warn(f"Test data input '{k}' is of type {type(v).__name__}. The runtime engine will cast this to a string.")
                
                # Check expected
                expected = case.get('expected')
                if expected is not None and not isinstance(expected, str):
                    console.warn(f"Test data expected output is of type {type(expected).__name__}. The runtime engine will cast this to a string.")
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
    topic: str = Field(...)

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
    graph: Dict[str, List[str]] = {}
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
        from promptops.utils import ROOT
        prompt_path = os.path.join(str(ROOT), step.prompt_file)
        prompt_content = None
        
        if os.path.exists(prompt_path):
            prompt_content = load_yaml(prompt_path)
            
        required_vars = set()
        found_valid = False
            
        if not prompt_content:
            path_obj = Path(prompt_path)
            skills_md = path_obj.parent / "skills.md"
            if skills_md.exists():
                from promptops.utils import parse_skill_manifest
                manifest = parse_skill_manifest(skills_md)
                
                def get_words(text):
                    words = set()
                    for w in re.findall(r'[a-z]+|[0-9]+', text.lower()):
                        if w.isdigit():
                            words.add(str(int(w)))
                        else:
                            words.add(w)
                    return words

                stem = path_obj.name.replace('.prompt.md', '').replace('.prompt.yml', '')
                stem_clean = re.sub(r'^\d+_', '', stem).lower()
                stem_words = get_words(stem_clean)
                
                best_match = None
                best_score = 0
                best_skill_len = float('inf')
                skills_list = manifest.get("skills", [])
                for skill in skills_list:
                    skill_name_clean = skill["name"].lower()
                    skill_words = get_words(skill_name_clean)
                    
                    score = len(stem_words & skill_words)
                    if score > best_score or (score > 0 and score == best_score and len(skill_words) < best_skill_len):
                        best_score = score
                        best_match = skill
                        best_skill_len = len(skill_words)
                
                if not best_match or best_score == 0:
                    m = re.match(r'^(\d+)_', stem)
                    if m:
                        idx = int(m.group(1)) - 1
                        if 0 <= idx < len(skills_list):
                            best_match = skills_list[idx]
                            best_score = 1
                
                if best_match and best_score > 0:
                    found_valid = True
                    for v in best_match.get("variables", []):
                        if isinstance(v, str):
                            required_vars.add(v)
                        elif isinstance(v, dict):
                            if v.get("required", True):
                                required_vars.add(v.get("name", "unknown"))

            if not found_valid:
                issues.append(f"Step '{step.step_id}' references missing prompt file or skill: {step.prompt_file}")
                continue
        else:
            try:
                prompt_schema = PromptSchema(**prompt_content)
                required_vars = {v.name for v in prompt_schema.variables if v.required}
            except ValidationError:
                issues.append(f"Step '{step.step_id}' references invalid prompt file: {step.prompt_file}")
                continue
        
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
    seen_names: Dict[str, str] = {}
    dir_path = os.environ.get('PROMPTOPS_REGISTRY', directory)
    dirs_to_check: Set[Path] = set()
    
    NAMING_RULES = {
        "meta": re.compile(r"^L\d+_.*\.prompt\.(ya?ml|md)$", re.IGNORECASE),
    }

    for file_path in iter_prompt_files(dir_path):
        
        # Collect directory to check hygiene later
        path = file_path.parent
        base_path = Path(dir_path).resolve()
        while path != base_path and base_path in path.parents:
            dirs_to_check.add(path)
            path = path.parent
        # Include if file is directly in dir_path
        if file_path.parent == base_path:
            dirs_to_check.add(base_path)

        if file_path.parent.name in NAMING_RULES and not file_path.name.endswith(".workflow.yaml") and not file_path.name.endswith(".workflow.yml"):
            if not NAMING_RULES[file_path.parent.name].match(file_path.name):
                console.error(f"{file_path} does not match required pattern for {file_path.parent.name}")
                ok = False

        content = load_yaml(str(file_path))
        if not content:
            ok = False
            continue
            
        try:
            PromptSchema(**content)
        except ValidationError as e:
            console.error(f"Validation error in {file_path}:\n{e}")
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
                console.warn(f"{file_path} has {', '.join(issues)}")

        name = content.get('name')
        if name:
            if name in seen_names:
                console.error(f"Duplicate name '{name}' found in:\n  - {seen_names[name]}\n  - {file_path}")
                ok = False
            else:
                seen_names[name] = str(file_path)


    # Validate Workflows
    for file_path in iter_workflow_files(dir_path):
        # Collect directory to check hygiene later
        path = file_path.parent
        base_path = Path(dir_path).resolve()
        while path != base_path and base_path in path.parents:
            dirs_to_check.add(path)
            path = path.parent
        if file_path.parent == base_path:
            dirs_to_check.add(base_path)

        if file_path.parent.name in NAMING_RULES and not file_path.name.endswith(".workflow.yaml") and not file_path.name.endswith(".workflow.yml"):
            if not NAMING_RULES[file_path.parent.name].match(file_path.name):
                console.error(f"{file_path} does not match required pattern for {file_path.parent.name}")
                ok = False

        content = load_yaml(str(file_path))
        if not content:
            ok = False
            continue
            
        issues = analyze_workflow_dependencies(str(file_path), content, dir_path)
        if issues:
            console.error(f"Validation error in workflow {file_path}:")
            for issue in issues:
                console.error(f"  - {issue}")
            ok = False

        if strict:
            test_data = content.get('testData', [])
            if test_data:
                for i, test_case in enumerate(test_data):
                    inputs = test_case.get('inputs', test_case.get('vars', {}))
                    try:
                        run_workflow(str(file_path), inputs, verbose=False, strict_mode=True)
                    except Exception as e:
                        console.error(f"Simulation failed on {file_path} scenario {i+1}: {e}")
                        ok = False
                        break
            else:
                try:
                    run_workflow(str(file_path), {}, verbose=False, strict_mode=True)
                except Exception as e:
                    console.error(f"Simulation failed on {file_path}: {e}")
                    ok = False

    # Check directory hygiene
    for directory in dirs_to_check:
        if not (directory / "overview.md").exists():
            console.error(f"Missing overview.md in {directory}")
            ok = False
            
        has_manifest = (directory / "skills.md").exists()
        for file in directory.iterdir():
            if not file.is_file() or file.name.startswith('.'):
                continue
            name = file.name
            lower_name = name.lower()
            if lower_name in {"overview.md", "readme.md", "skills.md"} or lower_name.endswith(".workflow.md"):
                continue

            is_prompt = lower_name.endswith(".prompt.md") or lower_name.endswith(".prompt.yml") or lower_name.endswith(".prompt.yaml")
            is_workflow = lower_name.endswith(".workflow.yaml") or lower_name.endswith(".workflow.yml")

            if has_manifest and is_prompt:
                console.error(f"Error: {file} is redundant because a skills.md manifest exists in {directory}")
                ok = False

            if not (is_prompt or is_workflow):
                console.error(f"{file} is not a recognised prompt or workflow file")
                ok = False

    return ok

