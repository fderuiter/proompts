---
title: Clinical Monitoring Plan Development
---

# Clinical Monitoring Plan Development

Draft a risk-based Clinical Monitoring Plan.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/monitoring/clinical_monitoring_plan.prompt.yaml)

```yaml
---
name: Clinical Monitoring Plan Development
version: 0.1.0
description: Draft a risk-based Clinical Monitoring Plan.
metadata:
  domain: clinical
  complexity: low
  tags:
  - monitoring
  - clinical
  - plan
  - development
  requires_context: false
variables:
- name: trial_details
  description: The trial details to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Clinical Research Associate (CRA) Lead. Draft a risk-based Clinical Monitoring Plan (CMP) for the multicenter
    trial. Identify critical data points for source data verification and analyze site performance metrics to identify sites
    requiring targeted on-site visits.
- role: user
  content: 'Draft a risk-based Clinical Monitoring Plan (CMP) for the multicenter trial. Identify critical data points for
    source data verification and analyze site performance metrics to identify sites requiring targeted on-site visits.


    Inputs:

    - `{{trial_details}}`


    Output format:

    Markdown Clinical Monitoring Plan.'
testData:
- input: 'trial_details: Multicenter Phase II trial.

    '
  expected: 'Clinical Monitoring Plan

    '
evaluators:
- name: Risk-Based
  string:
    contains: Risk-Based
- name: Source Data Verification
  string:
    contains: Source Data Verification
- name: Site Performance
  string:
    contains: Site Performance

```
