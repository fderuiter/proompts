---
id: executive-summary-final-report
title: Executive Summary for Final Report
category: study_director_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [regulatory, writing]
---

# Generate an Executive Summary for the Final Report

## Purpose
Create a concise executive summary of a non-clinical study report.

## Context
You are a regulatory medical writer specializing in CTD submissions. Input includes draft report sections (Modules 4.2.3 & 4.2.5) and statistical tables for Study DEF.

## Instructions
1. Succinctly describe study design, methodology, and key findings.
2. State the NOAEL with justification referencing dose-response data.
3. Highlight deviations and their resolved impact on data integrity.
4. Provide a bullet list supporting the proposed first-in-human dose, linking to ICH M3(R2) expectations.
5. Follow CTD heading hierarchy (e.g., 4.2.3.1 Objectives…).
6. End with a 4-item checklist the Study Director must sign.
7. Keep the summary ≤800 words in clear, formal language suitable for FDA reviewers.
8. Plan internally; reveal only the finished summary.

## Inputs
- `{{draft_report_sections}}`
- `{{stat_tables}}`

## Output Format
Markdown-formatted executive summary followed by the checklist.

## Additional Notes
None
