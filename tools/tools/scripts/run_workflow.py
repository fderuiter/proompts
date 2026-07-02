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

from __future__ import annotations
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../promptops")))
from promptops import console

import argparse
import logging
from typing import Any, Dict, Optional

from promptops.utils import load_yaml
from promptops.engine import run_workflow

logger = logging.getLogger(__name__)

def setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s')
    logger.setLevel(level)

def main():
    parser = argparse.ArgumentParser(
        description="Simulate a prompt workflow execution using mock data."
    )
    parser.add_argument("workflow_file", help="Path to the .workflow.yaml file.")
    parser.add_argument("-i", "--input", action='append', help="Set a workflow input, e.g., -i name='value'")
    parser.add_argument("-f", "--inputs-file", help="Path to a JSON or YAML file containing workflow inputs")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
    parser.add_argument("--strict", action="store_true", help="Run in strict mode")
    parser.add_argument("--chaos", action="store_true", help="Enable Chaos Mode")
    parser.add_argument("--no-color", action="store_true", help="Disable color output")
    parser.add_argument("--json", action="store_true", help="Output Fidelity Report as JSON only")

    args = parser.parse_args()

    if args.no_color:
        console.set_no_color(True)
        
    if args.json:
        console.set_json_mode(True)

    strict_mode = args.strict or os.environ.get('CI') == 'true'
    setup_logging(args.verbose)

    initial_inputs = {}

    if args.inputs_file:
        import json
        file_ext = args.inputs_file.split('.')[-1].lower()
        try:
            if file_ext in ['yaml', 'yml']:
                file_inputs = load_yaml(args.inputs_file)
                if file_inputs is None:
                    sys.exit(1)
                initial_inputs.update(file_inputs)
            elif file_ext == 'json':
                with open(args.inputs_file, 'r') as f:
                    initial_inputs.update(json.load(f))
            else:
                logger.error(f"Unsupported inputs file extension '{file_ext}'.")
                sys.exit(1)
        except Exception as e:
            logger.error(f"Failed to load inputs file {args.inputs_file}: {e}")
            sys.exit(1)

    if args.input:
        for item in args.input:
            if '=' in item:
                key, value = item.split('=', 1)
                initial_inputs[key] = value
            else:
                logger.warning(f"Invalid input format: {item}. Expected key=value")

    fidelity_report = {
        'evaluators_mocked': False,
        'rate_limits_simulated': False,
        'latency_simulated': False
    }

    workflow_data = load_yaml(args.workflow_file)
    if not initial_inputs and workflow_data and workflow_data.get('testData'):
        for test_case in workflow_data['testData']:
            inputs = test_case.get('inputs', test_case.get('vars', {}))
            console.step_header(f"Running Workflow Test Scenario with inputs: {inputs}")
            try:
                final_state = run_workflow(args.workflow_file, inputs, verbose=args.verbose, strict_mode=strict_mode, chaos_mode=args.chaos, fidelity_report=fidelity_report)
                if final_state:
                    final_output_step_id = workflow_data.get('steps', [{}])[-1].get('step_id')
                    if final_output_step_id:
                        final_output = final_state['steps'][final_output_step_id]['output']
                        logger.info(f"Scenario Output:\n{final_output}")
            except Exception as e:
                logger.error(f"Workflow test scenario failed: {e}")
                sys.exit(1)
        console.step_header("Simulation Finished (All Scenarios)")
    else:
        try:
            final_state = run_workflow(args.workflow_file, initial_inputs, verbose=args.verbose, strict_mode=strict_mode, chaos_mode=args.chaos, fidelity_report=fidelity_report)
        except Exception as e:
            logger.error(f"Workflow simulation failed: {e}")
            sys.exit(1)

        if final_state:
            console.step_header("Simulation Finished")
            final_output_step_id = workflow_data.get('steps', [{}])[-1].get('step_id')
            if final_output_step_id:
                final_output = final_state['steps'][final_output_step_id]['output']
                logger.info("Final workflow output:")
                console.info(final_output)

    if getattr(args, 'json', False):
        console.json_output(fidelity_report)
    else:
        console.info("\n[Simulation Fidelity Report]")
        console.info(f"- Evaluators Mocked: {'Yes' if fidelity_report['evaluators_mocked'] else 'No'}")
        console.info(f"- Rate Limits Simulated: {'Yes' if fidelity_report['rate_limits_simulated'] else 'No'}")
        console.info(f"- Latency Simulated: {'Yes' if fidelity_report['latency_simulated'] else 'No'}")

if __name__ == "__main__":
    main()
