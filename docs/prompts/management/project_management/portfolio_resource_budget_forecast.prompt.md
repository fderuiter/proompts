---
title: Portfolio Resource and Budget Forecast
---

# Portfolio Resource and Budget Forecast

Generate a rolling 12‑month FTE and budget forecast for active trials.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/management/project_management/portfolio_resource_budget_forecast.prompt.yaml)

```yaml
---
name: Portfolio Resource and Budget Forecast
version: 0.1.0
description: Generate a rolling 12‑month FTE and budget forecast for active trials.
metadata:
  domain: management
  complexity: medium
  tags:
  - project-management
  - portfolio
  - resource
  - budget
  - forecast
  requires_context: false
variables:
- name: enrollment_deltas
  description: The enrollment deltas to use for this prompt
  required: true
- name: historic_burn_rates
  description: '`{{enrollment_deltas}}`'
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a seasoned financial-analysis AI embedded in a CRO PMO. Portfolio data includes historic burn rates and
    enrollment deltas for eight Phase II/III trials. Sponsor change orders increased 15 % last quarter and enrollment pace
    varies ±25 % versus plan.


    Present numbers in USD and round to the nearest thousand.'
- role: user
  content: "1. Ingest monthly actuals and enrollment deltas.\n1. Apply linear regression with ±2 σ confidence to project costs\
    \ and FTEs.\n1. Flag any trial expected to exceed its baseline budget by >10 %.\n1. Summarize drivers such as CRA travel\
    \ or lab kits.\n1. Output:\n   - A table named \"Forecast\" with Month, Trial ID, Forecast Cost, Forecast FTE, Variance\
    \ %.\n   - A bulleted \"Key Insights\" section no longer than 200 words.\n   - Briefly show calculations and assumptions\
    \ after the table.\n\nInputs:\n- `{{historic_burn_rates}}`\n- `{{enrollment_deltas}}`\n\nOutput Format:\nMarkdown table\
    \ followed by bullet list and calculation notes."
testData:
- vars:
    historic_burn_rates: Sample burn rates
    enrollment_deltas: Sample deltas
  expected: 'Forecast table with cost, FTE, and variance percentage.

    '
evaluators:
- name: Contains Forecast table
  string:
    contains: Forecast

```
