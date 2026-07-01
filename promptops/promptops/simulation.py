import json
import yaml
from pathlib import Path
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
        
    from promptops.engine import run
    result = run(prompt_file, mock_data, verbose=True)
    return result is not None
