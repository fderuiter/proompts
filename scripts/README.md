# Scripts 📜

This directory contains high-level shell wrappers and maintenance scripts for the Proompts repository.

> [!NOTE]
> For more granular Python tools and utilities, check the [`tools/scripts/`](../tools/scripts/) directory.

## Directory Map 🗺️

| Script | Type | Description |
| :--- | :--- | :--- |
| **`validate_prompts.sh`** | 🐚 Shell | **The Master Validator.** Wrapper script that runs the full test suite (`tools/scripts/test_all.py`). Run this before every commit. |
| **`apply_refactor.py`** | 🐍 Python | **Refactoring Utility.** Helper script to restructure prompts into workflow-specific directories and fix file references. |

## Usage 🚀

### Validate the Repository

```bash
./scripts/validate_prompts.sh
```

### Apply Refactoring

This script is used when reorganizing prompts into the standard workflow directory structure (`prompts/<category>/<workflow_name>_workflow/`).

```bash
# Preview changes (Dry Run)
python3 scripts/apply_refactor.py --dry-run

# Apply changes (Move files)
python3 scripts/apply_refactor.py

# Fix broken references in workflow files only
python3 scripts/apply_refactor.py --fix-refs
```
