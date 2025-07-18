---
id: protocol-section-refinement
title: Protocol Section Refinement
category: protocol_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [protocol, refinement]
---

# Protocol Section Refinement

## Purpose
Improve the eligibility criteria section of an IVD performance trial protocol.

## Context
You are an experienced clinical operations lead refining a protocol targeting a specific condition.

## Instructions
1. Provide specific inclusion and exclusion rules (e.g., sample type, analyte range, comorbidities).
2. Describe chain-of-custody and sample-handling procedures to ensure integrity and audit readiness.
3. Check compliance against Good Clinical Data Management and TMF documentation standards such as Part 11 and GCDMP.

## Inputs
- `{{condition}}`
- `{{draft_section}}`

## Output Format
Revised section in Markdown with clear subsections for criteria and handling procedures.

## Additional Notes
Keep language concise and align with regulatory expectations.
