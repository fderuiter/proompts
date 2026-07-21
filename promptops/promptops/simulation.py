import json
from pathlib import Path
from promptops.utils import load_yaml
from promptops import console
from promptops.engine import simulate_prompt_execution

def simulate_prompt(prompt_file: str, data_file: str, chaos_mode: bool = False, strict_mode: bool = False) -> bool:
    try:
        content = load_yaml(prompt_file)
        if not content:
            path_obj = Path(prompt_file)
            from promptops.utils import resolve_fallback_prompt
            content = resolve_fallback_prompt(path_obj)
        
        if not content:
            console.error(f"Failed to load prompt: {prompt_file} (Not found in files or manifest)")
            return False
            
    except Exception as e:
        console.error(f"Failed to load prompt: {e}")
        return False
        
    data_path = Path(data_file)
    if not data_path.exists():
        console.error(f"Data file not found: {data_file}")
        return False
        
    try:
        if data_path.suffix == '.json':
            mock_data = json.loads(data_path.read_text(encoding='utf-8'))
        else:
            mock_data = load_yaml(data_path)
    except Exception as e:
        console.error(f"Failed to load mock data: {e}")
        return False
        
    try:
        fidelity_report: dict = {}
        output = simulate_prompt_execution(
            content, 
            mock_data, 
            prompt_file=prompt_file, 
            strict_mode=strict_mode, 
            chaos_mode=chaos_mode,
            fidelity_report=fidelity_report
        )
        console.info(f"\nFinal Output:\n{output}")
        return True
    except Exception as e:
        console.error(f"Simulation failed: {e}")
        return False
