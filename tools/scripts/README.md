# Developer Scripts & Utilities

This directory contains Python scripts for repository maintenance, validation, and workflow execution.

**TL;DR:** Run `python3 tools/scripts/test_all.py` before committing.

## Prerequisites

Before running these scripts, ensure you have the required dependencies installed:

```bash
pip install -r requirements.txt
```

## Table of Contents

1. [Validation & Testing](#validation--testing)
   - [test_all.py](#test_allpy)
   - [check_prompts.py](#check_promptspy)
   - [validate_prompt_schema.py](#validate_prompt_schemapy)
   - [test_run_workflow.py](#test_run_workflowpy)
2. [Workflow Execution](#workflow-execution)
   - [run_workflow.py](#run_workflowpy)
3. [Documentation Maintenance](#documentation-maintenance)
   - [update_docs_index.py](#update_docs_indexpy)
   - [generate_overviews.py](#generate_overviewspy)
   - [fix_markdown_issues.py](#fix_markdown_issuespy)
4. [Prompt Maintenance](#prompt-maintenance)
   - [standardize_c_prompts.py](#standardize_c_promptspy)
5. [Shared Libraries](#shared-libraries)
   - [utils.py](#utilspy)

---

## Validation & Testing

### `test_all.py`

**The Master Runner.** Runs all repository validation checks in sequence: `check_prompts`, `validate_prompt_schema`, `update_docs_index` (check mode), and `yamllint`.

**Usage:**

```bash
python3 tools/scripts/test_all.py
```

### `check_prompts.py`

Checks YAML-based prompts (`*.prompt.yaml`) for basic file naming conventions and ensures every prompt directory has an `overview.md` file.

**Usage:**

```bash
python3 tools/scripts/check_prompts.py
```

### `validate_prompt_schema.py`

Validates that prompt YAML files adhere to the strict Pydantic schema. Checks for required fields like `name`, `description`, `messages`, `testData`, and `evaluators`.

**Usage:**

```bash
# Validate all prompts
python3 tools/scripts/validate_prompt_schema.py

# Strict mode (warns about empty testData)
python3 tools/scripts/validate_prompt_schema.py --strict
```

### `test_run_workflow.py`

A functional test for the `run_workflow.py` script. It creates a temporary environment with mock prompts and workflows, runs them, and verifies the output.

**Usage:**

```bash
python3 tools/scripts/test_run_workflow.py
```

## Workflow Execution

### `run_workflow.py`

Executes a prompt workflow defined in a `.workflow.yaml` file. It resolves Jinja2 templates, runs prompt steps sequentially, and manages state.

**Usage:**

```bash
# Run a workflow with verbose output
python3 tools/scripts/run_workflow.py path/to/workflow.workflow.yaml -v

# Run with initial inputs
python3 tools/scripts/run_workflow.py path/to/workflow.workflow.yaml -i user_name="Alice"
```

## Documentation Maintenance

### `update_docs_index.py`

Scans all prompt folders to regenerate the documentation index (`docs/index.md`) and table of contents. Keeps the docs site in sync with the file system.

**Usage:**

```bash
# Update docs/index.md
python3 tools/scripts/update_docs_index.py

# Check if docs are up-to-date (for CI)
python3 tools/scripts/update_docs_index.py --check
```

### `generate_overviews.py`

Automatically creates `overview.md` files in prompt directories that are missing them. Populates the file with a list of prompts in that directory.

**Usage:**

```bash
python3 tools/scripts/generate_overviews.py
```

### `fix_markdown_issues.py`

Reads `todo_fix.md` (a list of file paths) and automatically corrects common Markdown formatting issues such as list indentation, header spacing, and trailing whitespace.

**Usage:**

```bash
# Ensure todo_fix.md exists in root, then run:
python3 tools/scripts/fix_markdown_issues.py
```

## Prompt Maintenance

### `standardize_c_prompts.py`

Enforces standard fields (`purpose`, `context`, `instructions`, etc.) on prompts within directories starting with 'c' (e.g., `prompts/communication`). Useful for bulk updates.

**Usage:**

```bash
python3 tools/scripts/standardize_c_prompts.py
```

## Shared Libraries

### `utils.py`

Contains shared constants and helper functions used by multiple scripts.

- `ROOT`: Path to the repository root.
- `PROMPTS_DIR`: Path to the `prompts/` directory.
- `load_yaml(path)`: Safely loads YAML files.
- `iter_prompt_files(root)`: Recursively yields all prompt files.

---

[Return to Documentation Index](../../docs/index.md)
