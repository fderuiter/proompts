#!/usr/bin/env python3
"""
run_workflow.py: The Workflow Simulation Engine

WHAT:
This script loads a `.workflow.yaml` file, parses the step execution order,
resolves inter-step variable mappings, and simulates the output of each prompt.

WHY:
It allows developers to verify the logic, input mappings, and output extraction
of complex prompt chains *without* incurring any LLM API costs or dealing with
network latency. It ensures your workflows are structurally sound before deployment.

HOW TO USE:
# Simulate a workflow with verbose output
python3 tools/tools/scripts/run_workflow.py path/to/workflow.workflow.yaml -v

# Simulate with initial inputs
python3 tools/tools/scripts/run_workflow.py path/to/workflow.workflow.yaml -i user_name="Alice"

Parameters:
  workflow_file : Path to the `.workflow.yaml` file
  -i, --input   : Initial input variables (key=value)
  -v, --verbose : Enable verbose logging
"""

import sys
import subprocess

print("WARNING: This script is deprecated. Please use 'promptops workflow' instead.", file=sys.stderr)

cmd = ["promptops", "workflow"] + sys.argv[1:]
try:
    # Use subprocess to run the new command through uv if needed, or directly if installed
    subprocess.run(["uv", "run"] + cmd, check=True)
except subprocess.CalledProcessError as e:
    sys.exit(e.returncode)
except FileNotFoundError:
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)
