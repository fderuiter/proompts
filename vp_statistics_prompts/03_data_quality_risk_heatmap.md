---
id: vp-data-quality-heatmap
title: Data-Quality Risk Heat Map
category: vp_statistics_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [data quality, risk]
---

# Data-Quality Risk Heat Map

## Purpose

Assess site-level data quality and recommend mitigation actions.

## Context

You are a clinical-data quality auditor specializing in risk-based monitoring. Inputs include:

- `{{raw_eds_dump}}` – patient-level dataset
- `{{query_log}}` – open and closed queries

## Instructions

1. Confirm dataset shapes and key columns.
1. Declare the risk-score formula and compute scores (0–100) for each site using:
   - Query burden per subject
   - Major protocol deviations per visit
   - Timeliness of data entry (Δ DBL)
1. Show a table of the top ten high-risk sites with driver metrics.
1. Generate an ASCII heat map (rows = sites, columns = risk deciles).
1. Recommend three specific mitigations for each high-risk site.
1. Include the Python (pandas) code used for calculations.
1. Ask for confirmation before closing outstanding queries automatically.
1. Keep total output under 800 words.

## Inputs

- `{{raw_eds_dump}}`
- `{{query_log}}`

## Output Format

Risk table → heat map → mitigation bullets.

## Additional Notes

Ensure summaries are reproducible.
