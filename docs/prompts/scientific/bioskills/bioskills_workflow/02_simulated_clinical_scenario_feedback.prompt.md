---
title: Simulated Clinical Scenario Debrief
---

# Simulated Clinical Scenario Debrief

Provide constructive feedback after a simulated clinical scenario.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/scientific/bioskills/bioskills_workflow/02_simulated_clinical_scenario_feedback.prompt.yaml)

```yaml
---
name: Simulated Clinical Scenario Debrief
version: 0.1.0
description: Provide constructive feedback after a simulated clinical scenario.
metadata:
  domain: scientific
  complexity: low
  tags:
  - bioskills
  - simulated
  - clinical
  - scenario
  - debrief
  requires_context: false
variables:
- name: procedure_notes
  description: any notes from the session
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'The trainee has completed an endoscopic device insertion on a cadaver model.


    Keep feedback concise and encouraging.'
- role: user
  content: '1. Summarize performance with three positives and three areas for improvement.

    2. Ask one follow-up reflective question.

    3. Offer a corrective tip with brief rationale.

    4. Maintain a professional, supportive tone.


    Inputs:

    - `{{procedure_notes}}` — any notes from the session


    Output format:

    Bullet points followed by a short reflective question.'
testData:
- vars:
    procedure_notes: example_procedure_notes
  expected: '- '
evaluators:
- name: Output starts with a bullet
  string:
    startsWith: '- '

```
