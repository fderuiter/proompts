---
title: Design Error Prevention
---

# Design Error Prevention

Review and optimize CRF layout to avoid duplication and non-essential fields.

[View Source YAML](../../../../prompts/clinical/forms/crf_design_optimization.prompt.yaml)

```yaml
---
name: Design Error Prevention
version: 0.1.0
description: Review and optimize CRF layout to avoid duplication and non-essential fields.
metadata:
  domain: clinical
  complexity: high
  tags:
  - forms
  - design
  - error
  - prevention
  requires_context: false
variables:
- name: crf_draft
  description: 'Study Protocol: `{{protocol}}`'
  required: true
- name: endpoints
  description: 'Study Hypothesis: `{{hypothesis}}`'
  required: true
- name: hypothesis
  description: The hypothesis to use for this prompt
  required: true
- name: protocol
  description: 'Safety and efficacy endpoints: `{{endpoints}}`'
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Clinical Data Manager/Designer. Analyze the draft CRF layout to identify redundant or non-essential fields
    based on the study hypothesis and suggest improvements to reduce entry errors and site burden. Adhere to ICH GCP E6(R2).
- role: user
  content: 'Analyze the draft CRF layout to identify redundant or non-essential fields based on the study hypothesis and suggest
    improvements to reduce entry errors and site burden.


    Inputs:

    - CRF Draft: `{{crf_draft}}`

    - Study Protocol: `{{protocol}}`

    - Safety and efficacy endpoints: `{{endpoints}}`

    - Study Hypothesis: `{{hypothesis}}`


    Output format:

    Markdown Optimization Report (Field | Issue | Recommendation).'
testData:
- input: 'crf_draft: "Field: Height (cm) at Visit 1 and Visit 2."

    protocol: "Height only needed at baseline."

    endpoints: "Weight change."

    hypothesis: "Drug reduces weight."

    '
  expected: '| Field | Issue | Recommendation |

    '
evaluators:
- name: Optimization Table
  string:
    contains: '| Field |'
- name: Redundancy Check
  string:
    contains: Visit 2

```
