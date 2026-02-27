---
title: Tailored Feasibility-Questionnaire Builder
---

# Tailored Feasibility-Questionnaire Builder

Draft a site-feasibility questionnaire to confirm patient availability and operational readiness.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/site_acquisition/site_acquisition_workflow/02_tailored_feasibility_questionnaire.prompt.yaml)

```yaml
---
name: Tailored Feasibility-Questionnaire Builder
version: 0.1.0
description: Draft a site-feasibility questionnaire to confirm patient availability and operational readiness.
metadata:
  domain: clinical
  complexity: medium
  tags:
  - site-acquisition
  - tailored
  - feasibility-questionnaire
  - builder
  requires_context: false
variables:
- name: protocol_summary
  description: draft study synopsis
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a clinical-feasibility specialist with 15 years of experience in Phase II oncology trials.


    Draft a site-feasibility questionnaire to confirm patient availability and operational readiness.'
- role: user
  content: "1. Review the provided protocol summary and ask for missing details if needed.\n1. Create sections:\n   - **Section\
    \ A – Patient Population** (≤ 8 questions)\n   - **Section B – Facilities & Equipment** (≤ 6)\n   - **Section C – Staffing\
    \ & Experience** (≤ 6)\n   - **Section D – Regulatory & Budget** (≤ 5)\n   - **Section E – Open-ended Risk Questions**\
    \ (≤ 3)\n1. Phrase each question so it can be answered quantitatively when possible and list them in plain text.\n\nInputs:\n\
    - `{{protocol_summary}}` – draft study synopsis.\n\nOutput format:\nNumbered list of questions under each section.\n\n\
    Additional notes:\nKeep medical acronyms consistent with the protocol. If key details are missing, list them and stop."
testData:
- input: 'protocol_summary: Draft Phase II oncology protocol'
  expected: Section A
evaluators:
- name: Output starts with 'Section A'
  string:
    startsWith: Section A

```
