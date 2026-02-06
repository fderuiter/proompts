# Scripts Overview

This directory contains Python scripts for repository maintenance, validation, and workflow execution.

## Prerequisites

Before running these scripts, ensure you have the required dependencies installed:

```bash
pip install -r requirements.txt
```

## Table of Contents

- [Validation & Maintenance](#validation--maintenance)
  - [check_prompts.py](#check_promptspy)
  - [validate_prompt_schema.py](#validate_prompt_schemapy)
  - [test_all.py](#test_allpy)
  - [fix_markdown_issues.py](#fix_markdown_issuespy)
  - [update_docs_index.py](#update_docs_indexpy)
- [Workflow Execution](#workflow-execution)
  - [run_workflow.py](#run_workflowpy)
- [Generators & Standardizers](#generators--standardizers)
  - [generate_overviews.py](#generate_overviewspy)
  - [standardize_c_prompts.py](#standardize_c_promptspy)
- [Shared Libraries](#shared-libraries)
  - [utils.py](#utilspy)

---

## Validation & Maintenance

### [`check_prompts.py`](./check_prompts.py)

Checks YAML-based prompts (`*.prompt.yaml`) for basic syntax and naming conventions. It also ensures that every directory has an `overview.md` file.

**Usage:**

```bash
python3 tools/scripts/check_prompts.py
```

### [`validate_prompt_schema.py`](./validate_prompt_schema.py)

Validates that prompt YAML files adhere to the defined schema using Pydantic. It checks for required fields like `name`, `description`, `messages`, `testData`, and `evaluators`.

**Usage:**

```bash
python3 tools/scripts/validate_prompt_schema.py
```

### [`test_all.py`](./test_all.py)

The master runner for all repository validation checks. It runs `check_prompts.py`, `validate_prompt_schema.py`, `update_docs_index.py`, and `yamllint`.

**Usage:**

```bash
python3 tools/scripts/test_all.py
```

### [`fix_markdown_issues.py`](./fix_markdown_issues.py)

Automatically fixes common Markdown issues listed in `todo_fix.md` in the root directory. Issues include trailing spaces, header styles, and list formatting.

**Usage:**

1. Ensure `todo_fix.md` exists in the root and lists files to fix (e.g., `- ./path/to/file.md`).
2. Run the script:

```bash
python3 tools/scripts/fix_markdown_issues.py
```

### [`update_docs_index.py`](./update_docs_index.py)

Scans all prompt folders to regenerate the documentation index (`docs/index.md`) and table of contents. This ensures the documentation site remains up-to-date with the repository structure.

**Usage:**

```bash
# Update the docs
python3 tools/scripts/update_docs_index.py

# Check if docs are up-to-date (used in CI)
python3 tools/scripts/update_docs_index.py --check
```

## Workflow Execution

### [`run_workflow.py`](./run_workflow.py)

Executes a prompt workflow defined in a `.workflow.yaml` file. It resolves inputs, runs the prompt steps, and manages the workflow state.

**Usage:**

```bash
# Run a workflow with verbose output
python3 tools/scripts/run_workflow.py path/to/workflow.workflow.yaml -v

# Run with initial inputs
python3 tools/scripts/run_workflow.py path/to/workflow.workflow.yaml -i user_name="Alice"
```

## Generators & Standardizers

### [`generate_overviews.py`](./generate_overviews.py)

Scans prompt directories and automatically generates an `overview.md` file if it is missing. It lists the prompts contained in the directory.

**Usage:**

```bash
python3 tools/scripts/generate_overviews.py
```

### [`standardize_c_prompts.py`](./standardize_c_prompts.py)

Standardizes the structure of prompts in directories starting with `c` (e.g., `prompts/communication`). It ensures fields like `purpose`, `context`, and `instructions` exist in the prompt body and updates metadata.

**Usage:**

```bash
python3 tools/scripts/standardize_c_prompts.py
```

## Shared Libraries

### [`utils.py`](./utils.py)

A shared utility library used by other scripts. It provides common constants (like `ROOT` and `PROMPTS_DIR`) and helper functions (like `load_yaml` and `iter_prompt_files`).

**Usage:**

Import it in your scripts:

```python
from utils import PROMPTS_DIR, load_yaml
```
