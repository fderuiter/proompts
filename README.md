# proompts

[![Deploy Jekyll site](https://github.com/fderuiter/proompts/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/deploy-pages.yml)

[![Generate Overviews](https://github.com/fderuiter/proompts/actions/workflows/generate-overviews.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/generate-overviews.yml)

[![Markdown Validation](https://github.com/fderuiter/proompts/actions/workflows/markdown-validation.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/markdown-validation.yml)

[![Repository Checks](https://github.com/fderuiter/proompts/actions/workflows/repo-checks.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/repo-checks.yml)

[![Update Docs Index](https://github.com/fderuiter/proompts/actions/workflows/update-docs.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/update-docs.yml)
[![Fix Markdown Issues](https://github.com/fderuiter/proompts/actions/workflows/fix-markdown-issues.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/fix-markdown-issues.yml)

A curated set of Markdown prompts for AI-assisted product development, regulatory workflows, and general operations. Prompts are organized by topic—ranging from code reviews to market research—so you can mix and match them in your own agentic workflows.

## Docs

- **`docs/`** – additional docs and a full [table of contents](docs/index.md)

## Prompt Schema

Each prompt begins with YAML front matter that includes these fields:

- `id` – unique kebab-case identifier.
- `title` – short descriptive title.
- `category` – directory or topical grouping.
- `author` – optional author attribution.
- `created` – date added (`YYYY-MM-DD`).
- `last_modified` – most recent modification date.
- `tested_model` – optional model/version used when testing.
- `temperature` – optional sampling temperature.
- `tags` – optional array of keywords.

The body of the prompt follows the template in `prompt_tools/L5_standardize-prompt-files.md` with **H2** sections for `Purpose`, `Context`, `Instructions`, `Inputs`, `Output Format`, `Additional Notes`, `Example Usage`, and `References`.

You can also see the same structure in JSON form in `docs/template_prompt.json`.
The machine-readable JSON schema is available in `docs/prompt_schema.json`.

## Validation

Check Markdown formatting and the docs index before committing:

```bash
./scripts/validate_markdown.sh
```

The script first runs `python3 scripts/update_docs_index.py --check` to ensure
`docs/index.md` and `docs/table-of-contents.md` are up to date, then runs `mdl`.
It requires both Python 3 and the `mdl` tool. Install the linter with
`gem install mdl` if it isn't already available. The same check runs in GitHub Actions.
This repository also runs workflows to generate missing `overview.md` files, verify file naming, and commit the docs index when it changes.

## Contributing

1. Add prompts as `.md` files in the appropriate folder.
1. Before committing, sanitize and standardize the file using `prompt_tools/L5_prompt_sanitiser.md` and `prompt_tools/L5_standardize-prompt-files.md`.
1. Optionally, run `prompt_tools/01_architecture_review_pipeline.md` to audit the repository.
1. If you create a new directory, an `overview.md` will be generated automatically by the workflow.
1. The docs index and Markdown formatting are checked in CI, but you can run `scripts/validate_markdown.sh` locally.

## License

This project is licensed under the [Proompts Personal Use License](LICENSE.md).
Individuals may freely use, modify, and distribute the prompts for personal,
non-commercial purposes. Commercial entities must obtain written permission
from Frederick de Ruiter before using the material.
