# Project Init & Skeleton (OpenAI Codex)

<!-- markdownlint-disable MD002 -->

## Goal

Spin up a brand-new repository with a minimal but runnable skeleton, plus a one-command local dev experience.

## Context / Background

- Caller will supply language/framework, package manager and licence preferences.
- Expect a `.env.example` file with `OPENAI_API_KEY=`.
- Include a helper module (`src/openaiClient.ts` or `openai_client.py`) that wraps `openai` calls.
- Assume **GitHub** remote unless the caller overrides it.

## Instructions

1. **Ask the caller** for project name, language/framework, package manager and whether it’s a monorepo.
1. Generate a folder tree, a “Hello, Codex 🚀” module, standard docs (`README.md`, `.gitignore`, etc.) and a task runner.
1. **Respond with** exact shell commands and the full text of each generated file.

## References

- [Org Directory Layout Guide](../docs/architecture/layout.md)

## Additional Notes

- If monorepo = yes, scaffold `packages/` with tooling placeholders.
- All generated code should compile / run without extra tweaks.

## Example Usage

> Paste this prompt into ChatGPT, answer the four questions it asks, then copy the shell commands and file snippets into your editor/terminal.
