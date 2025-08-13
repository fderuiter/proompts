# Repository Guidance for AI Agent Prompts

This repository stores a collection of AI agent prompts. Prompts are primarily
stored as YAML (`.prompt.yaml` or `.prompt.yml`) and placed in one of the
categories under the repository root (e.g. `agentic_coding`, `meta_prompts`).
Some legacy prompts remain as `.json` files for backward compatibility. Use this
file for guidelines on adding or modifying prompts.

## File Format and Layout

- **Preferred YAML**: New prompts must be stored as `.prompt.yaml` or
  `.prompt.yml` files containing valid YAML. Existing `.json` prompts may persist
  temporarily but should eventually be converted. Use Markdown strictly for
  documentation such as `README.md` or `overview.md`.
- **Markdown docs**: All documentation files—including `overview.md`, `docs/*.md`,
  and any additional guides—remain in Markdown format.
- **Naming**: Follow the existing naming style in each directory. For example,
  prompts in `agentic_coding` use numeric prefixes (`01_product_brief.prompt.yaml`,
  `02_project_brief_epic.prompt.yaml`, etc.), while prompts in `meta_prompts`
  start with `L#_` (`L0_master-ultrameta.prompt.yaml`).
- **Directory placement**: Add new prompts to the most relevant directory. Create
  new directories when necessary, using short, lowercase names separated by
  underscores.

## Prompt Structure

Each prompt file follows the structure shown in
`docs/template_prompt.prompt.yaml`. Top-level fields include:

- `name` *(string, required)* — short descriptive title.
- `description` *(string, optional)* — purpose of the prompt.
- `model` *(string, required)* — model identifier.
- `modelParameters` *(object, optional)* — model parameters such as `temperature`.
- `messages` *(array, required)* — ordered list of `role`/`content` pairs.
- `testData` *(array, optional)* — sample inputs with expected outputs.
- `evaluators` *(array, optional)* — evaluation rules.

Runtime messages should use simple `{{variable}}` placeholders where caller input
is expected.

## Contributing New Prompts

Follow these steps when adding a new prompt:

1. Create a `.prompt.yaml` file following `docs/template_prompt.prompt.yaml`.
1. Place the file in the appropriate directory (`agentic_coding`, `meta_prompts`, etc.). Create new directories if needed using short, lowercase names separated by underscores.
1. When you make a new directory, also add an `overview.md` file inside it that briefly explains the prompts in that folder.
1. Run the draft through `prompt_tools/L5_prompt_sanitiser.md`.
1. Use `prompt_tools/L5_standardize-prompt-files.md` to ensure structure and formatting are consistent.
1. For large reorganizations, follow `prompt_tools/L5_refactor-reindex-prompts.md`.
1. Optionally, run `prompt_tools/01_architecture_review_pipeline.md` for repository audits.
1. Run `scripts/update_docs_index.py` to regenerate the docs index (or rely on `.github/workflows/update-docs.yml`).
1. Verify the YAML syntax using a tool like `yamllint`.
1. Commit the new file with a concise message, e.g. `Add data ingestion prompt`.
1. Open a pull request for review.

Use a YAML linter to check prompt syntax before committing. For example:

```bash
yamllint **/*.prompt.yaml
```

Make sure the linter is available. Install it with your package manager if it's missing.
The `.github/workflows/update-docs.yml` workflow will automatically commit the docs index if it becomes out of date.

## Automation

Several GitHub Actions take care of routine maintenance tasks:

- **`generate-overviews.yml`** automatically creates an `overview.md` file in any new prompt directory and updates the docs index.
- **`repo-checks.yml`** verifies file naming conventions, ensures new prompt files use the `.prompt.yaml` extension, and checks that each directory contains `overview.md`.
- **`yaml-validation.yml`** runs a YAML linter over prompt files.
- **`update-docs.yml`** commits the documentation index if it changes.

These workflows run on every push or pull request. When contributing, you can rely on them to handle the overview generation and docs update steps for you.
