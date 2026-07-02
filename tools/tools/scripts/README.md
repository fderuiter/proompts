# Developer Scripts & Utilities 🧰

> [!NOTE]
> **TL;DR - Quickstart for Validation**
> Before committing any changes, run the master validation script from the repository root to check schemas, formatting, and update documentation:
> ```bash
> ./scripts/validate_prompts.sh
> ```

## What is this?
This directory is the "Engine Room" of the Proompts repository. It contains the core Python scripts responsible for CI/CD validation, workflow simulation, schema enforcement, and automated documentation generation.

## Why does it exist?
To maintain high standards across the prompt library. By automating schema checks and documentation generation, these scripts reduce manual overhead and prevent "Documentation Debt."

## Prerequisites

Before running these scripts, ensure you have the required dependencies installed:

```bash
pip install -r requirements.txt
```

## Available Scripts

### `check_broken_links.py`
**Purpose:** Scans Markdown files for broken internal links and missing anchors across the documentation and prompt directories.
**Usage:**
```bash
python3 tools/tools/scripts/check_broken_links.py
```

### `check_prompts.py`
**Purpose:** Performs structural and naming validation on the `prompts/` and `workflows/` directories to ensure repository consistency. Enforces that prompts follow required naming patterns and that every directory has documentation.
**Usage:**
```bash
python3 tools/tools/scripts/check_prompts.py
```

### `enrich_prompts.py`
**Purpose:** Scans prompt YAML files and automatically enriches them with missing metadata (such as `domain`, `complexity`, `tags`, and `requires_context`) and inferential descriptions for variables declared in the `messages` block.
**Usage:**
```bash
python3 tools/tools/scripts/enrich_prompts.py
```

### `fix_markdown_issues.py`
**Purpose:** Automatically resolves common Markdown formatting issues (like trailing spaces, missing blank lines, and malformed code blocks) for files listed in an external manifest.
> [!WARNING]
> **Manual Setup Required:**
> This script relies on a non-existent external manifest file named `todo_fix.md` in the repository root. You must manually create this file and populate it with a bulleted list of file paths (e.g., `- ./docs/README.md`) before running this script.

**Usage:**
```bash
python3 tools/tools/scripts/fix_markdown_issues.py
```

### `generate_docs.py`
**Purpose:** Generates the static Markdown documentation site structure in the `docs/` directory. Scans all prompts and workflows, organizes them by category, and builds category index pages and individual workflow pages.
**Usage:**
```bash
python3 tools/tools/scripts/generate_docs.py
```

### `generate_overviews.py`
**Purpose:** Automatically creates `overview.md` files for prompt directories if they are missing.
**Usage:**
```bash
python3 tools/tools/scripts/generate_overviews.py
```

### `generate_regulatory_prompts.py`
**Purpose:** Generates regulatory prompts based on a predefined list of tasks, creating prompt files in the appropriate directories under `prompts/regulatory/`.
**Usage:**
```bash
python3 tools/tools/scripts/generate_regulatory_prompts.py
```

### `generate_search_index.py`
**Purpose:** Generates a `search.json` index file for the static documentation site, extracting titles, descriptions, and tags from YAML files.
**Usage:**
```bash
python3 tools/tools/scripts/generate_search_index.py
```

### `governance_manifest_generator.py`
**Purpose:** Updates the baseline governance manifest and generates gap reports based on the regulatory knowledge base (`regulatory_kb.yaml`).
**Usage:**
```bash
python3 tools/tools/scripts/governance_manifest_generator.py
```

### `inject_test_data.py`
**Purpose:** Scans all `.workflow.yaml` files and automatically injects a boilerplate `testData` array if it is missing, based on the input variables detected in the workflow steps.
> [!WARNING]
> **Manual Setup Required:**
> This script currently hardcodes the target path as `/app/workflows/`, which is not a standard repository directory unless you are running inside a specific container structure. You must manually ensure this path exists or modify the script locally before execution.

**Usage:**
```bash
python3 tools/tools/scripts/inject_test_data.py
```

---

[Return to Documentation Index](../../docs/index.md)
