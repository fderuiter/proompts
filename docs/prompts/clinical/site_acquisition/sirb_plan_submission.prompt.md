---
title: Single IRB (sIRB) Plan Submission
---

# Single IRB (sIRB) Plan Submission

Generate sIRB Plan and communication strategy.

[View Source YAML](../../../../prompts/clinical/site_acquisition/sirb_plan_submission.prompt.yaml)

```yaml
---
name: Single IRB (sIRB) Plan Submission
version: 0.1.0
description: Generate sIRB Plan and communication strategy.
metadata:
  domain: clinical
  complexity: low
  tags:
  - site-acquisition
  - single
  - irb
  - plan
  - submission
  requires_context: false
variables:
- name: grant_details
  description: The grant details to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Grant Administrator. Generate a Single IRB (sIRB) Plan for this multi-site NIH grant application, including
    a list of participating sites and a communication plan for protocol-specific information. Adhere to NIH Single IRB Policy.
- role: user
  content: 'Generate a Single IRB (sIRB) Plan for this multi-site NIH grant application, including a list of participating
    sites and a communication plan for protocol-specific information.


    Inputs:

    - `{{grant_details}}`


    Output format:

    Markdown sIRB Plan.'
testData:
- input: 'grant_details: Multi-site study with 5 centers.

    '
  expected: 'sIRB Plan

    '
evaluators:
- name: Participating Sites
  string:
    contains: Participating Sites
- name: Communication Plan
  string:
    contains: Communication Plan

```
