import json
import logging
from functools import wraps
from typing import Any, Callable, Dict, Literal, Optional
from pathlib import Path
from pydantic import BaseModel, create_model, ValidationError

from promptops.utils import load_yaml, ROOT
from promptops.validation import PromptSchema

logger = logging.getLogger("proompts_guard")

class ProomptsGuardError(Exception):
    pass

class ProomptsValidationError(ProomptsGuardError):
    pass

def json_schema_to_pydantic_fields(schema: Dict[str, Any]) -> Dict[str, Any]:
    """Convert a simple JSON Schema dictionary to Pydantic model fields."""
    if schema.get("type") != "object":
        raise ValueError("Only 'object' type is supported for root output_schema.")
    
    properties = schema.get("properties", {})
    required = schema.get("required", [])
    
    fields = {}
    for prop_name, prop_details in properties.items():
        prop_type = prop_details.get("type", "string")
        
        if prop_type == "string":
            py_type = str
        elif prop_type == "integer":
            py_type = int
        elif prop_type == "number":
            py_type = float
        elif prop_type == "boolean":
            py_type = bool
        elif prop_type == "array":
            items = prop_details.get("items", {})
            item_type = items.get("type", "string")
            if item_type == "string":
                py_type = list[str]
            elif item_type == "integer":
                py_type = list[int]
            elif item_type == "number":
                py_type = list[float]
            elif item_type == "boolean":
                py_type = list[bool]
            else:
                py_type = list[Any]
        elif prop_type == "object":
            py_type = dict
        else:
            py_type = Any
            
        if prop_name in required:
            fields[prop_name] = (py_type, ...)
        else:
            fields[prop_name] = (Optional[py_type], None)
            
    return fields

def extract_text(response: Any) -> str:
    """Extracts string response from LLM SDK object."""
    if isinstance(response, str):
        return response
    
    # OpenAI pydantic model (v1 / v0)
    if hasattr(response, "choices") and isinstance(response.choices, list) and len(response.choices) > 0:
        choice = response.choices[0]
        if hasattr(choice, "message") and hasattr(choice.message, "content"):
            return choice.message.content
            
    # Anthropic
    if hasattr(response, "content") and isinstance(response.content, list) and len(response.content) > 0:
        block = response.content[0]
        if hasattr(block, "text"):
            return block.text
            
    # Dicts
    if isinstance(response, dict):
        if "choices" in response and isinstance(response["choices"], list) and len(response["choices"]) > 0:
            choice = response["choices"][0]
            if isinstance(choice, dict) and "message" in choice and "content" in choice["message"]:
                return choice["message"]["content"]
        if "content" in response and isinstance(response["content"], list) and len(response["content"]) > 0:
            block = response["content"][0]
            if isinstance(block, dict) and "text" in block:
                return block["text"]
                
    raise ValueError(f"Could not extract text from response of type {type(response)}")

def evaluate_rules(response_text: str, evaluators: list[Dict[str, Any]]) -> None:
    for evaluator in evaluators:
        rule = evaluator.get("python") or evaluator.get("rule")
        if not rule:
            continue
        
        if "python" in evaluator:
            local_vars = {"output": response_text}
            try:
                if rule.strip().startswith("return "):
                    func_code = f"def __eval(output):\n    {rule}"
                    exec(func_code, {}, local_vars)
                    passed = local_vars["__eval"](response_text)
                else:
                    exec(rule, {}, local_vars)
                    passed = local_vars.get("passed", True)
                
                if not passed:
                    raise ProomptsValidationError(f"Evaluator '{evaluator.get('name', 'unnamed')}' failed.")
            except Exception as e:
                 if isinstance(e, ProomptsValidationError):
                     raise e
                 raise ProomptsValidationError(f"Evaluator '{evaluator.get('name', 'unnamed')}' raised exception: {e}")

def guard(prompt_id: str, mode: Literal["fail_fast", "warning"] = "fail_fast") -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            # 1. Execute the function to get the LLM response
            response = func(*args, **kwargs)
            
            try:
                # 2. Extract text from the response
                try:
                    response_text = extract_text(response)
                except ValueError as e:
                    logger.warning(str(e))
                    return response
                
                # 3. Load prompt schema from file
                prompt_path = ROOT / "prompts" / f"{prompt_id}.prompt.yaml"
                if not prompt_path.exists():
                    # Check if they included .prompt.yaml
                    prompt_path = ROOT / "prompts" / prompt_id
                    if not prompt_path.exists():
                        raise FileNotFoundError(f"Prompt '{prompt_id}' not found.")
                
                prompt_data = load_yaml(prompt_path)
                schema_model = PromptSchema(**prompt_data)
                
                # 4. Validate output_schema if it exists
                if schema_model.output_schema:
                    # Try to strip common markdown json formatting
                    cleaned_text = response_text.strip()
                    if cleaned_text.startswith("```json"):
                        cleaned_text = cleaned_text[7:]
                    elif cleaned_text.startswith("```"):
                        cleaned_text = cleaned_text[3:]
                    if cleaned_text.endswith("```"):
                        cleaned_text = cleaned_text[:-3]
                    cleaned_text = cleaned_text.strip()
                    
                    try:
                        parsed_json = json.loads(cleaned_text)
                    except json.JSONDecodeError:
                        raise ProomptsValidationError("Response is not valid JSON.")
                        
                    fields = json_schema_to_pydantic_fields(schema_model.output_schema)
                    DynamicModel = create_model("DynamicOutputModel", **fields)
                    
                    try:
                        DynamicModel.model_validate(parsed_json)
                    except ValidationError as ve:
                        # Find the specific field that failed
                        errors = ve.errors()
                        if errors:
                            error = errors[0]
                            loc = ".".join([str(l) for l in error.get("loc", [])])
                            msg = error.get("msg", "")
                            error_type = error.get("type", "")
                            if error_type == "missing":
                                raise ProomptsValidationError(f"missing required field: '{loc}'")
                            else:
                                raise ProomptsValidationError(f"field '{loc}' failed validation: {msg}")
                        raise ProomptsValidationError(f"Validation error: {ve}")
                        
                # 5. Evaluate basic rules if any
                if schema_model.evaluators:
                    evaluate_rules(response_text, schema_model.evaluators)
                
                logger.info(f"ProomptsGuard validation succeeded for prompt '{prompt_id}'.")
                    
            except ProomptsValidationError as e:
                logger.error(f"ProomptsGuard validation failed for prompt '{prompt_id}': {e}")
                if mode == "fail_fast":
                    raise e
                else:
                    logger.warning(f"Passing through invalid response for prompt '{prompt_id}' due to warning mode.")
                    
            return response
        return wrapper
    return decorator
