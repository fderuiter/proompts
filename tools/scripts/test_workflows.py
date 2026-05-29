#!/usr/bin/env python3
"""
Test Workflows Script

Discovers all .workflow.yaml files in the workflows/ directory and runs
them through the simulation engine in strict mode to detect structural
errors, unresolved template variables, or missing step references.
"""

import sys
import glob
from pathlib import Path
from run_workflow import run_workflow, load_yaml, setup_logging

def main():
    setup_logging(verbose=False)
    
    # We will import run_workflow function directly and set strict_mode=True
    base_dir = Path(__file__).resolve().parent.parent.parent
    workflows_dir = base_dir / "workflows"
    
    workflow_files = workflows_dir.rglob("*.workflow.yaml")
    
    failed = []
    
    for wf in workflow_files:
        print(f"Testing workflow: {wf.relative_to(base_dir)}")
        
        # Load to extract testData
        workflow_data = load_yaml(str(wf))
        if not workflow_data:
            print(f"  ❌ Failed to parse YAML: {wf}")
            failed.append(wf)
            continue
            
        test_data = workflow_data.get('testData', [])
        
        if test_data:
            for i, test_case in enumerate(test_data):
                inputs = test_case.get('inputs', test_case.get('vars', {}))
                try:
                    # Run in strict mode
                    run_workflow(str(wf), inputs, verbose=False, strict_mode=True)
                except Exception as e:
                    print(f"  ❌ Simulation failed on scenario {i+1}: {e}")
                    failed.append(wf)
                    break
        else:
            # Still run strict mode with empty inputs to catch structural errors
            try:
                run_workflow(str(wf), {}, verbose=False, strict_mode=True)
            except Exception as e:
                print(f"  ❌ Simulation failed: {e}")
                failed.append(wf)
                
    if failed:
        print("\n❌ The following workflows have structural errors:")
        for wf in set(failed):
            print(f"  - {wf.relative_to(base_dir)}")
        sys.exit(1)
    else:
        print("\n✅ All workflows validated successfully.")
        sys.exit(0)

if __name__ == "__main__":
    main()
