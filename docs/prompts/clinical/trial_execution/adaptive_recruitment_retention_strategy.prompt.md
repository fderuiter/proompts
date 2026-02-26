---
title: Adaptive Recruitment and Retention Strategy
---

# Adaptive Recruitment and Retention Strategy

Design an optimized recruitment and retention plan for a multi-site pivotal study.

[View Source YAML](../../../../prompts/clinical/trial_execution/adaptive_recruitment_retention_strategy.prompt.yaml)

```yaml
---
name: Adaptive Recruitment and Retention Strategy
version: 0.1.0
description: Design an optimized recruitment and retention plan for a multi-site pivotal study.
metadata:
  domain: clinical
  complexity: medium
  tags:
  - trial-execution
  - adaptive
  - recruitment
  - retention
  - strategy
  requires_context: false
variables:
- name: device_or_ivd
  description: device or diagnostic under study
  required: true
- name: patient_population
  description: target population
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a clinical trial CRO strategist planning a study of **{{device_or_ivd}}** in **{{patient_population}}**.
    The strategy should incorporate AI‑enhanced pre‑screening, site‑level engagement tactics and metrics to monitor recruitment
    risk and retention performance.


    Ensure the plan is adaptable to varying enrollment rates.'
- role: user
  content: '1. Outline an AI‑assisted pre‑screening workflow (e.g., tele‑calls, transportation support).

    2. Describe site‑level engagement tactics such as CRO–site alignment and digital outreach.

    3. Define metrics to track recruitment risk and retention performance.


    Inputs:

    - `{{device_or_ivd}}` – device or diagnostic under study

    - `{{patient_population}}` – target population


    Output Format:

    Markdown list or table covering:

    1. Pre‑screening workflow

    2. Site-level engagement tactics

    3. Recruitment and retention metrics'
testData:
- input: 'device_or_ivd: glucose monitor

    patient_population: adults with diabetes

    '
  expected: 'Pre‑screening workflow

    '
evaluators:
- name: Contains metrics section
  string:
    contains: Recruitment and retention metrics

```
