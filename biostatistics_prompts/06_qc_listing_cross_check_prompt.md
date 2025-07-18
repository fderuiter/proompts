---
id: biostatistics-qc-cross-check
title: QC Listing & Cross-check Prompt
category: biostatistics_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [biostatistics, qc]
# QC Listing & Cross-check Prompt
---

## Purpose

Automate a listing and QC cross-check between independent R and SAS runs.

## Context

Act as the lead programmer overseeing double-programming for safety listings.

## Instructions

1. Use **R** to extract ADCM records where `USUBJID` appears in `ADAE` with `SAEFL='Y'`; list `USUBJID`, `CMTRT`, `CMDECOD`, `CMSTDTC`, `CMENDTC`.
2. Use **SAS** to replicate the same logic independently.
3. Perform a record-level comparison keyed by `USUBJID`, `CMDECOD`, and `CMSTDTC`.
4. Return three code blocks in order: R extract, SAS extract, R comparison.
5. If differences exist, print a diff table; otherwise output “QC PASS – R and SAS identical.”
6. Provide no additional commentary.

## Inputs

- `{{dataset_paths}}` — paths to ADAE and ADCM datasets

## Output Format

Three code blocks followed by a diff table or pass message.

## Additional Notes

Use concise code and avoid extra narrative text.
