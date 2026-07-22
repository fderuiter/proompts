"""Module docstring."""
import logging
from functools import wraps
from typing import Any, Callable, Literal

from promptops.utils import load_yaml, ROOT
from promptops.validation import PromptSchema, ProomptsValidationError, validate_response

logger = logging.getLogger("promptops.guard")


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


def guard(prompt_id: str, mode: Literal["fail_fast", "warning"] = "fail_fast") -> Callable:
    """Missing docstring."""
    def decorator(func: Callable) -> Callable:
        """Missing docstring."""
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            """Missing docstring."""
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
                
                # 4. Validate output
                response_text = validate_response(response_text, schema_model.output_schema, schema_model.evaluators)
                # Return the original response object if not a string, but if string, return modified string
                if isinstance(response, str):
                    response = response_text
                
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
