# proompts

[![Update Docs Index](https://github.com/fderuiter/proompts/actions/workflows/update-docs.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/update-docs.yml)
[![Markdown Validation](https://github.com/fderuiter/proompts/actions/workflows/markdown-validation.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/markdown-validation.yml)
[![Deploy Jekyll site](https://github.com/fderuiter/proompts/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/fderuiter/proompts/actions/workflows/deploy-pages.yml)

A curated set of Markdown prompts for AI-assisted product development, regulatory workflows, and general operations. Prompts are organized by topic—ranging from code reviews to market research—so you can mix and match them in your own agentic workflows.

## Repository structure

- **`adjudication_prompts/`** – clinical endpoint adjudication resources
- **`agentic_coding/`** – guides for planning, implementing and reviewing code
- **`architecture_review/`** – prompts for analyzing system architecture
- **`biological_safety_prompts/`** – biological risk assessment and planning
- **`biosafety_prompts/`** – general biosafety support
- **`bioskills_prompts/`** – hands-on device training prompts
- **`biostatistics_prompts/`** – statistical analysis and peer review tools
- **`business_development_prompts/`** – opportunity scans and proposals
- **`cfo_prompts/`** – financial forecasting and pricing optimization
- **`chemical_characterization_prompts/`** – chemical risk assessment templates
- **`clinical_data_prompts/`** – data management and discrepancy detection
- **`clinical_monitoring_prompts/`** – monitoring dashboards and CAPA plans
- **`clinical_prompts/`** – clinical data and CDASH guidance
- **`clinical_research_manager_prompts/`** – recruitment and regulatory updates
- **`clinical_safety_prompts/`** – adverse-event narratives and trending
- **`codebase_analysis/`** – checklists for evaluating code quality
- **`codex_prompts/`** – Codex/ChatGPT oriented scaffolding prompts
- **`communication_prompts/`** – summarization and presentation aids
- **`cra_prompts/`** – monitoring visit reports and RBM planning
- **`data_management_prompts/`** – data cleansing and architecture templates
- **`design_prompts/`** – documentation and design templates
- **`docs/`** – additional docs and a full [table of contents](docs/index.md)
- **`eclinical_integration_prompts/`** – system integration planning
- **`epro_prompts/`** – electronic patient-reported outcome workflows
- **`executive_prompts/`** – strategic and crisis management prompts
- **`glp_prompts/`** – good laboratory practice templates
- **`hr_finance_prompts/`** – workforce planning and budgeting
- **`imaging_prompts/`** – imaging charter templates and QC workflow
- **`leadership_prompts/`** – leadership coaching and culture reflections
- **`market_research_prompts/`** – market and user research helpers
- **`medical_director_prompts/`** – protocol review and RBM action plans
- **`meta_prompts/`** – templates that help you craft or refine other prompts
- **`microbiology_prompts/`** – microbiological testing guides
- **`non_glp_prompts/`** – non-GLP study planning and reporting
- **`operations_prompts/`** – process diagnostics and KPI tracking
- **`pathology_prompts/`** – pathology workflows and evaluations
- **`payment_prompts/`** – site payments and compliance
- **`project_management/`** – charters, risk registers, and status reports
- **`protocol_prompts/`** – SOP and protocol creation aids
- **`regulatory_prompts/`** – compliance and regulatory planning resources
- **`regulatory_quality_prompts/`** – monitoring and quality improvement
- **`rtsm_prompts/`** – randomization and supply management
- **`scripts/`** – helper scripts such as `validate_markdown.sh`
- **`site_acquisition_prompts/`** – site identification and engagement
- **`starter_pack/`** – quick-start templates for new projects
- **`sterility_prompts/`** – sterilization validation and risk analysis
- **`study_director_prompts/`** – GLP study protocol and reporting
- **`technical_writer_prompts/`** – CSR and investigator-brochure drafts
- **`testing_prompts/`** – instructions for creating thorough test plans
- **`trial_execution_prompts/`** – optimizing trial execution strategies
- **`vp_statistics_prompts/`** – advanced statistical guidance

## Validation

Check Markdown formatting and the docs index before committing:

```bash
./scripts/validate_markdown.sh
```

The script first runs `python3 scripts/update_docs_index.py --check` to ensure
`docs/index.md` and `docs/table-of-contents.md` are up to date, then runs `mdl`.
It requires both Python 3 and the `mdl` tool. Install the linter with
`gem install mdl` if it isn't already available. The same check runs in GitHub
Actions.
This repository also runs `.github/workflows/update-docs.yml` to automatically commit the index if it changes.

## Contributing

1. Add prompts as `.md` files in the appropriate folder.
1. Include an `overview.md` when creating a new directory.
1. Run `scripts/update_docs_index.py` to regenerate the index; the workflow will update it automatically.
1. Run the validation script above before committing.

## License

This project is licensed under the [Proompts Personal Use License](LICENSE.md).
Individuals may freely use, modify, and distribute the prompts for personal,
non-commercial purposes. Commercial entities must obtain written permission
from Frederick de Ruiter before using the material.
