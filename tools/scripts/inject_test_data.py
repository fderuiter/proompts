import yaml
import glob
from pathlib import Path
import re

workflows = glob.glob("/app/workflows/**/*.workflow.yaml", recursive=True)

for wf in workflows:
    with open(wf, 'r') as f:
        data = yaml.safe_load(f)
    
    if 'testData' not in data:
        print(f"Injecting testData into {wf}")
        
        # Determine required inputs
        required_vars = set()
        for step in data.get('steps', []):
            for map_k, map_v in step.get('map_inputs', {}).items():
                if isinstance(map_v, str):
                    matches = re.findall(r'\{\{\s*inputs\.([\w\-]+)\s*\}\}', map_v)
                    for m in matches:
                        required_vars.add(m)
        
        inputs = {}
        for var in required_vars:
            inputs[var] = "Sample " + var
            
        data['testData'] = [
            {
                "inputs": inputs
            }
        ]
        
        with open(wf, 'w') as f:
            yaml.dump(data, f, sort_keys=False)

