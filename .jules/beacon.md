# Beacon's Journal

## Critical Learnings
- Prompts use YAML format and should follow a schema (`docs/template_prompt.prompt.yaml`).
- Workflows chain multiple prompts together (`.workflow.yaml`).
- Validation tools exist in `tools/scripts`.
- `generate_overviews.py` is the main tool used for generating `overview.md` files for directories containing prompts and workflows, ensuring every directory has an overview.
# Beacon Critical Learnings

- Discovered a knowledge gap where many prompt directories lacked an `overview.md` file, which is critical for developers to understand the category's purpose. The automated solution is to use `python3 tools/scripts/generate_overviews.py` to generate directory maps for all subdirectories.
