# Beacon's Journal

## Critical Learnings

1. **JSON Schema Accessibility (docs/schemas/README.md):**
   A `docs/schemas/README.md` exists and explains how to configure VS Code and JetBrains IDEs to use the generated `prompt.schema.json` and `workflow.schema.json`. However, it's deep in the directory tree and its knowledge could be more prominently referenced in the main `tools/scripts/README.md` and `docs/USAGE.md` for better onboarding.

2. **todo_fix.md Usage:**
   The `fix_markdown_issues.py` script requires a `todo_fix.md` file in the root to function, formatted specifically as a markdown list. If it does not exist, the script silently skips running. I should ensure it's either clearly documented in a "How-To" snippet or handle its missing state more gracefully if possible.

3. **"TODO" Placeholders in Scripts vs Prompts:**
   There are several literal "TODO" strings injected by scripts (like `migrate_prompts.py`) to indicate missing descriptions. These need to be cleaned up periodically by `enrich_prompts.py`. The use of `TODO.md` as an orchestrator concept is separate and well-documented inside the prompt templates.
# 💡 Beacon Journal

## Critical Learnings

### 2025-05-18: The `scripts/` vs `tools/scripts/` Confusion
- **Knowledge Gap**: The `scripts/` directory lacked clear context explaining *why* it exists alongside the similarly named `tools/scripts/` directory.
- **Action Taken**: Refactored `scripts/README.md` to use the WHAT-WHY-HOW pattern, clarifying that `scripts/` contains top-level wrappers for everyday developer usage, while `tools/scripts/` is the "Engine Room" for granular Python utilities. Added usage examples to reduce cognitive load.
