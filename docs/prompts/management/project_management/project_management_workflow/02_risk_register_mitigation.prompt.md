---
title: Comprehensive Risk Register and Mitigation Plan
---

# Comprehensive Risk Register and Mitigation Plan

Produce a risk register with mitigation actions and overall strategies.

[View Source YAML](../../../../../prompts/management/project_management/project_management_workflow/02_risk_register_mitigation.prompt.yaml)

```yaml
---
name: Comprehensive Risk Register and Mitigation Plan
version: 0.1.0
description: Produce a risk register with mitigation actions and overall strategies.
metadata:
  domain: management
  complexity: medium
  tags:
  - project-management
  - comprehensive
  - risk
  - register
  - mitigation
  requires_context: false
variables:
- name: project_overview
  description: The project overview to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are an enterprise risk-management analyst. The user will supply a project overview including the current phase
    and budget.


    Use concise language suitable for senior stakeholders.'
- role: user
  content: '1. List each risk with ID, category, description, probability (1–5), impact (1–5), qualitative RAG score, owner,
    proposed mitigation, and residual risk score.

    1. Sort the table by highest combined risk score.

    1. Conclude with three overarching risk-response strategies.

    1. Wrap text in table cells at roughly 40 characters for readability.

    1. If project data are insufficient, list missing inputs and pause.


    Inputs:

    - `{{project_overview}}`


    Output Format:

    Markdown table followed by a short list of overarching strategies.'
testData:
- vars:
    project_overview: Example overview
  expected: 'Markdown table sorted by highest combined risk score.

    '
evaluators:
- name: Mentions mitigation actions
  string:
    contains: Mitigation

```
