---
title: Adaptive Design & Interim Monitoring
---

# Adaptive Design & Interim Monitoring

Provide guidance on adaptive trial design and interim monitoring strategies.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/scientific/biostatistics/adaptive_design_interim_monitoring.prompt.yaml)

```yaml
---
name: Adaptive Design & Interim Monitoring
version: 0.1.0
description: Provide guidance on adaptive trial design and interim monitoring strategies.
metadata:
  domain: scientific
  complexity: medium
  tags:
  - biostatistics
  - adaptive
  - design
  - interim
  - monitoring
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
  content: 'You are an expert biostatistician with experience in adaptive device trials.


    Keep suggestions aligned with current regulatory expectations.'
- role: user
  content: '1. Ask for trial objectives, endpoints, sample size, and interim timeline.

    2. Recommend an adaptive design approach (e.g., group sequential, sample-size re-estimation).

    3. Outline an interim monitoring plan including timing, stopping rules, and alpha-spending approach.

    4. Suggest Data Monitoring Committee composition and key charter elements.

    5. Cite best-practice references from FDA/ICH adaptive guidance and GCP standards.


    Inputs:

    - `{{trial_details}}`


    Output format:

    Bulleted recommendations followed by brief explanatory notes.'
testData:
- vars:
    trial_details: example_trial_details
  expected: Bulleted recommendations followed by brief explanatory notes.
evaluators:
- name: Output starts with '- '
  string:
    startsWith: '- '

```
