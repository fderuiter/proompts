# Guidance for AI Agents on Workflows

This directory contains executable prompt chains, defined as `.workflow.yaml` files.

## Understanding Workflows

- **Purpose**: Workflows chain multiple individual prompts together to perform complex, multi-step tasks.
- **Structure**: Each `.workflow.yaml` file defines the sequence of prompts and the data flow between them. Refer to `workflows/schema.md` for the detailed structure.
- **Location**: All workflows are stored in this directory.

## Creating and Modifying Workflows

- **Create New Workflows**: To automate a sequence of tasks, define a new `.workflow.yaml` file in this directory. Ensure it follows the established schema.
- **Use Existing Prompts**: Workflows should reuse the existing `.prompt.yaml` files from other directories in the repository.
- **Test Your Workflow**: After creating or modifying a workflow, you must test it to ensure it runs correctly. Use the `scripts/run_workflow.py` script.

### Testing a Workflow

To test a workflow, run the following command from the repository root, replacing the placeholders with your workflow's information:

```bash
python3 scripts/run_workflow.py workflows/your_workflow_name.workflow.yaml -i input_name="test_value"
```

Provide all the necessary inputs for the workflow to run. Verify that the output is as expected.

## Agent Tasks

- When asked to create a new workflow, follow the guidelines above.
- When asked to run a workflow, use the `run_workflow.py` script.
- When asked to modify a workflow, ensure you test your changes before concluding your work.
