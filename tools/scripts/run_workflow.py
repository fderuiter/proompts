from __future__ import annotations

import argparse
import logging
import os
import re
from typing import Any, Dict, Optional

import yaml

# Configure logger
logger = logging.getLogger(__name__)

def setup_logging(verbose: bool = False):
    """Configures the logger."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format='%(levelname)s: %(message)s')
    # Ensure module logger follows the level
    logger.setLevel(level)

def load_yaml(file_path: str) -> Optional[Dict[str, Any]]:
    """
    Loads a YAML file from the given path.

    Args:
        file_path: The path to the YAML file.

    Returns:
        The parsed YAML content as a dictionary, or None if the file is not found.
    """
    if not os.path.exists(file_path):
        logger.error(f"Error: File not found at {file_path}")
        return None
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def safe_render(template: str, context: Dict[str, Any]) -> Any:
    """
    Safely renders a template string by replacing {{ variables }} with values from context.

    This replaces Jinja2's from_string(template).render(**context) with a restricted
    implementation that only supports simple path-based variable access, preventing
    arbitrary code execution.

    Args:
        template: The string containing template variables (e.g., 'Hello {{ name }}').
        context: The dictionary containing available variables.

    Returns:
        The rendered value. If the template is exactly '{{ variable }}', it returns
        the native type of the variable. Otherwise, it returns a string.
    """
    if not isinstance(template, str) or "{{" not in template:
        return template

    # Regex to find all {{ variable.path }} patterns
    # Supports optional spaces: {{  var.path  }}
    pattern = re.compile(r"\{\{\s*([\w\.\-]+)\s*\}\}")

    # Special case: If the template is ONLY a single variable, preserve its native type
    # e.g., template = '{{ steps.step1.output }}' and output is a list, return the list.
    match = pattern.fullmatch(template.strip())
    if match:
        var_path = match.group(1)
        val = _get_value_from_context(var_path, context)
        # If the variable is missing, return the original template
        return val if val is not None else template

    # General case: string interpolation
    def replace_match(match):
        var_path = match.group(1)
        val = _get_value_from_context(var_path, context)
        return str(val) if val is not None else match.group(0)

    return pattern.sub(replace_match, template)

def _get_value_from_context(path: str, context: Dict[str, Any]) -> Any:
    """Helper to traverse a nested dictionary using a dot-separated path."""
    parts = path.split('.')
    current = context
    try:
        for part in parts:
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return None
        return current
    except (KeyError, TypeError):
        return None

def resolve_value(template_string: str, workflow_state: Dict[str, Any]) -> Any:
    """
    Resolves a template string like '{{steps.step_id.output}}' from the workflow state.

    This is part of the simulation engine, resolving variable mappings between steps
    without executing external code.

    Args:
        template_string: The string containing the template variable.
        workflow_state: The current state of the workflow containing inputs and steps.

    Returns:
        The resolved value if the template matches, otherwise the original string.
    """
    try:
        return safe_render(template_string, workflow_state)
    except Exception as e:
        logger.warning(f"Warning: Could not resolve value for template '{template_string}': {e}")
        return template_string

def simulate_prompt_execution(prompt_data: Dict[str, Any], inputs: Dict[str, Any]) -> str:
    """
    Simulates executing a prompt by substituting variables and returning a simulated output.

    NOTE: This function does NOT call any LLM API (e.g., OpenAI). It looks for a matching
    test case in the prompt's `testData` field and returns the expected output. This allows
    for deterministic testing of workflow logic and variable passing.

    Args:
        prompt_data: The prompt data loaded from the YAML file.
        inputs: A dictionary of mapped inputs for the prompt.

    Returns:
        The simulated output string from `testData`.
    """
    logger.info("---")
    logger.info(f"Simulating prompt: {prompt_data.get('name', 'Untitled Prompt')}")

    # Substitute variables in messages
    for message in prompt_data.get('messages', []):
        role = message.get('role', 'user')
        content = message.get('content', '')

        try:
            content = safe_render(content, inputs)
        except Exception as e:
            logger.warning(f"Failed to render message content: {e}")

        logger.info(f"  [{role}]: (Content hidden for security)")

    # Simulate output
    # Try to find a matching test case in testData
    if prompt_data.get('testData'):
        for test_case in prompt_data['testData']:
            # Check if expected inputs match actual inputs
            # Support both 'vars' (common in prompts) and 'inputs'
            expected_inputs = test_case.get('vars', test_case.get('inputs', {}))
            match = True
            for k, v in expected_inputs.items():
                # Convert both to string for comparison to handle potential type mismatches
                # Note: We cast to string because testData inputs might be defined as ints/bools
                # in YAML, but command-line inputs (-i) are parsed as strings.
                if k not in inputs or str(inputs[k]) != str(v):
                    match = False
                    break

            if match:
                logger.info("Found matching test case. Using its expected output.")
                output = test_case.get('expected', 'No expected output in test case.')
                return output[0] if isinstance(output, list) else output

        # If no match, use the first test case's output
        logger.info("No matching test case found. Using the first available test case output.")
        fallback_output = prompt_data['testData'][0].get('expected', 'Simulated output from first test case.')
        return fallback_output[0] if isinstance(fallback_output, list) else fallback_output

    # If no testData, return a generic placeholder
    return f"[Simulated output for prompt: {prompt_data.get('name', 'Untitled Prompt')}]"


def run_workflow(workflow_file: str, initial_inputs: Dict[str, Any], verbose: bool = True) -> Optional[Dict[str, Any]]:
    """
    Loads and simulates a workflow from a given file path.

    This function orchestrates the flow of data between steps but mocks the actual
    intelligence using the `simulate_prompt_execution` function.

    Args:
        workflow_file: Path to the workflow YAML file.
        initial_inputs: Dictionary of initial inputs for the workflow.
        verbose: Whether to print detailed execution logs.

    Returns:
        The final workflow state dictionary, or None if the workflow file could not be loaded.
    """
    # Configure logger level based on verbose flag if running standalone or called directly
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # If no handlers exist (e.g. called from another script without setup), add basic handler
    if not logger.handlers and not logging.getLogger().handlers:
         logging.basicConfig(level=logger.level, format='%(levelname)s: %(message)s')


    workflow_data = load_yaml(workflow_file)
    if not workflow_data:
        return None

    logger.info(f"Starting workflow simulation: {workflow_data.get('name', 'Untitled Workflow')}")
    logger.info("ℹ️  NOTE: Running in SIMULATION MODE. No API calls will be made.")

    # Initialize workflow state
    workflow_state = {
        "inputs": initial_inputs,
        "steps": {}
    }

    # Execute each step in order
    for step in workflow_data.get('steps', []):
        step_id = step['step_id']
        prompt_file = step['prompt_file']

        logger.info(f"\n===== Simulating Step: {step_id} =====")

        # 1. Load the prompt file
        prompt_data = load_yaml(prompt_file)
        if not prompt_data:
            logger.warning(f"Skipping step {step_id} due to missing prompt file.")
            continue

        # 2. Resolve inputs for the prompt
        prompt_inputs = {}
        for var_name, template in step.get('map_inputs', {}).items():
            prompt_inputs[var_name] = resolve_value(template, workflow_state)

        logger.debug(f"Resolved prompt inputs: {list(prompt_inputs.keys())}")

        # 3. Simulate prompt execution
        output = simulate_prompt_execution(prompt_data, prompt_inputs)

        # 4. Store the output in the workflow state
        workflow_state['steps'][step_id] = {'output': output}
        logger.debug(f"Step '{step_id}' produced output: (Content hidden for security)")

    return workflow_state

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Simulate a prompt workflow execution using mock data.\n\n"
            "NOTE: This tool does NOT make API calls to LLMs. It uses the 'testData' field "
            "in your prompt files to deterministically simulate outputs for validation."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("workflow_file", help="Path to the .workflow.yaml file.")
    parser.add_argument("-i", "--input", action='append', help="Set a workflow input, e.g., -i name='value' (Not recommended for sensitive data)")
    parser.add_argument("-f", "--inputs-file", help="Path to a JSON or YAML file containing workflow inputs (Recommended for security)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")

    args = parser.parse_args()

    # Setup logging early so that warnings/errors during argument parsing use the proper format
    setup_logging(args.verbose)

    # Parse inputs
    initial_inputs = {}

    # Load inputs from file if provided
    if args.inputs_file:
        import json
        import sys
        file_ext = args.inputs_file.split('.')[-1].lower()
        try:
            if file_ext in ['yaml', 'yml']:
                file_inputs = load_yaml(args.inputs_file)
                if file_inputs is None:
                    sys.exit(1) # load_yaml already logs the error
                initial_inputs.update(file_inputs)
            elif file_ext == 'json':
                with open(args.inputs_file, 'r') as f:
                    initial_inputs.update(json.load(f))
            else:
                logger.error(f"Unsupported inputs file extension '{file_ext}'. Expected .yaml, .yml, or .json")
                sys.exit(1)
        except Exception as e:
            logger.error(f"Failed to load inputs file {args.inputs_file}: {e}")
            sys.exit(1)

    # Parse inputs from command line (overrides file inputs if any)
    if args.input:
        logger.warning("Warning: Using -i/--input for workflow inputs. Avoid passing sensitive secrets via command-line arguments.")
        for item in args.input:
            if '=' in item:
                key, value = item.split('=', 1)
                initial_inputs[key] = value
            else:
                logger.warning(f"Invalid input format: {item}. Expected key=value")

    final_state = run_workflow(args.workflow_file, initial_inputs, verbose=args.verbose)

    if final_state:
        logger.info("\n===== Simulation Finished =====")
        workflow_data = load_yaml(args.workflow_file)
        final_output_step_id = workflow_data.get('steps', [{}])[-1].get('step_id')
        if final_output_step_id:
            final_output = final_state['steps'][final_output_step_id]['output']
            logger.info("Final workflow output:")
            print(final_output) # Print final output to stdout regardless of logging level

if __name__ == "__main__":
    main()
