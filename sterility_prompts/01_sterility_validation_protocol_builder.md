---
id: sterility-validation-protocol-builder
title: Sterility-Validation Protocol Builder
category: sterility_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [sterility, protocol]
---

# Sterility-Validation Protocol Builder

## Purpose
Draft a validation test plan for a single-use Class II instrument sterilized by gamma irradiation.

## Context
You are a senior sterility-assurance microbiologist.

## Instructions
1. Define worst-case product configuration and "family" grouping approach.
2. Design bioburden assessment, fractional/half-cycle verification, and VDmax method per **ISO 11137-1 : 2025** and **ISO 11737-2 : 2019**.
3. Calculate sample sizes and acceptance criteria to meet a PNSU ≤ 10^-6.
4. Map activities onto a Gantt-style timeline through Process Qualification (IQ | OQ | PQ).
5. List all required data outputs for a **510(k) sterility section** under FDA’s 2024 guidance.
6. Write in numbered sections: Overview, Materials, Methods, Acceptance Criteria, Timeline, References.
7. Include all equations explicitly.
8. Cite each standard or guidance section by clause number.
9. Think through the solution step-by-step internally; reveal only the final protocol.

## Inputs
None

## Output Format
Numbered protocol sections in Markdown.

## Additional Notes
None
