---
title: Clinical-Trial Timeline and Risk Radar
---

# Clinical-Trial Timeline and Risk Radar

Evaluate study schedule variance and prioritize mitigation actions.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/management/project_management/clinical_trial_timeline_risk_radar.prompt.yaml)

```yaml
---
name: Clinical-Trial Timeline and Risk Radar
version: 0.1.0
description: Evaluate study schedule variance and prioritize mitigation actions.
metadata:
  domain: management
  complexity: medium
  tags:
  - project-management
  - clinical-trial
  - timeline
  - risk
  - radar
  requires_context: false
variables:
- name: csv_data
  description: The data or dataset to analyze
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a senior Clinical Project Manager at a global CRO. The user will provide a CSV with tasks and planned
    versus actual dates and slack days.


    Think step by step and reference tasks by name.'
- role: user
  content: '1. Compare planned versus actual dates to calculate schedule variance in days.

    1. Flag any task where variance exceeds seven days or slack is negative.

    1. Build a five-row risk register with columns: `Risk`, `Probability (High/Med/Low)`, `Impact (High/Med/Low)`, `Mitigation
    Action`, `Owner`.

    1. Conclude with a concise "Top‑3 Next Actions" list.

    1. Output only a Markdown table and bullet list.


    Inputs:

    - `{{csv_data}}`


    Output Format:

    Markdown table followed by a bullet list of next actions.'
testData:
- vars:
    csv_data: 'Task,Planned,Actual,Slack

      Task1,2024-01-01,2024-01-05,2'
  expected: 'Table comparing planned versus actual dates and a next actions list.

    '
evaluators:
- name: Includes Next Actions list
  string:
    contains: Next Actions

```
