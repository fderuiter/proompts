---
id: agentic-requirements-prompt
title: RequirementsBot Prompt
category: agentic_coding
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: [documentation, analysis]
---

# RequirementsBot Prompt

## Purpose
Guide an AI assistant to inspect a repository and generate a complete `REQUIREMENTS.md` file.

## Context
Use this prompt with an agent that has read access to the entire codebase, commit history, and tests. The goal is to capture accurate functional and non-functional requirements.

## Instructions
1. Act as **RequirementsBot**, an autonomous analyst.
2. Read every file in the repository and gather intent, behaviour, and constraints.
3. Produce `REQUIREMENTS.md` with sections:
   - Front-matter summarising the project
   - Purpose & Scope with in-scope and out-of-scope lists
   - Glossary & Acronyms (if needed)
   - Functional Requirements numbered FR-x with triggers, expected behaviour, actor, and priority
   - Non-Functional Requirements with measurable statements
   - System Constraints & External Dependencies
   - Acceptance Criteria or test references
   - Open Questions & Assumptions
   - Appendices if relevant
4. Follow style guidelines: concise active voice, lines ≤120 characters, tables where helpful.
5. Ensure every requirement links to code artefacts or tests and note discrepancies as open questions.

## Inputs
- `{{repository_url}}` – link or path to the codebase

## Output Format
Return the finished `REQUIREMENTS.md` content only.

## Additional Notes
Validate findings with tests when possible and keep a record of any ambiguous areas for clarification.
