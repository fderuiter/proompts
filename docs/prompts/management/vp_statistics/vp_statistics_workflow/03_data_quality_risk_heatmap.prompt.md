---
title: Data-Quality Risk Heat Map
---

# Data-Quality Risk Heat Map

Assess site-level data quality and recommend mitigation actions.

[View Source YAML](../../../../../prompts/management/vp_statistics/vp_statistics_workflow/03_data_quality_risk_heatmap.prompt.yaml)

```yaml
---
name: Data-Quality Risk Heat Map
version: 0.1.0
description: Assess site-level data quality and recommend mitigation actions.
metadata:
  domain: management
  complexity: medium
  tags:
  - statistics
  - data-quality
  - risk
  - heat
  - map
  requires_context: false
variables:
- name: query_log
  description: open and closed queries
  required: true
- name: raw_eds_dump
  description: patient-level dataset
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a clinical-data quality auditor specializing in risk-based monitoring. Inputs include:


    - `{{raw_eds_dump}}` – patient-level dataset

    - `{{query_log}}` – open and closed queries


    Ensure summaries are reproducible.'
- role: user
  content: "1. Confirm dataset shapes and key columns.\n2. Declare the risk-score formula and compute scores (0–100) for each\
    \ site using:\n   - Query burden per subject\n   - Major protocol deviations per visit\n   - Timeliness of data entry\
    \ (Δ DBL)\n3. Show a table of the top ten high-risk sites with driver metrics.\n4. Generate an ASCII heat map (rows =\
    \ sites, columns = risk deciles).\n5. Recommend three specific mitigations for each high-risk site.\n6. Include the Python\
    \ (pandas) code used for calculations.\n7. Ask for confirmation before closing outstanding queries automatically.\n8.\
    \ Keep total output under 800 words.\n\nInputs:\n- `{{raw_eds_dump}}` – patient-level dataset\n- `{{query_log}}` – query\
    \ log with open and closed queries\n\nOutput Format:\n1. Markdown table of top ten high-risk sites with driver metrics\n\
    2. ASCII heat map (rows = sites, columns = risk deciles)\n3. Mitigation bullets (three per high-risk site)\n4. Python\
    \ (pandas) code block used for calculations"
testData:
- vars:
    raw_eds_dump: sample_dataset
    query_log: sample_query_log
  expected: Markdown table of top ten high-risk sites.
evaluators:
- name: Mentions risk deciles
  string:
    contains: risk deciles

```
