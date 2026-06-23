import json
import yaml
from pathlib import Path
from jinja2.sandbox import SandboxedEnvironment
from promptops.utils import load_yaml
from promptops import console

def simulate_prompt(prompt_file: str, data_file: str) -> bool:
    """
    Simulate a prompt definition against mock input data, rendering message content and optional tool call arguments as Jinja2 templates and printing the results.
    
    Parameters:
        prompt_file (str): Path to a prompt YAML file containing prompt metadata and a "messages" list.
        data_file (str): Path to a mock data file (JSON or YAML) used as the template context.
    
    Returns:
        bool: `True` if the prompt and mock data were loaded and all messages were processed; `False` if loading or parsing failed or if the data file is missing.
    """
    try:
        content = load_yaml(prompt_file)
    except Exception as e:
        console.error(f"Failed to load prompt: {e}")
        return False
        
    data_path = Path(data_file)
    if not data_path.exists():
        console.error(f"Data file not found: {data_file}")
        return False
        
    try:
        if data_path.suffix == '.json':
            mock_data = json.loads(data_path.read_text())
        else:
            mock_data = yaml.safe_load(data_path.read_text())
    except Exception as e:
        console.error(f"Failed to load mock data: {e}")
        return False
        
    env = SandboxedEnvironment()
    
    console.step_header(f"Simulating Prompt: {content.get('name', 'Unknown')}")
    messages = content.get('messages', [])
    for msg in messages:
        role = msg.get('role', 'unknown')
        raw_content = msg.get('content')
        
        if raw_content is not None:
            if isinstance(raw_content, list):
                content_str = yaml.dump(raw_content, sort_keys=False).strip()
            else:
                content_str = str(raw_content)
                
            template = env.from_string(content_str)
            rendered = template.render(**mock_data)
            console.role_message(role, rendered)
            
        tool_calls = msg.get('tool_calls')
        if tool_calls:
            # Recursively render templated variables in tool_calls structure
            def render_structure(obj, env, data):
                """
                Recursively renders all string values in a nested structure as Jinja templates using the provided environment and context.
                
                Parameters:
                    obj: The input value to render; may be a string, dict, list, or any other type.
                    env: A Jinja2 environment used to compile and render string templates.
                    data: A mapping of context values supplied to template rendering.
                
                Returns:
                    The same structure as `obj` with all strings replaced by their rendered results; dicts and lists are recreated with rendered children, and non-string, non-collection values are returned unchanged.
                """
                if isinstance(obj, str):
                    template = env.from_string(obj)
                    return template.render(**data)
                elif isinstance(obj, dict):
                    return {k: render_structure(v, env, data) for k, v in obj.items()}
                elif isinstance(obj, list):
                    return [render_structure(item, env, data) for item in obj]
                else:
                    return obj

            rendered_tool_calls = render_structure(tool_calls, env, mock_data)
            tc_yaml = yaml.dump(rendered_tool_calls, sort_keys=False, default_flow_style=False).strip()
            console.role_message("tool_call", tc_yaml)
        
    return True
