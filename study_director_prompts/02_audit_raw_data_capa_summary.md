---
id: audit-raw-data-capa-summary
title: Audit Raw Data and Draft a CAPA Summary
category: study_director_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [quality assurance, glp]
---

# Audit Raw Data and Draft a CAPA Summary

## Purpose
Review study data for deviations and produce a corrective-action plan.

## Context
Assume the role of a GLP Quality‑Assurance auditor examining raw body‑weight and clinical‑signs data from Day 15 of dermal toxicity Study ABC.

## Instructions
1. Identify protocol deviations, data gaps, or statistical outliers that could affect study integrity.
2. For each issue, rate the potential impact (Low/Med/High) and propose a corrective‑action/preventive‑action (CAPA).
3. Draft a CAPA memo addressed to the Study Director in no more than 300 words.

## Inputs
- `{{data_csv}}` – raw study data.

## Output Format
Markdown table (Issue ID | Impact | CAPA) followed by the memo.

## Additional Notes
- Ignore trivial rounding differences.
- Cite the line numbers or record IDs inspected so the Study Director can cross‑verify.
- Think silently first; output only the table and memo.
