"""
run_workflow.py: The Workflow Simulation Engine

WHAT:
This script loads a `.workflow.yaml` file, parses the step execution order,
resolves inter-step variable mappings, and simulates the output of each prompt.

WHY:
It allows developers to verify the logic, input mappings, and output extraction
of complex prompt chains *without* incurring any LLM API costs or dealing with
network latency. It ensures your workflows are structurally sound before deployment.

> [!NOTE]
> This is a SIMULATION engine. It does **not** make actual API calls to OpenAI,
> Anthropic, or any other LLM provider. Instead, it deterministically returns
> the `expected` output defined in the `testData` array of the corresponding prompt file.

HOW TO USE:
Basic simulation:
    python3 tools/scripts/run_workflow.py workflows/technical/agentic_coding.workflow.yaml

With custom initial inputs:
    python3 tools/scripts/run_workflow.py path/to/workflow.workflow.yaml -i user_name="Alice"

With verbose logging (useful for debugging variable resolution):
    python3 tools/scripts/run_workflow.py path/to/workflow.workflow.yaml -v
"""

from __future__ import annotations

import argparse
import logging
import os
import re
import sys
from typing import Any, Dict, Optional

import yaml

# Configure logger
logger = logging.getLogger(__name__)

def setup_logging(verbose: bool = False) -> None:
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

from jinja2 import Undefined, StrictUndefined
from jinja2.nativetypes import NativeEnvironment
from jinja2.sandbox import SandboxedEnvironment

class KeepUndefined(Undefined):
    def __getattr__(self, name):
        return KeepUndefined(name=f"{self._undefined_name}.{name}")
        
    def __getitem__(self, key):
        return KeepUndefined(name=f"{self._undefined_name}['{key}']")
        
    def __str__(self):
        return f"{{{{ {self._undefined_name} }}}}"

class NativeSandboxedEnvironment(NativeEnvironment, SandboxedEnvironment):
    pass

_run_env = NativeSandboxedEnvironment(undefined=KeepUndefined)
_strict_run_env = NativeSandboxedEnvironment(undefined=StrictUndefined)

def safe_render(template: str, context: Dict[str, Any], strict_mode: bool = False) -> Any:
    """
    Safely renders a template string by replacing {{ variables }} with values from context.

    This uses a restricted Jinja2 SandboxedEnvironment to prevent
    arbitrary code execution while allowing variable substitution and basic expressions.

    Args:
        template: The string containing template variables (e.g., 'Hello {{ name }}').
        context: The dictionary containing available variables.
        strict_mode: If True, raises an error on undefined variables.

    Returns:
        The rendered value. If the template is exactly '{{ variable }}', it returns
        the native type of the variable. Otherwise, it returns a string.
    """
    if not isinstance(template, str) or "{{" not in template:
        return template

    env = _strict_run_env if strict_mode else _run_env

    try:
        jinja_template = env.from_string(template)
        return jinja_template.render(**context)
    except Exception as e:
        if strict_mode:
            logger.error(f"Template Resolution Failed: {e} in template '{template}'")
            raise ValueError(f"Strict Template Resolution Failed: {e}")
        logger.debug(f"Could not fully render template (vars might be missing): {e}")
        return template


def resolve_value(template_string: str, workflow_state: Dict[str, Any], strict_mode: bool = False) -> Any:
    """
    Resolves a template string like '{{steps.step_id.output}}' from the workflow state.

    This is part of the simulation engine, resolving variable mappings between steps
    without executing external code.

    Args:
        template_string: The string containing the template variable.
        workflow_state: The current state of the workflow containing inputs and steps.
        strict_mode: If True, raises an error on failure.

    Returns:
        The resolved value if the template matches, otherwise the original string.
    """
    try:
        return safe_render(template_string, workflow_state, strict_mode)
    except Exception as e:
        if strict_mode:
            raise
        logger.warning(f"Warning: Could not resolve value for template '{template_string}': {e}")
        return template_string

def generate_mock_test_cases(prompt_data: Dict[str, Any], required_vars: list, iteration: int = 0) -> list:
    name_desc = (prompt_data.get('name', '') + " " + prompt_data.get('description', '')).lower()
    
    if "garden" in name_desc:
        domain = "gardening"
    elif "regulat" in name_desc or "audit" in name_desc or "compliance" in name_desc:
        domain = "regulatory"
    elif "code" in name_desc or "program" in name_desc or "python" in name_desc:
        domain = "coding"
    elif "clinic" in name_desc or "medical" in name_desc or "health" in name_desc or "patient" in name_desc:
        domain = "clinical"
    else:
        domain = "general"

    test_cases = []
    
    content_banks = {
        "gardening": [
            ("My tomato leaves are turning yellow.", "Yellowing leaves can indicate nitrogen deficiency. Apply a balanced organic fertilizer and ensure the soil is well-draining."),
            ("When is the best time to prune roses?", "Prune your roses in late winter or early spring just as new buds begin to swell. Cut at a 45-degree angle."),
            ("How often should I water my indoor fern?", "Water your fern when the top inch of soil feels dry. Ferns love humidity, so misting the leaves regularly also helps."),
            ("What causes blossom end rot in peppers?", "Blossom end rot is typically caused by calcium deficiency and inconsistent watering. Maintain even soil moisture."),
            ("How to get rid of aphids naturally?", "You can spray aphids off with a strong stream of water or apply a mixture of water and a few drops of dish soap.")
        ],
        "regulatory": [
            ("Summarize the requirements for 21 CFR Part 11.", "Under 21 CFR Part 11, electronic records must be trustworthy, reliable, and generally equivalent to paper records. Audit trails are mandatory."),
            ("What are the core elements of ISO 13485 design controls?", "ISO 13485 requires documented procedures for design and development planning, inputs, outputs, review, verification, validation, and transfer."),
            ("What is the reporting timeframe for a serious adverse event under EU MDR?", "Under the EU MDR, a serious public health threat must be reported within 2 days, and death or unanticipated serious deterioration within 10 days."),
            ("Explain the purpose of a 510(k) submission.", "A 510(k) is a premarket submission made to the FDA to demonstrate that the device to be marketed is at least as safe and effective as a legally marketed device."),
            ("What are the documentation requirements for a CAPA?", "A CAPA must document the investigation of the nonconformity, root cause analysis, action plan, verification of effectiveness, and management review.")
        ],
        "coding": [
            ("Write a function to reverse a string in Python.", "Here is the implementation:\n```python\ndef reverse_string(s):\n    return s[::-1]\n```"),
            ("Explain the concept of RESTful APIs.", "RESTful APIs use standard HTTP methods (GET, POST, PUT, DELETE) and rely on stateless, client-server communication to manipulate resources identified by URIs."),
            ("How do I handle exceptions in Java?", "Use a try-catch block:\n```java\ntry {\n    // code that may throw an exception\n} catch (Exception e) {\n    e.printStackTrace();\n}\n```"),
            ("What is a Docker container?", "A Docker container is a lightweight, standalone, executable package that includes everything needed to run a piece of software, including the code, runtime, and system tools."),
            ("Explain the difference between Git merge and rebase.", "Git merge combines the histories of two branches by creating a new merge commit, whereas rebase rewrites the commit history by moving the base of the branch.")
        ],
        "clinical": [
            ("Patient presents with acute chest pain and shortness of breath.", "Immediate evaluation is required to rule out acute coronary syndrome or pulmonary embolism. Administer oxygen and order a 12-lead ECG and troponin levels."),
            ("What is the standard first-line treatment for uncomplicated hypertension?", "First-line treatments typically include ACE inhibitors, ARBs, calcium channel blockers, or thiazide diuretics, depending on patient-specific factors."),
            ("Analyze the following lab result: HbA1c 7.5%.", "An HbA1c of 7.5% indicates elevated blood glucose over the past 2-3 months, consistent with diabetes mellitus. Review the patient's current treatment plan and lifestyle modifications."),
            ("What are the signs of anaphylaxis?", "Signs of anaphylaxis include hives, swelling of the face or throat, difficulty breathing, rapid heartbeat, and a sudden drop in blood pressure."),
            ("Provide dosage guidelines for pediatric Amoxicillin.", "For children, the typical dosage of Amoxicillin is 20 to 40 mg/kg/day in divided doses every 8 hours, or 25 to 45 mg/kg/day in divided doses every 12 hours.")
        ],
        "general": [
            ("Analyze this performance report and provide three key takeaways.", "1. Revenue increased by 15% QoQ.\n2. Customer retention remains stable at 92%.\n3. Operational costs increased slightly due to new software licenses."),
            ("Draft a polite decline email for a vendor proposal.", "Dear [Vendor],\n\nThank you for your proposal. After careful consideration, we have decided not to move forward at this time. We will keep your information on file for future opportunities.\n\nBest regards,\n[Name]"),
            ("Summarize the main benefits of remote work.", "Remote work offers flexibility, reduces commute time, and can increase productivity. It also allows companies to hire from a global talent pool."),
            ("What is the best way to organize a project meeting?", "Set a clear agenda, invite only necessary stakeholders, keep the meeting strictly timed, and send out actionable minutes immediately afterward."),
            ("Explain the importance of cybersecurity training for employees.", "Cybersecurity training helps employees recognize phishing attempts, manage passwords securely, and understand the impact of data breaches, significantly reducing organizational risk.")
        ]
    }

    bank = content_banks[domain]
    
    for i in range(3):
        idx = (i + (iteration * 3)) % len(bank)
        input_val, expected_val = bank[idx]
        
        inputs_mock = {}
        for var in required_vars:
            inputs_mock[var] = input_val
            
        if not required_vars:
             inputs_mock = {"input_text": input_val}

        test_cases.append({
            "inputs": inputs_mock,
            "expected": [expected_val]
        })
    
    return test_cases

def simulate_prompt_execution(prompt_data: Dict[str, Any], inputs: Dict[str, Any], prompt_file: Optional[str] = None, strict_mode: bool = False) -> str:
    """
    Simulates executing a prompt by substituting variables and returning a simulated output.

    NOTE: This function does NOT call any LLM API (e.g., OpenAI). It looks for a matching
    test case in the prompt's `testData` field and returns the expected output. This allows
    for deterministic testing of workflow logic and variable passing.

    Args:
        prompt_data: The prompt data loaded from the YAML file.
        inputs: A dictionary of mapped inputs for the prompt.
        prompt_file: Optional path to the prompt file for self-healing.
        strict_mode: If True, raises an error on undefined variables.

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
            content = safe_render(content, inputs, strict_mode)
        except Exception as e:
            if strict_mode:
                raise ValueError(f"Strict Template Resolution Failed in {prompt_data.get('name')}: {e}")
            logger.warning(f"Failed to render message content: {e}")

        logger.info(f"  [{role}]: (Content hidden for security)")

    # Simulate output
    # Check if we need to heal missing test data
    if not prompt_data.get('testData'):
        logger.info(f"No testData found for {prompt_data.get('name', 'Untitled Prompt')}.")
        if not strict_mode and sys.stdout.isatty() and not os.environ.get('CI'):
            print(f"\n[Self-Healing] No testData found for '{prompt_data.get('name', 'Untitled Prompt')}'.")
            print("To ensure deterministic simulation, generating 3 realistic input/output pairs...")
            
            required_vars = list(inputs.keys())
            if not required_vars:
                required_vars = []
                for msg in prompt_data.get('messages', []):
                    matches = re.findall(r"\{\{\s*([\w\.\-]+)\s*\}\}", msg.get('content', ''))
                    required_vars.extend(matches)
                required_vars = list(set(required_vars))

            iteration = 0
            while True:
                test_cases = generate_mock_test_cases(prompt_data, required_vars, iteration)
                print("\nProposed Test Data:")
                print(yaml.dump(test_cases, sort_keys=False))
                
                choice = input("Approve (a), Reject (r), or Regenerate (g)? [a/r/g]: ").lower()
                if choice == 'a':
                    prompt_data['testData'] = test_cases
                    if prompt_file:
                        with open(prompt_file, 'w') as f:
                            yaml.dump(prompt_data, f, sort_keys=False)
                        print("[Self-Healing] Successfully updated YAML file.")
                    break
                elif choice == 'g':
                    iteration += 1
                elif choice == 'r':
                    break

    # Try to find a matching test case in testData
    if prompt_data.get('testData'):
        for test_case in prompt_data['testData']:
            # Schema Mismatch Recovery
            if 'input' in test_case and 'inputs' not in test_case and 'vars' not in test_case:
                logger.warning(f"Schema mismatch detected in {prompt_data.get('name', 'Untitled Prompt')}: 'input' key used instead of 'inputs' or 'vars'.")
                if not strict_mode and sys.stdout.isatty() and not os.environ.get('CI'):
                    print("\n[Self-Healing] Detected unmatched variable key 'input'. The standard schema requires 'inputs' or 'vars'.")
                    choice = input("Would you like to automatically heal this by mapping 'input' -> 'inputs'? (y/n): ")
                    if choice.lower() == 'y':
                        if isinstance(test_case['input'], str):
                            test_case['inputs'] = {'input': test_case.pop('input')}
                        else:
                            test_case['inputs'] = test_case.pop('input')
                        if prompt_file:
                            with open(prompt_file, 'w') as f:
                                yaml.dump(prompt_data, f, sort_keys=False)
                            print("[Self-Healing] Successfully updated YAML file.")
                    else:
                        pass
                else:
                    # In non-interactive mode, auto-heal in memory to continue simulation
                    if isinstance(test_case['input'], str):
                        test_case['inputs'] = {'input': test_case.pop('input')}
                    else:
                        test_case['inputs'] = test_case.pop('input')

            # Check if expected inputs match actual inputs
            # Support both 'vars' (common in prompts) and 'inputs'
            expected_inputs = test_case.get('vars', test_case.get('inputs', {}))
            if isinstance(expected_inputs, str):
                expected_inputs = {"input": expected_inputs}
            
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


def run_workflow(workflow_file: str, initial_inputs: Dict[str, Any], verbose: bool = True, strict_mode: bool = False) -> Optional[Dict[str, Any]]:
    """
    Loads and simulates a workflow from a given file path.

    This function orchestrates the flow of data between steps but mocks the actual
    intelligence using the `simulate_prompt_execution` function.

    Args:
        workflow_file: Path to the workflow YAML file.
        initial_inputs: Dictionary of initial inputs for the workflow.
        verbose: Whether to print detailed execution logs.
        strict_mode: If True, fail aggressively on structural issues or missing templates.

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

    # Static Validation
    defined_steps = set()
    if strict_mode and 'testData' not in workflow_data:
        logger.warning(f"Strict Mode: Workflow '{workflow_data.get('name', 'Untitled')}' is missing 'testData' field.")
        
    for step in workflow_data.get('steps', []):
        step_id = step.get('step_id')
        for var_name, template in step.get('map_inputs', {}).items():
            if isinstance(template, str):
                matches = re.findall(r'\{\{\s*steps\.([\w\-]+)\.', template)
                for match in matches:
                    if match not in defined_steps:
                        msg = f"Step ID Mismatch: Step '{step_id}' references undefined step '{match}' in mapping '{var_name}'."
                        if strict_mode:
                            logger.error(msg)
                            raise ValueError(msg)
                        else:
                            logger.warning(msg)
        if step_id:
            defined_steps.add(step_id)

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

        # Adjust relative path resolving correctly if needed
        # Assuming prompt_file is relative to the workflow file's directory or root
        if not os.path.exists(prompt_file):
             # Try relative to workflow dir
             workflow_dir = os.path.dirname(workflow_file)
             alt_prompt_file = os.path.join(workflow_dir, prompt_file)
             if os.path.exists(alt_prompt_file):
                 prompt_file = alt_prompt_file
             else:
                 # Try relative to root (assuming current working directory is root)
                 pass

        logger.info(f"\n===== Simulating Step: {step_id} =====")

        # 1. Load the prompt file
        prompt_data = load_yaml(prompt_file)
        if not prompt_data:
            logger.warning(f"Skipping step {step_id} due to missing prompt file.")
            continue

        # 2. Resolve inputs for the prompt
        prompt_inputs = {}
        for var_name, template in step.get('map_inputs', {}).items():
            prompt_inputs[var_name] = resolve_value(template, workflow_state, strict_mode)

        logger.debug(f"Resolved prompt inputs: {list(prompt_inputs.keys())}")

        # 3. Simulate prompt execution
        output = simulate_prompt_execution(prompt_data, prompt_inputs, prompt_file=prompt_file, strict_mode=strict_mode)

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
    parser.add_argument("--strict", action="store_true", help="Run in strict mode (fails on structural errors or undefined variables)")

    args = parser.parse_args()

    # Determine if we should implicitly use strict mode
    strict_mode = args.strict or os.environ.get('CI') == 'true'

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

    # If no inputs provided, try to extract them from workflow testData
    workflow_data = load_yaml(args.workflow_file)
    if not initial_inputs and workflow_data and workflow_data.get('testData'):
        logger.info(f"Using workflow-level testData for inputs.")
        # We can either run all test scenarios or just the first one. Let's run all scenarios to fully validate.
        for test_case in workflow_data['testData']:
            inputs = test_case.get('inputs', test_case.get('vars', {}))
            logger.info(f"\n[Running Workflow Test Scenario with inputs: {inputs}]")
            try:
                final_state = run_workflow(args.workflow_file, inputs, verbose=args.verbose, strict_mode=strict_mode)
                if final_state:
                    final_output_step_id = workflow_data.get('steps', [{}])[-1].get('step_id')
                    if final_output_step_id:
                        final_output = final_state['steps'][final_output_step_id]['output']
                        logger.info(f"Scenario Output:\n{final_output}")
            except Exception as e:
                logger.error(f"Workflow test scenario failed: {e}")
                sys.exit(1)
        logger.info("\n===== Simulation Finished (All Scenarios) =====")
    else:
        try:
            final_state = run_workflow(args.workflow_file, initial_inputs, verbose=args.verbose, strict_mode=strict_mode)
        except Exception as e:
            logger.error(f"Workflow simulation failed: {e}")
            sys.exit(1)

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
