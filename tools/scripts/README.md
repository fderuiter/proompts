# Developer Scripts & Utilities

This directory contains Python scripts for repository maintenance, validation, and workflow execution.

**TL;DR:** Run `python3 tools/scripts/test_all.py` before committing.

## Prerequisites

Before running these scripts, ensure you have the required dependencies installed:

```bash
pip install -r requirements.txt
```

## Table of Contents

- [Developer Scripts \& Utilities](#developer-scripts--utilities)
  - [Prerequisites](#prerequisites)
  - [Table of Contents](#table-of-contents)
  - [Validation \& Testing](#validation--testing)
    - [`test_all.py`](#test_allpy)
    - [`check_prompts.py`](#check_promptspy)
    - [`validate_prompt_schema.py`](#validate_prompt_schemapy)
    - [`test_run_workflow.py`](#test_run_workflowpy)
    - [`test_generate_workflow_diagrams.py`](#test_generate_workflow_diagramspy)
    - [`test_generate_overviews.py`](#test_generate_overviewspy)
    - [`test_fix_markdown_issues.py`](#test_fix_markdown_issuespy)
    - [`test_utils.py`](#test_utilspy)
  - [Workflow Execution](#workflow-execution)
    - [`run_workflow.py`](#run_workflowpy)
    - [`generate_workflow_diagrams.py`](#generate_workflow_diagramspy)
  - [Documentation Maintenance](#documentation-maintenance)
    - [`update_docs_index.py`](#update_docs_indexpy)
    - [`generate_docs.py`](#generate_docspy)
    - [`check_broken_links.py`](#check_broken_linkspy)
    - [`generate_overviews.py`](#generate_overviewspy)
    - [`generate_search_index.py`](#generate_search_indexpy)
    - [`fix_markdown_issues.py`](#fix_markdown_issuespy)
  - [Prompt Maintenance](#prompt-maintenance)
    - [`search_prompts.py`](#search_promptspy)
    - [`update_last_modified.py`](#update_last_modifiedpy)
    - [`standardize_c_prompts.py`](#standardize_c_promptspy)
  - [Shared Libraries](#shared-libraries)
    - [`utils.py`](#utilspy)

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

### `test_generate_workflow_diagrams.py`

Unit tests for `generate_workflow_diagrams.py`. Verifies that Mermaid diagrams are correctly generated from workflow definitions, covering various edge cases like missing inputs or complex dependencies.

**Usage:**

```bash
python3 tools/scripts/test_generate_workflow_diagrams.py
```

### `test_generate_overviews.py`

Unit tests for `generate_overviews.py`. Ensures that prompt titles are correctly extracted from YAML files (prioritizing `name`, then `title`, then filename fallback) and that overview files are generated properly.

**Usage:**

```bash
python3 tools/scripts/test_generate_overviews.py
```

### `test_fix_markdown_issues.py`

Unit tests for `fix_markdown_issues.py`. Verifies the logic for correcting common Markdown formatting errors, such as trailing whitespace, header spacing, and list indentation.

**Usage:**

```bash
python3 tools/scripts/test_fix_markdown_issues.py
```

### `test_utils.py`

Unit tests for `utils.py`. Ensures shared utility functions work as expected.

**Usage:**

```bash
python3 tools/scripts/test_utils.py
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

### `generate_workflow_diagrams.py`

Generates Mermaid.js flowchart diagrams for all `.workflow.yaml` files in the repository. It creates a companion `.workflow.md` file next to each workflow, visualizing the inputs, steps, and data flow between them.

**Usage:**

```bash
python3 tools/scripts/generate_workflow_diagrams.py
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

### `generate_docs.py`

Generates the static documentation site structure in `docs/`. It scans all prompts and workflows, organizes them by category (metadata-driven), and generates:
- Category index pages (e.g., `docs/clinical.md`)
- Individual workflow documentation pages in `docs/workflows/`

**Usage:**

```bash
python3 tools/scripts/generate_docs.py
```

### `check_broken_links.py`

Scans all Markdown files in `docs/` and `prompts/` for broken internal links. It validates:
- Relative file paths
- Anchors (e.g., `#section`)
- Directory links (valid if directory exists)

**Usage:**

```bash
python3 tools/scripts/check_broken_links.py
```

### `generate_overviews.py`

Automatically creates `overview.md` files in prompt directories that are missing them. Populates the file with a list of prompts in that directory.

**Usage:**

```bash
python3 tools/scripts/generate_overviews.py
```

### `generate_search_index.py`

Generates a `search.json` file in the repository root. This JSON file indexes all prompts with their titles, descriptions, and tags, enabling the search functionality on the documentation site.

**Usage:**

```bash
python3 tools/scripts/generate_search_index.py
```

### `fix_markdown_issues.py`

Reads `todo_fix.md` (a list of file paths) and automatically corrects common Markdown formatting issues such as list indentation, header spacing, and trailing whitespace.

The `todo_fix.md` file must contain a list of files to process, formatted as a markdown list where each line starts with `- ./` and ends with `.md`.

**Usage:**

```bash
# Ensure todo_fix.md exists in root, then run:
python3 tools/scripts/fix_markdown_issues.py
```

## Prompt Maintenance

### `search_prompts.py`

Searches for prompts by keyword in the `name` or `description` fields.

**Usage:**

```bash
# Search for prompts containing "review"
python3 tools/scripts/search_prompts.py review

# Show full descriptions
python3 tools/scripts/search_prompts.py "review" -v
```

### `update_last_modified.py`

Updates the `last_modified` field in the specified prompt files to the current UTC time. If the field is missing, it adds it after `name` or at the top of the file.

**Usage:**

```bash
# Update a specific file
python3 tools/scripts/update_last_modified.py prompts/my_prompt.prompt.yaml

# Update multiple files
python3 tools/scripts/update_last_modified.py prompts/*.prompt.yaml

# Check if files need updating without modifying them
python3 tools/scripts/update_last_modified.py prompts/my_prompt.prompt.yaml --check
```

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
- `iter_workflow_files(root)`: Recursively yields all workflow files.

---

[Return to Documentation Index](../../docs/index.md)
