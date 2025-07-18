---
id: 02-crf-quality-auditor
title: CRF Quality Auditor
category: clinical_prompts
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: []
---

# CRF Quality Auditor

## Purpose

- Evaluate against CDISC CDASH IG v2.1 and SDTM traceability.

## Context

## Instructions

- Check for: duplicated fields, ambiguous wording, inconsistent units, uncontrolled text boxes, and mis-aligned visit windows.
- For each issue, suggest a concrete fix and cite the relevant guideline section.
- Summarise the overall risk level (low / moderate / high).
- Return your findings as a two-column Markdown table with columns "Issue" and "Recommended Fix".
- Reflect step-by-step before producing the table.

## Inputs

## Output Format

## Additional Notes
