# 💡 Beacon Journal

## Critical Learnings

### 2025-05-18: The `scripts/` vs `tools/scripts/` Confusion
- **Knowledge Gap**: The `scripts/` directory lacked clear context explaining *why* it exists alongside the similarly named `tools/scripts/` directory.
- **Action Taken**: Refactored `scripts/README.md` to use the WHAT-WHY-HOW pattern, clarifying that `scripts/` contains top-level wrappers for everyday developer usage, while `tools/scripts/` is the "Engine Room" for granular Python utilities. Added usage examples to reduce cognitive load.