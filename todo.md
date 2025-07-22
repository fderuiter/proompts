# Repository Improvement Tasks

Below is a list of improvements and tooling ideas that could help maintain and scale the repository.

1. **Add a `.gitignore` file** – Prevent accidental commits of temporary build files.
1. **Create a `CONTRIBUTING.md` guide** – Summarize the workflow from `AGENTS.md` so contributors know to sanitize, standardize, and run validation scripts before opening PRs.
1. **Include explicit setup and validation instructions in the README** – Document how to run `scripts/validate_markdown.sh` and install its dependencies.
1. **Provide issue and pull-request templates** – Ensure consistent bug reports and prompt submissions by adding templates under `.github/`.
1. **Add a pre-commit configuration** – Automate `scripts/validate_markdown.sh` and `scripts/check_prompts.py`.
1. **Implement front-matter validation** – Create a script to verify required fields and detect duplicate IDs across prompts.
1. **Automatically update the documentation index** – Extend `scripts/update_docs_index.py` or use a Git hook so `docs/index.md` stays synchronized.
1. **Introduce search or catalog tooling** – Provide a CLI or web page that searches titles and tags within the prompts.
1. **Expand or refine categories** – Add new directories for missing subject areas and generate `overview.md` for each new folder.
1. **Track repository changes** – Add a `CHANGELOG.md` summarizing updates and link it from the README.
1. **Add automated `last_modified` updates** – Script changes to adjust the `last_modified` field whenever a prompt changes.
1. **Enhance documentation** – Offer usage examples or best practices for prompts, expanding on the brief “Prompt Tools” overview.
