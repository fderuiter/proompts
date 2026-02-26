---
title: Trial Master File (TMF) Maintenance
---

# Trial Master File (TMF) Maintenance

Generate TMF checklist based on CDISC Reference Model.

[View Source YAML](../../../../prompts/clinical/data_management/tmf_maintenance.prompt.yaml)

```yaml
---
name: Trial Master File (TMF) Maintenance
version: 0.1.0
description: Generate TMF checklist based on CDISC Reference Model.
metadata:
  domain: clinical
  complexity: low
  tags:
  - data-management
  - trial
  - master
  - file
  - tmf
  requires_context: true
variables:
- name: study_phase
  description: The study phase to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a TMF Specialist. Generate a checklist for the Trial Master File (TMF) based on the CDISC TMF Reference
    Model, categorizing documents required before, during, and after the clinical phase to ensure audit readiness.
- role: user
  content: 'Generate a checklist for the Trial Master File (TMF) based on the CDISC TMF Reference Model, categorizing documents
    required before, during, and after the clinical phase to ensure audit readiness.


    Inputs:

    - `{{study_phase}}`


    Output format:

    Markdown TMF Checklist.'
testData:
- input: 'study_phase: Study Start-up.

    '
  expected: 'TMF Checklist

    '
evaluators:
- name: CDISC TMF Reference Model
  string:
    contains: CDISC TMF Reference Model
- name: Audit Readiness
  string:
    contains: Audit Readiness

```
