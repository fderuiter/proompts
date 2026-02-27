---
title: Biological Safety Plan Developer
---

# Biological Safety Plan Developer

Create a biological safety plan for the preclinical phase of a new medical device.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/scientific/biosafety/biological_safety_workflow/02_biological_safety_plan_developer.prompt.yaml)

```yaml
---
name: Biological Safety Plan Developer
version: 0.1.0
description: Create a biological safety plan for the preclinical phase of a new medical device.
metadata:
  domain: scientific
  complexity: low
  tags:
  - biosafety
  - biological
  - safety
  - plan
  - developer
  requires_context: false
variables:
- name: device_description
  description: description and materials of the device
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are leading a biological safety consulting team.


    Keep instructions concise and actionable.'
- role: user
  content: '1. Identify key biological endpoints (e.g., irritation, sensitization, systemic toxicity).

    2. Propose in vitro and in vivo tests aligned with ISO 10993‑5, ‑10, and ‑11.

    3. Define pass/fail criteria and acceptance thresholds.

    4. Provide rationale for each test, including risk prioritization.

    5. Outline a step-by-step workflow and timeline.


    Inputs:

    - `{{device_description}}` — description and materials of the device


    Output format:

    Bullet points and headings forming a clear plan.'
testData:
- vars:
    device_description: example_device_description
  expected: Bullet points and headings forming a clear plan.
evaluators:
- name: Output starts with a bullet point
  string:
    startsWith: '-'

```
