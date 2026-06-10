import json
import yaml
from pathlib import Path
from jinja2.sandbox import SandboxedEnvironment
from promptops.utils import load_yaml

def simulate_prompt(prompt_file: str, data_file: str) -> bool:
    try:
        content = load_yaml(prompt_file)
    except Exception as e:
        print(f"Failed to load prompt: {e}")
        return False
        
    data_path = Path(data_file)
    if not data_path.exists():
        print(f"Data file not found: {data_file}")
        return False
        
    try:
        if data_path.suffix == '.json':
            mock_data = json.loads(data_path.read_text())
        else:
            mock_data = yaml.safe_load(data_path.read_text())
    except Exception as e:
        print(f"Failed to load mock data: {e}")
        return False
        
    env = SandboxedEnvironment()
    
    print(f"--- Simulating Prompt: {content.get('name', 'Unknown')} ---")
    messages = content.get('messages', [])
    for msg in messages:
        role = msg.get('role', 'unknown')
        raw_content = msg.get('content')
        
        print(f"\n[{role.upper()}]:")
        
        if raw_content is not None:
            if isinstance(raw_content, list):
                content_str = yaml.dump(raw_content, sort_keys=False).strip()
            else:
                content_str = str(raw_content)
                
            template = env.from_string(content_str)
            rendered = template.render(**mock_data)
            print(rendered)
            
        tool_calls = msg.get('tool_calls')
        if tool_calls:
            print("[TOOL_CALL]:")
            tc_yaml = yaml.dump(tool_calls, sort_keys=False, default_flow_style=False).strip()
            print(tc_yaml)
            
        print("-" * 40)
        
    return True
