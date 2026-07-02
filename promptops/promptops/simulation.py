import json
import yaml
from pathlib import Path
from promptops.utils import load_yaml
from promptops import console
from promptops.engine import simulate_prompt_execution

def simulate_prompt(prompt_file: str, data_file: str, chaos_mode: bool = False, strict_mode: bool = False) -> bool:
    try:
        content = load_yaml(prompt_file)
        if not content:
            import re
            path_obj = Path(prompt_file)
            skills_md = path_obj.parent / "skills.md"
            if skills_md.exists():
                from promptops.utils import parse_skill_manifest
                manifest = parse_skill_manifest(skills_md)
                
                stem = path_obj.name.replace('.prompt.md', '').replace('.prompt.yml', '')
                stem_clean = re.sub(r'^\d+_', '', stem).replace('_', ' ').lower()
                
                for skill in manifest.get("skills", []):
                    skill_name_clean = skill["name"].lower().replace('_', ' ')
                    if stem_clean in skill_name_clean or skill_name_clean in stem_clean or skill["name"].replace(' ', '_').lower() in stem:
                        content = {
                            "name": skill["name"],
                            "description": skill.get("description", ""),
                            "variables": skill.get("variables", []),
                            "messages": [{"role": "system", "content": skill.get("instructions", "")}],
                            "testData": skill.get("testData", [])
                        }
                        break
        
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
            mock_data = json.loads(data_path.read_text())
        else:
            mock_data = yaml.safe_load(data_path.read_text())
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
