<!-- markdownlint-disable MD029 -->
---
id: agents-md-checklist
title: AGENTS.md Checklist Generator
category: meta_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [meta, documentation]
---

# AGENTS.md Checklist Generator

## Purpose

Create a best-practice checklist for writing an AGENTS.md file and provide a meta‑prompt to generate one from any repository.

## Context

You are an expert software-documentation agent.

## Instructions

1. Summarize key elements every AGENTS.md should cover: purpose, structure, coding conventions, testing workflow, execution constraints, PR guidelines and programmatic checks.
1. Provide a ready-to-use meta‑prompt that analyzes a repository at `{{repo_url}}` and outputs a compliant AGENTS.md.
1. Keep bullets concise and commands in code blocks.
1. Return only the markdown content with no commentary.

## Inputs

- `{{repo_url}}` – URL of the target repository

## Output Format

Markdown document containing the checklist and the meta‑prompt.

## Additional Notes

Mention that nested AGENTS.md files override parent rules and direct system prompts override all.
