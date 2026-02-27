---
title: Clinical Study Report (CSR) Writing
---

# Clinical Study Report (CSR) Writing

Draft Clinical Study Report sections.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/scientific/medical_writing/csr_writing.prompt.yaml)

```yaml
---
name: Clinical Study Report (CSR) Writing
version: 0.1.0
description: Draft Clinical Study Report sections.
metadata:
  domain: scientific
  complexity: low
  tags:
  - medical-writing
  - clinical
  - study
  - report
  - csr
  requires_context: false
variables:
- name: statistical_outputs
  description: The statistical outputs to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Medical Writer. Draft the Clinical Study Report following the ICH E3 structure, integrating the final
    statistical outputs and providing descriptive narratives for all serious adverse events.
- role: user
  content: 'Draft the Clinical Study Report following the ICH E3 structure, integrating the final statistical outputs and
    providing descriptive narratives for all serious adverse events.


    Inputs:

    - `{{statistical_outputs}}`


    Output format:

    Markdown CSR Sections.'
testData:
- input: 'statistical_outputs: Efficacy data and SAE listings.

    '
  expected: 'Clinical Study Report

    '
evaluators:
- name: ICH E3
  string:
    contains: ICH E3
- name: Safety Narratives
  string:
    contains: Safety Narratives

```
