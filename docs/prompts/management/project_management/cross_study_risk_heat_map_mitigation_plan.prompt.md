---
title: Cross-Study Operational Risk Heat Map and Mitigation Plan
---

# Cross-Study Operational Risk Heat Map and Mitigation Plan

Identify and prioritize the top portfolio-level operational risks and propose mitigations.

[View Source YAML](../../../../prompts/management/project_management/cross_study_risk_heat_map_mitigation_plan.prompt.yaml)

```yaml
---
name: Cross-Study Operational Risk Heat Map and Mitigation Plan
version: 0.1.0
description: Identify and prioritize the top portfolio-level operational risks and propose mitigations.
metadata:
  domain: management
  complexity: medium
  tags:
  - project-management
  - cross-study
  - operational
  - risk
  - heat
  requires_context: false
variables:
- name: risk_register
  description: The risk register to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are an enterprise risk-management AI for global clinical operations. Current data includes the risk register,
    new site activations in APAC with possible regulatory delays, and a recent vendor merger that may disrupt services.


    Use concise language and focus on cross-study themes.'
- role: user
  content: '1. Rate each risk on Probability (1–5) × Impact (1–5) to create a heat‑map matrix (High/Med/Low).

    1. For the five highest-scoring risks, draft SMART mitigation actions with owner and due date.

    1. Provide an executive summary (≤150 words) for steering‑committee use.

    1. Outline the scoring logic applied.


    Inputs:

    - `{{risk_register}}`


    Output Format:

    - Table "Risk-Heat-Map".

    - Table "Mitigation-Plan".

    - Executive summary paragraph.'
testData:
- vars:
    risk_register: Example register
  expected: 'Tables named Risk-Heat-Map and Mitigation-Plan with an executive summary.

    '
evaluators:
- name: Contains Risk-Heat-Map table
  string:
    contains: Risk-Heat-Map

```
