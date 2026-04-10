---
title: Workflows Usage
---

# Workflows Usage Guide 🚀

The `run_workflow.py` script is a powerful tool to execute sequences of prompts dynamically. This page provides practical usage examples and details about how to run and verify your workflows.

## 🛠️ Usage Examples

The simulation engine allows you to test your workflows locally. It reads variables from user inputs and outputs mocked data based on the `testData` within the prompts.

### 1. Run a Simple Workflow

To run a workflow with a single input via the command line:

```bash
python3 tools/scripts/run_workflow.py workflows/technical/agentic_coding.workflow.yaml -i product_concept="A new time-tracking app"
```

### 2. Supply Inputs via a File

For workflows requiring many inputs, or when inputs contain sensitive data, use an input file (YAML or JSON):

```bash
# Example inputs.yaml file
# product_concept: "A secure messaging platform"
# target_audience: "Enterprise customers"

python3 tools/scripts/run_workflow.py workflows/technical/agentic_coding.workflow.yaml -f inputs.yaml
```

### 3. Run in Verbose Mode

To debug a workflow and see the exact inputs being passed to each step during execution, use the `-v` (verbose) flag:

```bash
python3 tools/scripts/run_workflow.py workflows/technical/agentic_coding.workflow.yaml -i product_concept="A new time-tracking app" -v
```

## 🔍 How it works

The `run_workflow.py` script does **NOT** make actual LLM calls. It utilizes the `testData` field found within the corresponding `.prompt.yaml` files.

If a prompt's inputs match the variables specified in a `testData` entry, the simulator will return that specific `expected` string. Otherwise, it will return the first available test output, or a generic placeholder.

**Example `testData` matching:**

```yaml
# In your 01_topic_generator.prompt.yaml file:
testData:
  - inputs:
      user_name: "Alice"
    expected: "Hello Admin Alice, welcome to the system."
```

If you start your workflow with `user_name="Alice"`, the simulator resolves it correctly and passes the "expected" string to the next step.

## 💡 Best Practices
* **Provide `testData`**: Always populate your prompts with exhaustive `testData` elements to provide reliable test scenarios.
* **Test Incrementally**: Break complex workflows into multiple independent workflows to simplify testing before chaining them.
* **Avoid Command Line Secrets**: Do not pass secrets directly via `-i`. Always rely on an inputs file (`-f`) for sensitive execution tokens.
