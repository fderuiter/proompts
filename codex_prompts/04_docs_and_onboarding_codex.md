# Documentation & Developer Onboarding (OpenAI Codex)

## Goal

Create living docs that cut time-to-first-PR and capture architectural decisions.

## Context / Background

- Repo is runnable and deployable.
- Org favours Markdown docs plus ADRs.

## Instructions

Generate / update:

1. **`README.md`**
   - Quick Start (`pnpm i && pnpm dev` / `poetry run uvicorn main:app --reload`).
   - Env-vars table (`OPENAI_API_KEY`, `OPENAI_ORG` …).
   - Architecture diagram (ASCII or Mermaid link).
   - Badges (build, test-coverage, licence).
1. **`CONTRIBUTING.md`**
   - Local setup, pre-commit, commit message style.
1. `docs/` folder
   - `architecture.md`, `troubleshooting.md`, `adr/0001-record-architecture-decisions.md`.
1. `.vscode/extensions.json` suggesting “OpenAI Code-Completion”, Docker, and ESLint plugins.

Output each file as a fenced code block.

## References

- [ADR Template](../docs/adr/template.md)

## Additional Notes

- If Codespaces or Dev Containers are desired, also scaffold `.devcontainer/`.

## Example Usage

> Paste this prompt into ChatGPT once CI/CD is in place, then review & commit the generated docs.
