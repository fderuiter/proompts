# Beacon's Journal: Documentation Debt Audit

**Date:** 2024-05-22
**Author:** Beacon

## Critical Learnings

- **Ambiguity in `tools/`:** The `tools/` directory contains both executable scripts (`tools/scripts/`) and meta-prompts (`tools/prompt_tools/`). This distinction is not immediately obvious to new users.
- **Missing Directory Map:** The root `README.md` lacks a comprehensive overview of the repository structure, making it harder for new contributors to navigate.
- **Inconsistent Documentation:** Some directories (e.g., `prompts/`) are well-structured, while others rely on implicit knowledge or external documentation.

## Proposed Improvements

1.  **Directory Map:** Add a "Directory Map" section to the root `README.md` to clarify the purpose of each top-level directory.
2.  **Clarify `tools/`:** Explicitly differentiate between `scripts/` (Python utilities) and `prompt_tools/` (meta-prompts) in the documentation.
3.  **Standardize `README.md`:** Ensure all directories follow a consistent `README.md` template with clear "What", "Why", and "How" sections.
