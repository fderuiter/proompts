---
id: sterility-validation-protocol-builder
title: Sterility-Validation Protocol Builder
category: sterility_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [sterility, validation]
---

# Sterility-Validation Protocol Builder

## Purpose

Draft a complete validation protocol for a single-use Class II instrument sterilized by gamma irradiation.

## Context

You are a senior sterility-assurance microbiologist.

## Instructions

- Define worst-case product configuration and family grouping approach.
- Design bioburden assessment, fractional/half-cycle verification, and VDmax method per **ISO 11137‑1:2025** and **ISO 11737‑2:2019**.
- Calculate sample sizes and acceptance criteria to meet a PNSU ≤ 10^-6.
- Map activities onto a Gantt-style timeline through Process Qualification (IQ \| OQ \| PQ).
- List all required data outputs for a **510(k) sterility section** under FDA’s 2024 guidance.

## Inputs

- `{{device_description}}` – instrument details.

## Output Format

Numbered sections: Overview, Materials, Methods, Acceptance Criteria, Timeline, and References.

## Additional Notes

- Include all equations explicitly.
- Cite each standard or guidance section by clause number.
- Think through the solution step-by-step internally and reveal only the final protocol.
