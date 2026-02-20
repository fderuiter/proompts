# Shell Wrappers & Helper Scripts 🐚

This directory contains convenience scripts and standalone tools for repository maintenance.

> [!NOTE]
> For the core Python automation suite (e.g., `generate_docs.py`, `validate_prompt_schema.py`), see [`tools/scripts/`](../tools/scripts/README.md).

## 🗺️ Directory Map

| Script | Type | Description |
| :--- | :--- | :--- |
| **`validate_prompts.sh`** | Bash | **Validation Wrapper.** Runs the full test suite (`tools/scripts/test_all.py`). Use this before committing. |
| **`apply_refactor.py`** | Python | **Refactoring Tool.** Analyzing workflow usage and reorganizing prompt files into dedicated directories. |

## 🚀 Usage

### `validate_prompts.sh`

Run this script to ensure your changes are valid. It checks YAML syntax, prompt schema compliance, and documentation integrity.

```bash
# Run from repository root
./scripts/validate_prompts.sh
```

### `apply_refactor.py`

Use this tool when you need to restructure the prompt library, specifically to move prompts into workflow-specific subfolders.

```bash
# Preview changes (Dry Run)
python3 scripts/apply_refactor.py --dry-run

# Apply changes (Move files and create directories)
python3 scripts/apply_refactor.py

# Fix broken references in workflow files (after moving)
python3 scripts/apply_refactor.py --fix-refs
```

**How it works:**
1.  **Analyzes Workflows:** Scans `workflows/` to find which prompts are used where.
2.  **Plans Moves:** Suggests moving prompts into `prompts/CATEGORY/WORKFLOW_NAME_workflow/`.
3.  **Renames:** Sequentially numbers files (e.g., `01_prompt.yaml`) based on workflow step order.
4.  **Fixes References:** Updates the `.workflow.yaml` files to point to the new paths.
