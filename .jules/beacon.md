# Beacon's Journal

## Critical Learnings
- Prompts use YAML format and should follow a schema (`docs/template_prompt.prompt.yaml`).
- Workflows chain multiple prompts together (`.workflow.yaml`).
- Validation tools exist in `tools/scripts`.
- `generate_overviews.py` is the main tool used for generating `overview.md` files for directories containing prompts and workflows, ensuring every directory has an overview.
