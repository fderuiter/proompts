---
id: 02-tooling-and-quality-codex
title: Tooling, Linting & Quality Gates (OpenAI Codex)
category: codex_prompts
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: []
---

# Tooling, Linting & Quality Gates (OpenAI Codex)

## Purpose

Add opinionated linters, formatters, type-checkers, commit hooks, and test frameworks so the repo “fails fast” on bad code.

## Context

- A repository already exists (created via `project-init.codex.prompt.md`).
- The primary language(s) were specified by the caller.
- CI provider defaults to **GitHub Actions**.

## Instructions

1. Detect language(s) and apply tooling:
   - **JS/TS** → ESLint + Prettier, TypeScript strict, `husky` + `lint-staged`.
   - **Python** → Ruff/Flake8, Black, Mypy, pre-commit.
1. Add test framework:
   - **JS/TS** → Vitest (or Jest).
   - **Python** → Pytest with coverage ≥ 80 %.
1. Create / update config files (`.eslintrc`, `pyproject.toml`, etc.).
1. Produce a **`quality.yml` GitHub Action**: install → lint → test → upload coverage.
1. Reply with:
   - Any new or patched files (triple-back-tick blocks).
   - A short “How to run locally” snippet (`pnpm test`, `pytest -q`, …).

## Inputs

## Output Format

## Additional Notes

- Merge, don’t clobber, any existing config.
- Use the `.env.example` from step 1 to inject `OPENAI_API_KEY` in integration tests if needed.

## Example Usage

> Paste this prompt into ChatGPT from the root of your repo.
> Tell ChatGPT the primary language if it can’t infer it (for polyglot repos).

## References

- [Quality Gates Standard](../docs/quality/gates.md)
