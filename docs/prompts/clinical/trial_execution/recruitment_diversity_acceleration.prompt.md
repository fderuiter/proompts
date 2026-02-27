---
title: Patient Recruitment and Diversity Acceleration Plan
---

# Patient Recruitment and Diversity Acceleration Plan

Boost enrollment and improve demographic diversity in a stalled Phase III study.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/trial_execution/recruitment_diversity_acceleration.prompt.yaml)

```yaml
---
name: Patient Recruitment and Diversity Acceleration Plan
version: 0.1.0
description: Boost enrollment and improve demographic diversity in a stalled Phase III study.
metadata:
  domain: clinical
  complexity: medium
  tags:
  - trial-execution
  - patient
  - recruitment
  - diversity
  - acceleration
  requires_context: false
variables: []
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a patient‑engagement strategist. Enrollment has stalled at 45 % of target in a Phase III rare‑disease
    study spanning 22 countries and 70 sites. The sponsor seeks recovery. The goal is to increase monthly randomizations by
    ≥ 35 % while aligning diversity with FDA 2024 guidance. Maintain the current protocol and keep budget increases ≤ 8 %.


    Ask clarifying questions first if any information is missing.'
- role: user
  content: '1. Provide a data‑driven root‑cause analysis framework covering site performance, startup, outreach and eligibility.

    2. Propose country‑by‑country recruitment tactics such as community partnerships and telehealth pre‑screening.

    3. Estimate budget impact (± 15 %) and ROI projection.

    4. Outline a metrics dashboard with leading and lagging indicators.


    Inputs:

    - None


    Output Format:

    Concise report (≤ 1 000 words) plus a one‑slide KPI dashboard sketch in text form.'
testData:
- input: 'Create recovery plan.

    '
  expected: 'metrics dashboard

    '
evaluators:
- name: Includes ROI projection
  string:
    contains: ROI

```
