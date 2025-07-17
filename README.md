# proompts

[![Markdown Validation](https://github.com/fderuiter/proompts/actions/workflows/markdown-validation.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/markdown-validation.yml)

A curated set of Markdown prompts for AI-assisted product development, regulatory workflows, and general operations. Prompts are organized by topic—ranging from code reviews to market research—so you can mix and match them in your own agentic workflows.

## Repository structure

- **`agentic_coding/`** – guides for planning, implementing and reviewing code
- **`architecture_review/`** – prompts for analyzing system architecture
- **`biological_safety_prompts/`** – biological risk assessment and planning
- **`biosafety_prompts/`** – general biosafety support
- **`biostatistics_prompts/`** – statistical analysis and peer review tools
- **`clinical_prompts/`** – clinical data and CDASH guidance
- **`codebase_analysis/`** – checklists for evaluating code quality
- **`codex_prompts/`** – Codex/ChatGPT oriented scaffolding prompts
- **`communication_prompts/`** – summarization and presentation aids
- **`data_management_prompts/`** – data cleansing and architecture templates
- **`design_prompts/`** – documentation and design templates
- **`executive_prompts/`** – strategic and crisis management prompts
- **`glp_prompts/`** – good laboratory practice templates
- **`leadership_prompts/`** – leadership coaching and culture reflections
- **`market_research_prompts/`** – market and user research helpers
- **`meta_prompts/`** – templates that help you craft or refine other prompts
- **`operations_prompts/`** – process diagnostics and KPI tracking
- **`project_management/`** – charters, risk registers, and status reports
- **`protocol_prompts/`** – SOP and protocol creation aids
- **`regulatory_prompts/`** – compliance and regulatory planning resources
- **`regulatory_quality_prompts/`** – monitoring and quality improvement
- **`starter_pack/`** – quick-start templates for new projects
- **`testing_prompts/`** – instructions for creating thorough test plans
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

This project is licensed under the [Proompts Personal Use License](LICENSE.md).
Individuals may freely use, modify, and distribute the prompts for personal,
non-commercial purposes. Commercial entities must obtain written permission
from Frederick de Ruiter before using the material.
