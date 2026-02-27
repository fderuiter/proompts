---
title: Protocol Section Refinement
---

# Protocol Section Refinement

Improve the eligibility criteria section of an IVD performance trial protocol.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/protocol/protocol_workflow/04_protocol_section_refinement.prompt.yaml)

```yaml
---
name: Protocol Section Refinement
version: 0.1.0
description: Improve the eligibility criteria section of an IVD performance trial protocol.
metadata:
  domain: clinical
  complexity: medium
  tags:
  - protocol-design
  - protocol
  - section
  - refinement
  requires_context: false
variables:
- name: condition
  description: disease or study condition
  required: true
- name: draft_section
  description: current text of the protocol section
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are an experienced clinical operations lead refining a protocol targeting a specific condition.


    Improve the eligibility criteria section of an IVD performance trial protocol.'
- role: user
  content: "1. Provide specific inclusion and exclusion rules (e.g., sample type, analyte range, comorbidities).\n1. Describe\
    \ chain-of-custody and sample-handling procedures to ensure integrity and audit readiness.\n1. Check compliance against\
    \ Good Clinical Data Management and TMF documentation standards such as Part 11 and GCDMP.\n\n  Inputs:\n  - `{{condition}}`\
    \ – disease or study condition\n  - `{{draft_section}}` – current text of the protocol section\n\nOutput format:\nRevised\
    \ section in Markdown with clear subsections for criteria and handling procedures.\n\nAdditional notes:\nKeep language\
    \ concise and align with regulatory expectations."
testData:
- input: 'condition: diabetes

    draft_section: placeholder text

    '
  expected: Inclusion
evaluators:
- name: Contains inclusion subsection
  string:
    contains: Inclusion

```
