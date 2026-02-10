# proompts

[![Deploy Jekyll site](https://github.com/fderuiter/proompts/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/deploy-pages.yml)
[![YAML Validation](https://github.com/fderuiter/proompts/actions/workflows/yaml-validation.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/yaml-validation.yml)
[![Repository Checks](https://github.com/fderuiter/proompts/actions/workflows/repo-checks.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/repo-checks.yml)

A curated set of prompts in YAML for AI-assisted product development, regulatory workflows, and general operations. Prompts are organized by topic: ranging from code reviews to market research. You can mix and match them in your own agentic workflows!

## Docs

- **`docs/`** – additional docs and a full [table of contents](docs/index.md)
- **`tools/scripts/`** – [developer scripts and utilities](tools/scripts/README.md)
- **[Usage Guide](docs/USAGE.md)** – how to use the prompts

## Setup

To run validation scripts and tools locally, you need Python 3 and the required dependencies.

1.  Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the validation script to verify everything is set up correctly:
    ```bash
    ./scripts/validate_prompts.sh
    ```

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

To run all validation checks (YAML linting, schema validation, documentation index verification) locally, use the provided script:

```bash
./scripts/validate_prompts.sh
```

This script runs the following checks:
- `check_prompts`: Verifies file naming conventions and directory structure.
- `validate_prompt_schema`: Ensures prompts follow the required schema (e.g., `messages`, `testData`).
- `update_docs_index`: Checks if the documentation index is up-to-date.
- `yamllint`: Lints YAML files for formatting.

It is recommended to run this script before committing changes.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed instructions on how to contribute.

1. Create prompts as `.prompt.yaml` files that follow [`docs/template_prompt.prompt.yaml`](docs/template_prompt.prompt.yaml) and place them in the appropriate folder.
2. Review the [Best Practices Guide](docs/BEST_PRACTICES.md) for detailed guidance on creating high-quality prompts.
3. Ensure your prompt includes:
   - Meaningful `testData` with realistic examples (at least 1-2 test cases)
   - `evaluators` to validate output quality
   - Clear instructions and expected output format
4. Before committing, run validation:
   ```bash
   ./scripts/validate_prompts.sh
   ```
5. If you create a new directory, an `overview.md` will be generated automatically by the workflow.

The same validation runs in CI, but running checks locally helps catch issues early.

## License

This project is licensed under the [Proompts Personal Use License](LICENSE.md).
Individuals may freely use, modify, and distribute the prompts for personal,
non-commercial purposes. Commercial entities must obtain written permission
from Frederick de Ruiter before using the material.
