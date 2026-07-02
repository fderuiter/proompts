#!/usr/bin/env python3
"""
Inject Test Data Script

## What is this?
This script scans all `.workflow.yaml` files and automatically injects a boilerplate `testData` array if it is missing, based on the input variables detected in the workflow steps.

## Why use it?
- **Accelerates Testing:** Provides a quick baseline for workflow developers to start simulating their chains without manually writing the entire testData block.
- **Maintains Consistency:** Ensures all workflows have a testData schema ready for `promptops workflow` simulation.

> [!WARNING]
> **Manual Setup Required:**
> This script currently hardcodes the target path as `/app/workflows/`, which is not a standard repository directory unless you are running inside a specific container structure. You must manually ensure this path exists or modify the script locally before execution.

## How to use it?
```bash
python3 tools/tools/scripts/inject_test_data.py
```
"""

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

