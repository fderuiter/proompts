# Beacon's Journal 💡

## Critical Learnings

### The Dual-Nature of `docs/`
- **Knowledge Gap Discovered**: New contributors might manually edit files in `docs/` like `index.md` or prompt-specific markdown pages, not realizing they will be overwritten by `tools/scripts/generate_docs.py` or `tools/scripts/update_docs_index.py`.
- **Action Taken**: Created `docs/README.md` to explicitly define the "What-Why-How" of the documentation generation pipeline and differentiate between static guides (like `USAGE.md`) and generated artifacts. A Mermaid diagram was added to visualize the flow, optimizing "Time to Understanding" for the documentation architecture.