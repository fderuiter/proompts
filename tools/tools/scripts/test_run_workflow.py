from __future__ import annotations

import os
import shutil
import yaml
from tools.scripts.run_workflow import run_workflow

# Define the test directory
TEST_DIR = "temp_test_workflow"

def setup_test_environment():
    """Creates a temporary directory and mock prompt/workflow files."""
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)
    os.makedirs(TEST_DIR)

    # --- Create Mock Prompt 1 ---
    prompt1_content = {
        "name": "Test Prompt 1: Greeter",
        "description": "Takes a name and says hello.",
        "messages": [{"role": "user", "content": "Hello, {{name}}!"}],
        "testData": [{
            "inputs": {"name": "World"},
            "expected": ["Hello, World!"]
        }]
    }
    with open(os.path.join(TEST_DIR, "prompt1.prompt.yaml"), 'w') as f:
        yaml.dump(prompt1_content, f)

    # --- Create Mock Prompt 2 ---
    prompt2_content = {
        "name": "Test Prompt 2: Exclamation",
        "description": "Adds an exclamation mark to a phrase.",
        "messages": [{"role": "user", "content": "Add emphasis to: {{phrase}}"}],
        "testData": [{
            "inputs": {"phrase": "Hello, World!"},
            "expected": ["Hello, World!!!"]
        }]
    }
    with open(os.path.join(TEST_DIR, "prompt2.prompt.yaml"), 'w') as f:
        yaml.dump(prompt2_content, f)

    # --- Create Mock Prompt 3 (Failing Evaluator) ---
    prompt3_content = {
        "name": "Test Prompt 3: Failing Evaluator",
        "description": "Fails evaluation intentionally.",
        "messages": [{"role": "user", "content": "Analyze: {{data}}"}],
        "testData": [{
            "inputs": {"data": "Bad Data"},
            "expected": ["Output contains forbidden word"]
        }],
        "evaluators": [
            {
                "name": "Forbidden Word Checker",
                "python": "return 'forbidden' not in output",
                "action": "terminate"
            }
        ]
    }
    with open(os.path.join(TEST_DIR, "prompt3.prompt.yaml"), 'w') as f:
        yaml.dump(prompt3_content, f)

    # --- Create Mock Prompt 4 (Redact PII) ---
    prompt4_content = {
        "name": "Test Prompt 4: Redact PII",
        "description": "Tests the global PII scanner redaction.",
        "messages": [{"role": "user", "content": "Summarize: {{info}}"}],
        "testData": [{
            "inputs": {"info": "Patient details"},
            "expected": ["Patient SSN is 123-45-6789."]
        }]
    }
    with open(os.path.join(TEST_DIR, "prompt4.prompt.yaml"), 'w') as f:
        yaml.dump(prompt4_content, f)

    # --- Create Mock Workflow ---
    workflow_content = {
        "name": "Test Workflow",
        "inputs": [{"name": "user_name"}],
        "steps": [
            {
                "step_id": "step1_greet",
                "prompt_file": os.path.join(TEST_DIR, "prompt1.prompt.yaml"),
                "map_inputs": {"name": "{{inputs.user_name}}"}
            },
            {
                "step_id": "step2_emphasize",
                "prompt_file": os.path.join(TEST_DIR, "prompt2.prompt.yaml"),
                "map_inputs": {"phrase": "{{steps.step1_greet.output}}"}
            },
            {
                "step_id": "step3_redact",
                "prompt_file": os.path.join(TEST_DIR, "prompt4.prompt.yaml"),
                "map_inputs": {"info": "Patient"}
            }
        ]
    }
    workflow_path = os.path.join(TEST_DIR, "test.workflow.yaml")
    with open(workflow_path, 'w') as f:
        yaml.dump(workflow_content, f)

    return workflow_path

def cleanup_test_environment():
    """Removes the temporary test directory."""
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)

def run_tests():
    """Sets up the environment, runs the test, and cleans up."""
    print("--- Setting up test environment ---")
    workflow_file = setup_test_environment()

    print("\n--- Running workflow test ---")
    initial_inputs = {"user_name": "World"}
    # Set verbose=False to keep the test output clean
    final_state = run_workflow(workflow_file, initial_inputs, verbose=False)

    print("\n--- Verifying results ---")
    try:
        # Check output of first step
        step1_output = final_state["steps"]["step1_greet"]["output"]
        assert step1_output == "Hello, World!", f"FAIL: Step 1 output was '{step1_output}'"
        print("PASS: Step 1 output is correct.")

        # Check output of second step
        step2_output = final_state["steps"]["step2_emphasize"]["output"]
        assert step2_output == "Hello, World!!!", f"FAIL: Step 2 output was '{step2_output}'"
        print("PASS: Step 2 output is correct.")

        # Check output of third step (redaction)
        step3_output = final_state["steps"]["step3_redact"]["output"]
        assert "123-45-6789" not in step3_output, "FAIL: PII was not redacted!"
        assert "[REDACTED]" in step3_output, "FAIL: Redaction marker missing!"
        print("PASS: Step 3 output redacted PII correctly.")

        # Test terminate action with prompt3
        print("\n--- Running failing workflow test ---")
        failing_workflow_content = {
            "name": "Failing Workflow",
            "inputs": [],
            "steps": [
                {
                    "step_id": "step1_fail",
                    "prompt_file": os.path.join(TEST_DIR, "prompt3.prompt.yaml"),
                    "map_inputs": {"data": "Bad"}
                }
            ]
        }
        failing_workflow_path = os.path.join(TEST_DIR, "fail.workflow.yaml")
        with open(failing_workflow_path, 'w') as f:
            yaml.dump(failing_workflow_content, f)

        try:
            run_workflow(failing_workflow_path, {}, verbose=False)
            assert False, "FAIL: Workflow should have terminated!"
        except Exception as e:
            assert "Evaluator failed" in str(e), f"FAIL: Unexpected exception: {e}"
            print("PASS: Failing evaluator terminated workflow correctly.")

        print("\nAll tests passed successfully!")

    except AssertionError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\n--- Cleaning up test environment ---")
        cleanup_test_environment()

if __name__ == "__main__":
    run_tests()
