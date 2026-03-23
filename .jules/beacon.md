# Beacon's Journal

## Core Principles
- **Documentation is UI**: Treat documentation as a first-class product.
- **Time to Understanding**: Optimize for new developers to understand the codebase quickly.
- **Consistency**: Enforce standard formats to build trust.
- **What-Why-How**: Every document should explain what it is, why it exists, and how to use it.

## Learnings
- Prompts use a strict YAML schema.
- Validation scripts are critical (`scripts/validate_prompts.sh`).
- Workflows chain prompts together.
- Documentation generation is automated and verified by `scripts/validate_prompts.sh`.
- The validation script `check_prompts.py` historically neglected checking for `overview.md` files in the `workflows/` directory. Added checking and generation logic for `overview.md` in `workflows/` directories to prevent documentation debt and ensure uniform repository structure.
