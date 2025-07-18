---
id: 04-docs-and-onboarding-codex
title: Documentation & Developer Onboarding (OpenAI Codex)
category: codex_prompts
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: []
---

# Documentation & Developer Onboarding (OpenAI Codex)

## Purpose

Create living docs that cut time-to-first-PR and capture architectural decisions.

## Context

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

## Inputs

## Output Format

## Additional Notes

- If Codespaces or Dev Containers are desired, also scaffold `.devcontainer/`.

## Example Usage

> Paste this prompt into ChatGPT once CI/CD is in place, then review & commit the generated docs.

## References

- [ADR Template](../docs/adr/template.md)
