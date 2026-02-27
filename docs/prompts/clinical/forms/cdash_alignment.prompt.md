---
title: CDASH Alignment
---

# CDASH Alignment

Standardize clinical data collection fields using CDASH models.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/forms/cdash_alignment.prompt.yaml)

```yaml
---
name: CDASH Alignment
version: 0.1.0
description: Standardize clinical data collection fields using CDASH models.
metadata:
  domain: clinical
  complexity: medium
  tags:
  - forms
  - cdash
  - alignment
  requires_context: false
variables:
- name: cdash_guide
  description: The cdash guide to use for this prompt
  required: true
- name: crf_draft
  description: 'CDASH User Guide: `{{cdash_guide}}`'
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a CDISC Standards Expert. Standardize clinical data collection fields using CDASH models to facilitate
    easier flow into SDTM. Focus on Vital Signs (VS) domain. Adhere to CDISC CDASH 2.0.
- role: user
  content: 'Reformat the data collection fields in this draft CRF to align with the CDASH v2.1 standards for the Vital Signs
    (VS) domain, ensuring the inclusion of standard indicator questions.


    Inputs:

    - CRF Draft: `{{crf_draft}}`

    - CDASH User Guide: `{{cdash_guide}}`


    Output format:

    Markdown CDASH Alignment Table (Draft Field -> CDASH Variable -> Question Text).'
testData:
- input: 'crf_draft: "Patient Height in inches."

    cdash_guide: "Use VS.VSORRES, VS.VSORRESU."

    '
  expected: '| Draft Field | CDASH Variable |

    '
evaluators:
- name: Alignment Table
  string:
    contains: '| Draft Field |'
- name: CDASH Variable
  string:
    contains: VSORRES

```
