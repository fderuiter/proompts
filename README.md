# proompts

[![Markdown Validation](https://github.com/fderuiter/proompts/actions/workflows/markdown-validation.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/markdown-validation.yml)

A curated set of Markdown prompts for AI‑assisted software development. Prompts are organized by topic—ranging from product briefs to architecture reviews—so you can mix and match them in your own agentic workflows.

## Repository structure

- **`agentic_coding/`** – guides for planning, implementing and reviewing code
- **`meta_prompts/`** – templates that help you craft or refine other prompts
- **`design_prompts/`** – documentation and design templates
- **`architecture_review/`** – prompts for analyzing system architecture
- **`testing_prompts/`** – instructions for creating thorough test plans
- **`codebase_analysis/`** – checklists for evaluating code quality
- **`codex_prompts/`** – Codex/ChatGPT oriented scaffolding prompts
- **`starter_pack/`** – quick-start templates for new projects
- **`docs/`** – additional documentation and a full [table of contents](docs/index.md)
- **`scripts/`** – helper scripts such as `validate_markdown.sh`

## Validation

Check Markdown formatting before committing:

```bash
./scripts/validate_markdown.sh
```

The script requires the `mdl` tool and is executed automatically in GitHub Actions.

## Contributing

1. Add prompts as `.md` files in the appropriate folder.
1. Include an `overview.md` when creating a new directory.
1. Update `docs/index.md` so the prompt appears in the table of contents.
1. Run the validation script above before committing.

## License

This project is licensed under the [GNU Affero General Public License v3](LICENSE.md).
