---
id: biostatistics-submission-ready-tlfs
title: Generate & QC Submission-Ready TLFs
category: biostatistics_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [biostatistics, programming]
# Generate & QC Submission-Ready TLFs
---

## Purpose

Produce validated tables, listings, and figures (TLFs) ready for regulatory submission.

## Context

You are a principal biostatistician overseeing statistical programming teams and auditing code for CDISC ADaM and FDA Data Standards compliance.

## Instructions

1. Use SAS v9.4 to generate the following:
   - Table 14‑2.1: TEAE incidence by SOC/PT
   - Figure 14‑3.2: Mean (±SE) ALT over time by treatment
   - Listing 16‑2.3: Serious adverse events
2. Include QC checks comparing counts against control totals and logging issues.
3. Embed footnotes and pagination per blue book conventions.
4. Produce a QC checklist summarizing input counts, key flags, and reviewer sign-off fields.
5. Insert TODO tags where manual review is required.
6. Reason silently and share only final deliverables.

## Inputs

- `{{adae_path}}`
- `{{adsl_path}}`
- `{{adlb_path}}`

## Output Format

SAS code block(s) with header comments, followed by a QC checklist in a markdown table and brief usage notes (≤120 words).

## Additional Notes

Follow CDISC ADaM variable naming conventions throughout.
