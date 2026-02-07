# 🛠️ Scripts & Utilities

This directory contains the Python scripts used for repository maintenance, validation, and workflow execution.

## 🚀 Getting Started

Before running any script, ensure you have the required dependencies installed:

```bash
pip install -r requirements.txt
```

> [!NOTE]
> All scripts should be run from the repository root to ensuring correct path resolution.

---

## 📜 Script Catalog

### 1. `check_prompts.py`
**Purpose:** Enforces file naming conventions and directory structure.
- Checks that prompt files end in `.prompt.yaml` or `.prompt.yml`.
- Ensures every directory has an `overview.md` file.
- Verifies that `meta` and `communication` directories follow specific naming rules.

**Usage:**
```bash
python3 tools/scripts/check_prompts.py
```

### 2. `validate_prompt_schema.py`
**Purpose:** Validates the content of prompt YAML files against the strict schema.
- Checks for required fields: `name`, `description`, `messages`, `testData`, `evaluators`.
- Ensures `messages` has at least 2 items.
- Uses `pydantic` for robust validation.

**Usage:**
```bash
# Basic validation
python3 tools/scripts/validate_prompt_schema.py

# Strict mode (warns about empty testData/evaluators)
python3 tools/scripts/validate_prompt_schema.py --strict
```

### 3. `run_workflow.py`
**Purpose:** Executes multi-step Prompt Workflows defined in `.workflow.yaml` files.
- Simulates prompt execution using `testData` matching (does not call live LLMs).
- Resolves `{{ inputs.variable }}` and `{{ steps.step_id.output }}`.
- Supports Jinja2 templating.

**Usage:**
```bash
# Run a workflow with inputs
python3 tools/scripts/run_workflow.py path/to/workflow.workflow.yaml -i user_name="Alice"

# Run with verbose logging
python3 tools/scripts/run_workflow.py path/to/workflow.workflow.yaml -v
```

### 4. `update_docs_index.py`
**Purpose:** Regenerates the documentation index and table of contents.
- Scans `prompts/` for all YAML files.
- Updates `docs/index.md` and `docs/table-of-contents.md`.
- Ensures the documentation site mirrors the file structure.

**Usage:**
```bash
# Update docs
python3 tools/scripts/update_docs_index.py

# Check if docs are up-to-date (for CI)
python3 tools/scripts/update_docs_index.py --check
```

### 5. `test_all.py`
**Purpose:** The "Master Runner" for all repository checks.
- Runs `check_prompts`, `validate_prompt_schema`, `update_docs_index`, and `yamllint` in sequence.
- Used in CI/CD pipelines and pre-commit hooks.

**Usage:**
```bash
python3 tools/scripts/test_all.py
```

### 6. `fix_markdown_issues.py`
**Purpose:** Automatically fixes common Markdown formatting issues.
- Reads `todo_fix.md` for a list of files to process.
- Fixes list indentation, header spacing, and trailing whitespace.

**Usage:**
```bash
python3 tools/scripts/fix_markdown_issues.py
```

### 7. `generate_overviews.py`
**Purpose:** Auto-generates missing `overview.md` files.
- Scans prompt directories.
- Creates a basic `overview.md` listing the prompts in that folder if one doesn't exist.

**Usage:**
```bash
python3 tools/scripts/generate_overviews.py
```

### 8. `standardize_c_prompts.py`
**Purpose:** Enforces a specific schema for prompts in directories starting with "c" (e.g., `communication`).
- Adds required fields like `purpose`, `context`, `instructions`.
- Sets default values for missing fields.

**Usage:**
```bash
python3 tools/scripts/standardize_c_prompts.py
```

### 9. `test_run_workflow.py`
**Purpose:** Unit tests for `run_workflow.py`.
- Creates a temporary environment with mock prompts and workflows.
- Verifies that variable substitution and step execution work as expected.

**Usage:**
```bash
python3 tools/scripts/test_run_workflow.py
```

---

## 📚 Shared Utilities

### `utils.py`
**Purpose:** A shared library for common operations.
- `ROOT` and `PROMPTS_DIR`: Path constants.
- `load_yaml(path)`: Safely loads YAML files with error handling.
- `iter_prompt_files(root)`: Generator yielding all `.prompt.yaml` files.

**Example Usage in a Script:**
```python
from pathlib import Path
try:
    from utils import PROMPTS_DIR, load_yaml
except ImportError:
    import sys
    sys.path.append(str(Path(__file__).parent))
    from utils import PROMPTS_DIR, load_yaml

for prompt_file in PROMPTS_DIR.glob("**/*.prompt.yaml"):
    data = load_yaml(prompt_file)
    print(data.get("name"))
```
