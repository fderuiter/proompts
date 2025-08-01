# Repository Guidance for AI Agent Prompts

This repository stores a collection of AI agent prompts. Each prompt is stored as JSON and placed in one of the categories under the repository root (e.g. `agentic_coding`, `meta_prompts`). Use this file for guidelines on adding or modifying prompts.

## File Format and Layout

- **JSON only**: All prompts must be stored as `.json` files containing valid JSON. Use Markdown strictly for documentation such as `README.md` or `overview.md`.
- **Markdown docs**: All documentation files—including `overview.md`, `docs/*.md`, and any additional guides—remain in Markdown format. Do not convert these files to JSON or other formats.
- **Naming**: Follow the existing naming style in each directory. For example, prompts in `agentic_coding` use numeric prefixes (`01_product_brief.json`, `02_project_brief_epic.json`, etc.), while prompts in `meta_prompts` start with `L#_` (`L0_master-ultrameta.json`).
- **Directory placement**: Add new prompts to the most relevant directory. Create new directories when necessary, using short, lowercase names separated by underscores.

## Prompt Metadata Schema

Each prompt is stored as a JSON file. The required top-level fields are
`id`, `title`, `category`, `created`, `last_modified`, and `prompt`.
The `prompt` object itself must contain `purpose`, `context`, `instructions`,
`inputs`, and `output_format`. Optional fields are described below.
See `docs/template_prompt.json` for a complete example.

The full schema is:

- `id` *(string, required)* — unique kebab‑case identifier.
- `title` *(string, required)* — short descriptive title.
- `category` *(string, required)* — directory or topical grouping.
- `author` *(string, optional)* — original author or maintainer.
- `created` *(string, required)* — date added in `YYYY-MM-DD` format.
- `last_modified` *(string, required)* — last modification date in the same format.
- `tested_model` *(string, optional)* — model name or version used for testing.
- `temperature` *(number, optional)* — sampling temperature (0–2).
- `tags` *(array of strings, optional)* — helpful keywords.
- `prompt` *(object, required)* — contains the text of the prompt. It must include `purpose`, `context`, `instructions`, `inputs`, and `output_format`. Optional keys are `additional_notes`, `example_usage`, and `references`. See `prompt_tools/L5_standardize-prompt-files.md` for details on these sections.

For a machine-readable definition, see `docs/prompt_schema.json`. A filled-out example
that conforms to this schema is provided in `docs/template_prompt.json`.

## Contributing New Prompts

Follow these steps when adding a new prompt:

1. Create a JSON file that follows `docs/prompt_schema.json`.
1. Place the file in the appropriate directory (`agentic_coding`, `meta_prompts`, etc.). Create new directories if needed using short, lowercase names separated by underscores.
1. When you make a new directory, also add an `overview.md` file inside it that briefly explains the prompts in that folder.
1. Run the draft through `prompt_tools/L5_prompt_sanitiser.md`.
1. Use `prompt_tools/L5_standardize-prompt-files.md` to ensure JSON structure conforms to the schema.
1. For large reorganizations, follow `prompt_tools/L5_refactor-reindex-prompts.md`.
1. Optionally, run `prompt_tools/01_architecture_review_pipeline.md` for repository audits.
1. Run `scripts/update_docs_index.py` to regenerate the docs index (or rely on `.github/workflows/update-docs.yml`).
1. Verify the JSON syntax using a tool like `jq`.
1. Commit the new file with a concise message, e.g. `Add data ingestion prompt`.
1. Open a pull request for review.

The workflow in `.github/workflows/json-validation.yml` runs `scripts/validate_json.sh` to verify JSON formatting. You can run this script locally before committing:

```bash
./scripts/validate_json.sh
```

Make sure the `jq` command-line tool is available. Install it with your package manager if it's missing.
The `.github/workflows/update-docs.yml` workflow will automatically commit the docs index if it becomes out of date.

## Automation

Several GitHub Actions take care of routine maintenance tasks:

- **`generate-overviews.yml`** automatically creates an `overview.md` file in any new prompt directory and updates the docs index.
- **`repo-checks.yml`** verifies file naming conventions, ensures all prompt files use the `.json` extension, and checks that each directory contains `overview.md`.
- **`json-validation.yml`** runs `scripts/validate_json.sh`.
- **`update-docs.yml`** commits the documentation index if it changes.

These workflows run on every push or pull request. When contributing, you can rely on them to handle the overview generation and docs update steps for you.
