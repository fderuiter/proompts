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
