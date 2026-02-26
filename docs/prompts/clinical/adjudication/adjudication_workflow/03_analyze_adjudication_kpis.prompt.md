---
title: Analyze Adjudication KPIs
---

# Analyze Adjudication KPIs

Calculate adjudication performance metrics and recommend improvements.

[View Source YAML](../../../../../prompts/clinical/adjudication/adjudication_workflow/03_analyze_adjudication_kpis.prompt.yaml)

```yaml
---
name: Analyze Adjudication KPIs
version: 0.1.0
description: Calculate adjudication performance metrics and recommend improvements.
metadata:
  domain: clinical
  complexity: medium
  tags:
  - adjudication
  - analyze
  - kpis
  requires_context: false
variables:
- name: adjudication_log.csv
  description: event log export
  required: true
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: '- CSV file `adjudication_log.csv` lists all events in an oncology trial.

    - Leadership expects a plan to reduce median cycle time by 20%.


    Request a data dictionary if any column in the CSV is ambiguous before starting the analysis.'
- role: user
  content: "1. Load the CSV and compute:\n   - median and 90th percentile cycle time from event trigger to final decision\n\
    \   - reviewer disagreement rate\n   - top three root causes of delays inferred from status fields\n2. Create bar charts\
    \ for each metric and save them as PNGs.\n3. Recommend at least five concrete process changes tied to these metrics that\
    \ would achieve the target reduction.\n\nInputs:\n- `{{adjudication_log.csv}}` – event log export\n\nOutput format:\n\
    - **Metrics Summary Table**\n- Embedded charts or download links for each PNG\n- Bullet list of recommendations"
testData:
- vars:
    adjudication_log.csv: example_adjudication_log.csv
  expected: '- **Metrics Summary Table**

    - Embedded charts or download links for each PNG

    - Bullet list of recommendations'
evaluators:
- name: Output includes 'Metrics Summary Table'
  string:
    contains: Metrics Summary Table

```
