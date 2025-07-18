---
id: audit-raw-data-capa-summary
title: Audit Raw Data and Draft CAPA Summary
category: study_director_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [GLP, audit]
---

# Audit Raw Data and Draft a CAPA Summary

## Purpose
Identify data issues and produce a corrective-action/preventive-action summary.

## Context
Assume the role of a GLP Quality-Assurance auditor. You are given raw body-weight and clinical-signs data from Day 15 of dermal toxicity Study ABC (CSV format).

## Instructions
1. Identify protocol deviations, data gaps, or statistical outliers that could affect study integrity.
2. For each issue, rate the potential impact (Low/Med/High) and propose a CAPA.
3. Draft a CAPA memo ≤300 words addressed to the Study Director.
4. Ignore trivial rounding differences.
5. Use a Markdown table (Issue ID | Impact | CAPA) followed by the memo.
6. Cite the line numbers or record IDs inspected so the Study Director can cross-verify.
7. Think silently first; output only the table and memo.

## Inputs
- `{{raw_data_csv}}` – attached data.

## Output Format
Markdown table then the memo paragraph.

## Additional Notes
None
