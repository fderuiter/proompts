# Scripts 📜

> [!NOTE]
> **TL;DR - The Master Validator**
> Run this before every commit to ensure schemas and tests pass:
> ```bash
> ./scripts/validate_prompts.sh
> ```

## Table of Contents
- [What is this?](#what-is-this)
- [Why does it exist?](#why-does-it-exist)
- [How to use it?](#how-to-use-it)
  - [validate_prompts.sh](#validate_promptssh)
  - [apply_refactor.py](#apply_refactorpy)
- [Directory Map](#directory-map-🗺️)

## What is this?
This directory contains high-level shell wrappers and maintenance scripts for the Proompts repository. These are convenient entry points for daily repository tasks.

## Why does it exist?
While `tools/scripts/` contains granular Python tools and utilities, this `scripts/` directory exists to provide simple, top-level wrappers that developers can easily run. This reduces cognitive load by abstracting away the underlying python commands and complex arguments.

## How to use it?

### `validate_prompts.sh`
This script runs the full test suite (which delegates to `tools/scripts/test_all.py`).
**Usage:**
```bash
# From the repository root
./scripts/validate_prompts.sh
```

### `apply_refactor.py`
This Python script is a helper for restructuring prompts into standard workflow directory structures (`prompts/<category>/<workflow_name>_workflow/`).
**Usage:**
```bash
# Preview changes without moving any files (Dry Run)
python3 scripts/apply_refactor.py --dry-run

# Execute the planned file moves
python3 scripts/apply_refactor.py

# Only fix broken references inside workflow files
python3 scripts/apply_refactor.py --fix-refs
```

## Directory Map 🗺️

| Script | Type | Description |
| :--- | :--- | :--- |
| **`validate_prompts.sh`** | 🐚 Shell | **The Master Validator.** Wrapper script that runs the full test suite. |
| **`apply_refactor.py`** | 🐍 Python | **Refactoring Utility.** Helper script to restructure prompts into workflow-specific directories and fix file references. |
