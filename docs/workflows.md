# Prompt Workflows

This repository includes a feature to chain multiple prompts together into a single, executable workflow. This allows you to build more complex, multi-step processes from the individual prompts in the library.

Workflows are defined in `.workflow.yaml` files and are stored in the `workflows/` directory.

## How it Works

A workflow consists of a series of steps, where each step executes a single prompt. The system allows you to map the output of one prompt to the input of a subsequent prompt, creating a data pipeline.

Workflows are executed using the `run_workflow.py` script.

## Workflow Schema

Workflow files (`.workflow.yaml`) have a clear and defined structure. For a detailed explanation of the schema, including all available fields and examples, please see the [Workflow Schema Documentation](</workflows/schema.md).

## Running a Workflow

To execute a workflow, use the `scripts/run_workflow.py` script from the root of the repository.

### Basic Usage

The script requires a single argument: the path to the workflow file you want to run.

```bash
python3 scripts/run_workflow.py path/to/your/workflow.workflow.yaml
```

### Providing Inputs

Most workflows require initial inputs to get started. You can provide these using the `-i` or `--input` flag. The format is `key='value'`.

For example, the `agentic_coding.workflow.yaml` requires a `product_concept` as input:

```bash
python3 scripts/run_workflow.py workflows/agentic_coding.workflow.yaml -i product_concept="A mobile app for identifying plants from photos."
```

You can provide multiple inputs by using the flag multiple times:

```bash
python3 scripts/run_workflow.py path/to/workflow.yaml -i input1="value1" -i input2="value2"
```

### How Execution is Simulated

Since the script cannot make live calls to an AI model, the execution of each prompt is **simulated**. Here's what happens at each step:

1.  **Input Resolution**: The script calculates the inputs for the current prompt based on the `map_inputs` section of the workflow step.
2.  **Variable Substitution**: The resolved inputs are substituted into the `{{variable}}` placeholders in the prompt's messages.
3.  **Simulated Output**: To generate an output for the step, the script first looks for a `testData` section in the `.prompt.yaml` file.
    - If `testData` is present, it uses the `expected` output from a test case (preferably one that matches the current inputs).
    - If no `testData` is available, a generic placeholder output is generated.
4.  **State Update**: The simulated output is saved and can be referenced by subsequent steps in the workflow.

This simulation allows you to test the logic and data flow of your workflow without needing API keys or incurring costs.
