---
id: agentic-project-review
title: Project Review Checklist
category: agentic_coding
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: [coding, review]
---

# Project Review Checklist

## Purpose
Verify completion of a coding project before finalizing.

## Context
Run this checklist at the end of a development cycle to ensure quality and documentation are complete.

## Instructions
1. Run the formatter (`dotnet format` or equivalent).
2. Execute all tests with `dotnet test` and fix failures.
3. Resolve compiler and static-analysis warnings.
4. Review changes using `git diff --name-only main`.
5. Confirm the to-do list shows all tasks complete.
6. Cross-reference `memory.md` for project state accuracy.
7. Update development guidelines with any lessons learned.

## Inputs
None

## Output Format
Markdown checklist confirming each step was completed.

## Additional Notes
Only mark the project finished when every checklist item passes.
