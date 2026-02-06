# Scripts Overview

This directory contains Python scripts for repository maintenance, validation, and workflow execution.

## Prerequisites

Before running these scripts, ensure you have the required dependencies installed:

```bash
pip install -r requirements.txt
```

## Available Scripts

### 1. `check_prompts.py`

Checks YAML-based prompts (`*.prompt.yaml`) for basic syntax and naming conventions. It also ensures that every directory has an `overview.md` file.

**Usage:**

```bash
python3 tools/scripts/check_prompts.py
```

### 2. `validate_prompt_schema.py`

Validates that prompt YAML files adhere to the defined schema using Pydantic. It checks for required fields like `name`, `description`, `messages`, `testData`, and `evaluators`.

**Usage:**

```bash
python3 tools/scripts/validate_prompt_schema.py
```

### 3. `run_workflow.py`

Executes a prompt workflow defined in a `.workflow.yaml` file. It resolves inputs, runs the prompt steps, and manages the workflow state.

**Usage:**

```bash
# Run a workflow with verbose output
python3 tools/scripts/run_workflow.py path/to/workflow.workflow.yaml -v

# Run with initial inputs
python3 tools/scripts/run_workflow.py path/to/workflow.workflow.yaml -i user_name="Alice"
```

### 4. `update_docs_index.py`

Scans all prompt folders to regenerate the documentation index (`docs/index.md`) and table of contents. This ensures the documentation site remains up-to-date with the repository structure.

**Usage:**

```bash
# Update the docs
python3 tools/scripts/update_docs_index.py

# Check if docs are up-to-date (used in CI)
python3 tools/scripts/update_docs_index.py --check
```

### 5. `test_all.py`

The master runner for all repository validation checks. It runs `check_prompts.py`, `validate_prompt_schema.py`, `update_docs_index.py`, and `yamllint`.

**Usage:**

```bash
python3 tools/scripts/test_all.py
```
