# Nexus Journal

## 2024-05-22: The Coding Split and Broken Paths

**Observation:**
The repository contained two disparate directories for coding prompts: `prompts/technical/codex` (Tactical/Task-based) and `prompts/technical/agentic_coding` (Strategic/Lifecycle-based). This violated the MECE principle and created confusion ("The Coding Split").

Additionally, `workflows/agentic_coding.workflow.yaml` referenced files with paths like `agentic_coding/01_product_brief.prompt.yaml`, which were incorrect relative to the repository root. The actual files were in `prompts/technical/agentic_coding/`. This confirmed "Orphaned Flows" or broken references.

**Strategy:**
Merge both directories into `prompts/technical/software_engineering` with a clear stratification:
- `lifecycle/` (from `agentic_coding`): Strategic, whole-project flows.
- `tasks/` (from `codex`): Tactical, specific coding actions.

**Action:**
- Moved files to the new structure.
- Renamed `codex` files to remove redundant suffixes.
- Updated `agentic_coding.workflow.yaml` to use correct, full paths.
- Updated documentation.

## 2024-05-23: The Great Consolidation

**Observation:**
The repository suffered from "The General Dump" (`prompts/general`), containing mismatched prompts for productivity, communication, and miscellaneous tasks. This violated the semantic home principle. Also, `prompts/technical/repository_refactoring` used inconsistent naming (`Prompt_1_...`).

**Strategy:**
Dissolve `prompts/general` entirely by distributing its contents into new semantic homes:
- `prompts/communication` (New Root)
- `prompts/management/personal_effectiveness` (New)
- `prompts/management/training` (New)
- `prompts/management/innovation` (New)
- Consolidate others into existing `business`, `meta`, `regulatory`, and `technical` domains.

**Action:**
- Migrated all 25+ files from `general` to their new homes.
- Created 4 new semantic directories.
- Renamed `repository_refactoring` files to `01_` convention.
- Updated `check_prompts.py` to support the new structure.
- Regenerated documentation index.
- Eliminated `prompts/general`.

**Addendum:**
Renumbered files in new directories to resolve prefix collisions and enforce sequential ordering (e.g., `prompts/communication` re-indexed 01-20).
