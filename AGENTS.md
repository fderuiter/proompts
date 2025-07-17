# Repository Guidance for AI Agent Prompts

This repository stores a collection of AI agent prompts. Each prompt is written in Markdown and placed in one of the categories under the repository root (e.g. `agentic_coding`, `meta_prompts`). Use this file for guidelines on adding or modifying prompts.

## File Format and Layout

- **Markdown only**: Every file in this repository should have the `.md` extension and contain valid Markdown content.
- **Naming**: Follow the existing naming style in each directory. For example, prompts in `agentic_coding` use numeric prefixes (`01_product_brief.md`, `02_project_brief_epic.md`, etc.), while prompts in `meta_prompts` start with `L#_` (`L0_master-ultrameta.md`).
- **Directory placement**: Add new prompts to the most relevant directory. Create new directories when necessary, using short, lowercase names separated by underscores.

## Contributing New Prompts

1. Create a Markdown file that contains the prompt text. Begin with a level-one heading describing the prompt.
1. Verify the Markdown formatting by running `./scripts/validate_markdown.sh`.
1. Commit the new file with a concise message, e.g. `Add data ingestion prompt`.
1. Open a pull request for review.

## Validation Script

The workflow in `.github/workflows/markdown-validation.yml` runs `scripts/validate_markdown.sh` to check Markdown formatting. You can run this script locally before committing:

```bash
./scripts/validate_markdown.sh
```

Make sure the `markdownlint` tool (`mdl` command) is available. If it's missing, install it with `gem install mdl` or your package manager.
