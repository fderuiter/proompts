# Beacon's Journal

## 2024-05-22: Documentation Debt in `tools/scripts`

- **Knowledge Gap**: Several scripts in `tools/scripts/` (`enrich_prompts.py`, `generate_regulatory_prompts.py`, `migrate_prompts.py`, `test_run_workflow_unit.py`, `test_validate_prompt_schema.py`) were completely undocumented.
- **Impact**: Developers might not be aware of these useful tools or how to run specific tests, leading to duplicated effort or lower quality contributions.
- **Action**: Updating `tools/scripts/README.md` to include these scripts with usage examples.
