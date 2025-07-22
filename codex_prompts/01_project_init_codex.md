---
id: 01-project-init-codex
title: Project Init & Skeleton (OpenAI Codex)
category: codex_prompts
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: []
---

# Project Init & Skeleton (OpenAI Codex)

## Purpose

Spin up a brand-new repository with a minimal but runnable skeleton, plus a one-command local dev experience.

## Context

- Caller will supply language/framework, package manager and licence preferences.
- Expect a `.env.example` file with `OPENAI_API_KEY=`.
- Include a helper module (`src/openaiClient.ts` or `openai_client.py`) that wraps `openai` calls.
- Assume **GitHub** remote unless the caller overrides it.

## Instructions

<!-- markdownlint-disable MD002 -->

1. **Ask the caller** for project name, language/framework, package manager and whether it’s a monorepo.
1. Generate a folder tree, a “Hello, Codex 🚀” module, standard docs (`README.md`, `.gitignore`, etc.) and a task runner.
1. **Respond with** exact shell commands and the full text of each generated file.

## Inputs

## Output Format

## Additional Notes

- If monorepo = yes, scaffold `packages/` with tooling placeholders.
- All generated code should compile / run without extra tweaks.

## Example Usage

> Paste this prompt into ChatGPT, answer the four questions it asks, then copy the shell commands and file snippets into your editor/terminal.

## References

- [Org Directory Layout Guide](../docs/architecture/layout.md)
