import argparse
import yaml
import re
import os

def load_yaml(file_path):
    """Loads a YAML file from the given path."""
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return None
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def resolve_value(template_string, workflow_state):
    """Resolves a template string like '{{steps.step_id.output}}' from the workflow state."""
    match = re.match(r"{{(.*?)}}", template_string)
    if not match:
        return template_string # Return the original string if it's not a template

    path = match.group(1).split('.')
    value = workflow_state
    try:
        for key in path:
            if isinstance(value, list): # Handle lists of inputs/steps if needed
                # Simple implementation: find the dict with the right name/id
                value = next(item for item in value if item.get('name') == key or item.get('step_id') == key)
            else:
                value = value[key]
        return value
    except (KeyError, TypeError, StopIteration):
        print(f"Warning: Could not resolve value for template '{template_string}'")
        return None

def simulate_prompt_execution(prompt_data, inputs):
    """
    Simulates executing a prompt by substituting variables and returning a simulated output.
    """
    print("\n---")
    print(f"Executing prompt: {prompt_data.get('name', 'Untitled Prompt')}")

    # Substitute variables in messages
    for message in prompt_data.get('messages', []):
        role = message.get('role', 'user')
        content = message.get('content', '')

        # Replace all placeholders
        for key, value in inputs.items():
            content = content.replace(f"{{{{{key}}}}}", str(value))

        print(f"  [{role}]: {content[:150]}...") # Print truncated content

    # Simulate output
    # Try to find a matching test case in testData
    if prompt_data.get('testData'):
        for test_case in prompt_data['testData']:
            # A simple match: if all inputs for the test case are present in the current inputs
            if all(item in inputs.items() for item in test_case.get('inputs', {}).items()):
                print("Found matching test case. Using its expected output.")
                return test_case.get('expected', 'No expected output in test case.')[0]

        # If no match, use the first test case's output
        print("No matching test case found. Using the first available test case output.")
        return prompt_data['testData'][0].get('expected', ['Simulated output from first test case.'])[0]

    # If no testData, return a generic placeholder
    return f"[Simulated output for prompt: {prompt_data.get('name', 'Untitled Prompt')}]"


def run_workflow(workflow_file, initial_inputs, verbose=True):
    """
    Loads and runs a workflow from a given file path.
    Returns the final workflow state dictionary.
    """
    workflow_data = load_yaml(workflow_file)
    if not workflow_data:
        return None

    if verbose:
        print(f"Starting workflow: {workflow_data.get('name', 'Untitled Workflow')}")

    # Initialize workflow state
    workflow_state = {
        "inputs": initial_inputs,
        "steps": {}
    }

    # Execute each step in order
    for step in workflow_data.get('steps', []):
        step_id = step['step_id']
        prompt_file = step['prompt_file']

        if verbose:
            print(f"\n===== Running Step: {step_id} =====")

        # 1. Load the prompt file
        prompt_data = load_yaml(prompt_file)
        if not prompt_data:
            if verbose:
                print(f"Skipping step {step_id} due to missing prompt file.")
            continue

        # 2. Resolve inputs for the prompt
        prompt_inputs = {}
        for var_name, template in step.get('map_inputs', {}).items():
            prompt_inputs[var_name] = resolve_value(template, workflow_state)

        if verbose:
            print(f"Resolved prompt inputs: {prompt_inputs}")

        # 3. Simulate prompt execution
        output = simulate_prompt_execution(prompt_data, prompt_inputs)

        # 4. Store the output in the workflow state
        workflow_state['steps'][step_id] = {'output': output}
        if verbose:
            print(f"Step '{step_id}' produced output: {output[:100]}...")

    return workflow_state

def main():
    parser = argparse.ArgumentParser(description="Run a prompt workflow.")
    parser.add_argument("workflow_file", help="Path to the .workflow.yaml file.")
    parser.add_argument("-i", "--input", action='append', help="Set a workflow input, e.g., -i name='value'")

    args = parser.parse_args()

    # Parse inputs from command line
    initial_inputs = {}
    if args.input:
        for item in args.input:
            key, value = item.split('=', 1)
            initial_inputs[key] = value

    final_state = run_workflow(args.workflow_file, initial_inputs)

    if final_state:
        print("\n===== Workflow Finished =====")
        workflow_data = load_yaml(args.workflow_file)
        final_output_step_id = workflow_data.get('steps', [{}])[-1].get('step_id')
        if final_output_step_id:
            final_output = final_state['steps'][final_output_step_id]['output']
            print("Final workflow output:")
            print(final_output)

if __name__ == "__main__":
    main()
