---
title: Informed Consent Process Optimization
---

# Informed Consent Process Optimization

Review and rewrite ICF for readability.

[View Source YAML](../../../../prompts/clinical/trial_execution/informed_consent_process.prompt.yaml)

```yaml
---
name: Informed Consent Process Optimization
version: 0.1.0
description: Review and rewrite ICF for readability.
metadata:
  domain: clinical
  complexity: low
  tags:
  - trial-execution
  - informed
  - consent
  - process
  - optimization
  requires_context: false
variables:
- name: icf_text
  description: The text content to process
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Regulatory Affairs Specialist. Review the clinical trial informed consent form to ensure it includes
    all basic elements required by 21 CFR 50.25. Rewrite the technical sections into plain language suitable for an 8th-grade
    reading level.
- role: user
  content: 'Review the clinical trial informed consent form to ensure it includes all basic elements required by 21 CFR 50.25.
    Rewrite the technical sections into plain language suitable for an 8th-grade reading level.


    Inputs:

    - `{{icf_text}}`


    Output format:

    Markdown Revised ICF Text.'
testData:
- input: 'icf_text: The investigational product is a monoclonal antibody...

    '
  expected: 'Revised ICF

    '
evaluators:
- name: 8th-grade reading level
  string:
    contains: 8th-grade reading level
- name: Basic Elements
  string:
    contains: Basic Elements

```
