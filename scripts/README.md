# Scripts 📜

This directory contains high-level shell wrappers and maintenance scripts for the Proompts repository.

> [!NOTE]
> For more granular Python tools and utilities, check the [`tools/tools/scripts/`](../tools/tools/scripts/) directory.

## Directory Map 🗺️

| Script | Type | Description |
| :--- | :--- | :--- |
| **`validate_prompts.sh`** | 🐚 Shell | **The Master Validator.** Wrapper script that runs the full test suite using `uv run`. Run this before every commit. |

## Usage 🚀

### Validate the Repository

```bash
./scripts/validate_prompts.sh
```
