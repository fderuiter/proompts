---
id: agentic-folder-module-organization
title: Folder and Module Organization
category: agentic_coding
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: [refactoring, organization]
---

# Folder and Module Organization

## Purpose
Provide a detailed plan for restructuring a Python codebase into clearer, feature-based modules.

## Context
Use this prompt when analysing an existing project with confusing package layouts and circular dependencies.

## Instructions
1. Analyse the current package and module structure.
2. Identify opportunities for feature- or domain-based grouping and flag separation-of-concern violations.
3. Produce a step-by-step refactoring plan including:
   - pre-refactor checklist commands (`pytest`, `coverage`, `flake8` or `pylint`)
   - file migration steps with `git mv` and import updates
   - post-refactor validation commands
   - rollback guidance if a step fails
4. Offer follow-up prompts to drill into sample modules, examine cross-module dependencies, and validate scalability with a new feature stub.

## Inputs
- `{{repo_path}}` – path to the project source

## Output Format
Markdown plan detailing the checklist, migration steps, validation commands, and follow-up prompts.

## Additional Notes
Include exact shell commands where possible and highlight tools such as `import-linter` or `ruff` to enforce layering rules.
