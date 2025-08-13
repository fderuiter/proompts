# JSON to YAML Migration Plan

This document outlines the tasks required to migrate existing JSON prompts to the `.prompt.yaml` format while retaining the original JSON files for reference.

Legacy JSON prompts remain in the repository for backward compatibility. Contributors
should continue to update these JSON files alongside their YAML counterparts until
the legacy format is fully phased out.

## Migration Tasks

1. **Inventory all JSON prompts**
   - Use `find . -name '*.json'` to list existing prompts.
   - Record their locations and purpose.
2. **Create YAML equivalents**
   - For each JSON prompt, create a `.prompt.yaml` file in the same directory.
   - Follow `docs/template_prompt.prompt.yaml` for the schema and naming conventions.
3. **Cross-check content**
   - Ensure each YAML version faithfully mirrors the JSON prompt's behavior and metadata.
   - Document any deviations or improvements.
4. **Update references**
   - Replace references to `.json` prompts in documentation, scripts, or workflows with the new `.prompt.yaml` versions.
   - Keep JSON files available until all consumers confirm they can use YAML.
5. **Automation updates**
   - Modify scripts and GitHub Actions to handle `.prompt.yaml` files (e.g., rename `json-validation.yml` to `yaml-validation.yml` or add YAML validation steps).
   - Ensure repository checks allow legacy `.json` files but flag new ones.
6. **Validation**
   - Run `yamllint` on new YAML files.
   - Run `scripts/validate_prompts.sh` to ensure legacy files remain valid during the transition.
7. **Documentation**
   - Update README, AGENTS, and other docs to reference YAML prompts and note the presence of legacy JSON files.
   - Provide guidance on the migration process for contributors.
8. **Final cleanup**
   - Once all stakeholders use the YAML prompts, remove obsolete JSON files and any JSON-specific tooling.
