# proompts

[![Deploy Jekyll site](https://github.com/fderuiter/proompts/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/deploy-pages.yml)
[![YAML Validation](https://github.com/fderuiter/proompts/actions/workflows/yaml-validation.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/yaml-validation.yml)
[![Repository Checks](https://github.com/fderuiter/proompts/actions/workflows/repo-checks.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/repo-checks.yml)

A curated set of prompts in YAML for AI-assisted product development, regulatory workflows, and general operations. Prompts are organized by topic—ranging from code reviews to market research—so you can mix and match them in your own agentic workflows.

## Docs

- **`docs/`** – additional docs and a full [table of contents](docs/index.md)

## Prompt Schema

Prompts are stored as `.prompt.yaml` or `.prompt.yml` files. Each prompt file
contains two sections:

- **Runtime information** – ordered `messages` with `role`/`content` pairs that
  form the actual prompt. Use `{{variable}}` placeholders for user-provided
  values.
- **Development information** – optional metadata that describes the prompt and
  how to test it.

Top-level fields available in a prompt file include:

- `name` – short human-readable title
- `description` – concise summary of what the prompt does
- `model` – model identifier
- `modelParameters` – optional model parameters such as `temperature`
- `messages` – list of system and user messages
- `testData` – example inputs with their expected outputs
- `evaluators` – rules for verifying model responses

See `docs/template_prompt.prompt.yaml` for a filled-out example.

## Prompt Workflows

In addition to individual prompts, this repository supports **Prompt Workflows**,
which chain multiple prompts together to perform complex, multi-step tasks.
Workflows are defined in `.workflow.yaml` files and can be executed with the
included runner script.

To learn more, see the [Prompt Workflows Documentation](docs/workflows.md).

## Validation

Run a YAML linter to verify formatting and keep the docs index current before
committing:

```bash
yamllint **/*.prompt.yaml
```

The linter helps ensure valid YAML syntax. The repository also runs workflows to
generate missing `overview.md` files, verify file naming, validate prompts,
and commit the docs index when it changes.

## Contributing

1. Create prompts as `.prompt.yaml` files that follow [`docs/template_prompt.prompt.yaml`](docs/template_prompt.prompt.yaml) and place them in the appropriate folder. Convert any existing `.json` prompts to YAML and remove the obsolete JSON files.
1. Before committing, sanitize and standardize the file using `tools/prompt_tools/L5_prompt_sanitiser.md` and `tools/prompt_tools/L5_standardize-prompt-files.md`.
1. Run a YAML linter to verify formatting and update the docs index.
1. Optionally, run `tools/prompt_tools/01_architecture_review_pipeline.md` to audit the repository.
1. If you create a new directory, an `overview.md` will be generated automatically by the workflow.
1. The same validation runs in CI, but running a YAML linter locally helps catch issues early.

## License

This project is licensed under the [Proompts Personal Use License](LICENSE.md).
Individuals may freely use, modify, and distribute the prompts for personal,
non-commercial purposes. Commercial entities must obtain written permission
from Frederick de Ruiter before using the material.
