---
id: biostatistics-sap-generator
title: Statistical Analysis Plan Generator
category: biostatistics_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [biostatistics, SAP]
# Statistical Analysis Plan Generator
---

## Purpose

Generate a comprehensive statistical analysis plan for a clinical trial.

## Context

You are an experienced biostatistics consultant. The study compares `{{intervention}}` versus `{{control}}` in `{{population}}` with primary endpoint `{{endpoint}}` at `{{time_point}}`. Randomisation is stratified by `{{factors}}`.

## Instructions

1. Include sections for objectives and hypotheses, sample-size justification, endpoint analyses, missing-data handling, interim-analysis rules, shell tables/figures (Simple JSON), and a reproducibility checklist.
2. Keep total length ≤ 1 500 words.
3. Begin each subsection with a plain-English summary.
4. List assumptions requiring sponsor confirmation.

## Inputs

- `{{intervention}}`
- `{{control}}`
- `{{population}}`
- `{{endpoint}}`
- `{{time_point}}`
- `{{factors}}`

## Output Format

Markdown document using H2 headings for each section.

## Additional Notes

Think step-by-step internally, but present only the final SAP.
