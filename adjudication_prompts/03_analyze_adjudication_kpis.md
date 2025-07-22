---
id: adjudication-analyze-kpis
title: Analyze Adjudication KPIs
category: adjudication_prompts
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: [adjudication, analytics]
---

# Analyze Adjudication KPIs

## Purpose

Calculate adjudication performance metrics and recommend improvements.

## Context

- CSV file `adjudication_log.csv` lists all events in an oncology trial.
- Leadership expects a plan to reduce median cycle time by 20%.

## Instructions

1. Load the CSV and compute:
   - median and 90th percentile cycle time from event trigger to final decision
   - reviewer disagreement rate
   - top three root causes of delays inferred from status fields
1. Create bar charts for each metric and save them as PNGs.
1. Recommend at least five concrete process changes tied to these metrics that would achieve the target reduction.

## Inputs

- `{{adjudication_log.csv}}` – event log export

## Output Format

- **Metrics Summary Table**
- Embedded charts or download links for each PNG
- Bullet list of recommendations

## Additional Notes

Request a data dictionary if any column in the CSV is ambiguous before starting the analysis.
