---
id: biostatistics-universal-table
title: Universal Template-Table Prompt
category: biostatistics_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [biostatistics, programming]
---

# Universal Template-Table Prompt

## Purpose

Create a formatted safety table from an ADaM ADAE dataset using either R or SAS.

## Context

You are a senior clinical-trial statistical programmer proficient in CDISC ADaM, R (tidyverse/gt), and SAS 9.4.

## Instructions

1. Produce Table 14-1 “Treatment-Emergent Adverse Events by System Organ Class and Preferred Term.”
1. Use ADAE with variables `TRT01A`, `AESOC`, `AEDECOD`, and `SAFFL`.
1. Include subjects with `SAFFL='Y'`; order rows by descending `n` in the active arm.
1. Count `n` and `%` within `TRT01A` for each SOC/PT; overall row first.
1. Output code in the language specified (R or SAS).
1. Return a `gt`/PROC REPORT table ready for the CSR with footnote “Percent based on safety population (N displayed in header).”
1. Confirm understanding briefly, then emit only the code block and table.

## Inputs

- `{{language}}` — `R` or `SAS`
- `{{dataset_path}}` — path to ADAE dataset

## Output Format

Code block followed by the generated table.

## Additional Notes

Use a structured Task/Data/Rules/Output approach for reproducibility.
