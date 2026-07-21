"""
inject_test_data.py: Data Injection Utility

WHAT:
This script scans all `.workflow.yaml` files in the `workflows/` directory. If a workflow is missing the `testData` field, it automatically inspects the required inputs from the step mappings and injects a mock `testData` block.

WHY:
Ensures all workflows have baseline test data for simulation and validation without requiring manual data entry for every single required input.

HOW TO USE:
python3 tools/tools/scripts/inject_test_data.py
"""

import yaml
from pathlib import Path
import re

from promptops.utils import iter_workflow_files

ROOT_DIR = Path(__file__).resolve().parents[3]
workflows = iter_workflow_files(ROOT_DIR)

for wf in workflows:
    with open(wf, 'r', encoding='utf-8') as f:
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
        
        with open(wf, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, sort_keys=False)

