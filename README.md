# proompts

[![Markdown Validation](https://github.com/fderuiter/proompts/actions/workflows/markdown-validation.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/markdown-validation.yml)

`proompts` is a curated library of reusable prompts for AI coding agents and related workflows.
Each directory contains Markdown templates you can copy into your own projects or tools.

## Directory overview

- **`agentic_coding/`** – step‑by‑step prompts for planning and coding with an AI assistant.
- **`meta_prompts/`** – templates that help you design and layer new prompts.
- **`design_prompts/`** – guidance for producing design docs and architecture diagrams.
- **`architecture_review/`** – prompts to review existing systems and suggest improvements.
- **`testing_prompts/`** – resources for building comprehensive test suites.
- **`codebase_analysis/`** – analyze a codebase for maintainability and best practices.
- **`starter_pack/`** – quick‑start prompts for new projects.
- **`codex_prompts/`** – specialized prompts for OpenAI Codex and ChatGPT.

See [docs/index.md](docs/index.md) for a complete table of contents.

## Contributing

1. Add new prompts as Markdown files (`.md`) in the appropriate directory.
1. Include an `overview.md` when creating a new folder and link it from `docs/index.md`.
1. Run `./scripts/validate_markdown.sh` to lint formatting before committing.
1. Open a pull request with a concise commit message.

Refer to [AGENTS.md](AGENTS.md) for the full checklist.

## License

This project is licensed under the [GNU Affero General Public License v3](LICENSE.md).
