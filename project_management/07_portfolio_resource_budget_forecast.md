---
id: pm-portfolio-budget-forecast
title: Portfolio Resource and Budget Forecast
category: project_management
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [project management, forecasting]
---

# Portfolio Resource and Budget Forecast

## Purpose
Generate a rolling 12‑month FTE and budget forecast for active trials.

## Context
You are a seasoned financial-analysis AI embedded in a CRO PMO. Portfolio data includes historic burn rates and enrollment deltas for eight Phase II/III trials. Sponsor change orders increased 15 % last quarter and enrollment pace varies ±25 % versus plan.

## Instructions
1. Ingest monthly actuals and enrollment deltas.
2. Apply linear regression with ±2 σ confidence to project costs and FTEs.
3. Flag any trial expected to exceed its baseline budget by >10 %.
4. Summarize drivers such as CRA travel or lab kits.
5. Output:
   - A table named "Forecast" with Month, Trial ID, Forecast Cost, Forecast FTE, Variance %.
   - A bulleted "Key Insights" section no longer than 200 words.
   - Briefly show calculations and assumptions after the table.

## Inputs
- `{{historic_burn_rates}}`
- `{{enrollment_deltas}}`

## Output Format
Markdown table followed by bullet list and calculation notes.

## Additional Notes
Present numbers in USD and round to the nearest thousand.
