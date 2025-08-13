# proompts

[![Deploy Jekyll site](https://github.com/fderuiter/proompts/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/deploy-pages.yml)

[![Generate Overviews](https://github.com/fderuiter/proompts/actions/workflows/generate-overviews.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/generate-overviews.yml)

[![JSON Validation](https://github.com/fderuiter/proompts/actions/workflows/json-validation.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/json-validation.yml)

[![Repository Checks](https://github.com/fderuiter/proompts/actions/workflows/repo-checks.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/repo-checks.yml)

[![Update Docs Index](https://github.com/fderuiter/proompts/actions/workflows/update-docs.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/update-docs.yml)
[![Fix Markdown Issues](https://github.com/fderuiter/proompts/actions/workflows/fix-markdown-issues.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/fix-markdown-issues.yml)

A curated set of Markdown prompts for AI-assisted product development, regulatory workflows, and general operations. Prompts are organized by topic—ranging from code reviews to market research—so you can mix and match them in your own agentic workflows.

## Docs

- **`docs/`** – additional docs and a full [table of contents](docs/index.md)

## Prompt Schema

Prompts are stored as `.json` files that conform to `docs/prompt_schema.json`. Each
file contains these top-level fields:

- `id` – unique kebab-case identifier
- `title` – short descriptive title
- `category` – directory or topical grouping
- `author` – optional author attribution
- `created` – date added (`YYYY-MM-DD`)
- `last_modified` – most recent modification date
- `tested_model` – optional model/version used when testing
- `temperature` – optional sampling temperature
- `tags` – optional array of keywords
- `prompt` – object holding the prompt text

The `prompt` object must include `purpose`, `context`, `instructions`, `inputs`,
and `output_format`. Optional keys are `additional_notes`, `example_usage`, and
`references`. See `docs/template_prompt.json` for a filled-out example.

The body of the prompt mirrors the template in
`prompt_tools/L5_standardize-prompt-files.md` with sections for `Purpose`,
`Context`, `Instructions`, `Inputs`, `Output Format`, `Additional Notes`,
`Example Usage`, and `References`.

## Validation

Run the helper script to verify JSON formatting and the docs index before committing:

```bash
./scripts/validate_json.sh
```

The script requires `jq` and Python 3. It checks that
`docs/index.md` and `docs/table-of-contents.md` are current and then runs `jq`
against every `*.json` file. The same check runs in GitHub Actions.
This repository also runs workflows to generate missing `overview.md` files, verify file naming, and commit the docs index when it changes.

## Contributing

1. Create prompts as `.json` files that follow [`docs/prompt_schema.json`](docs/prompt_schema.json) and place them in the appropriate folder.
1. Before committing, sanitize and standardize the file using `prompt_tools/L5_prompt_sanitiser.md` and `prompt_tools/L5_standardize-prompt-files.md`.
1. Run `scripts/validate_json.sh` to verify JSON formatting and update the docs index.
1. Optionally, run `prompt_tools/01_architecture_review_pipeline.md` to audit the repository.
1. If you create a new directory, an `overview.md` will be generated automatically by the workflow.
1. The same validation runs in CI, but running `scripts/validate_json.sh` locally helps catch issues early.

## License

This project is licensed under the [Proompts Personal Use License](LICENSE.md).
Individuals may freely use, modify, and distribute the prompts for personal,
non-commercial purposes. Commercial entities must obtain written permission
from Frederick de Ruiter before using the material.
