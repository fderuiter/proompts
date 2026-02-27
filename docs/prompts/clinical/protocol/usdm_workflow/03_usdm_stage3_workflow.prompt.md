---
title: Protocol to USDM Stage 3 - Workflow
---

# Protocol to USDM Stage 3 - Workflow

Extract Encounters and Activities from Schedule of Activities.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/protocol/usdm_workflow/03_usdm_stage3_workflow.prompt.yaml)

```yaml
---
name: Protocol to USDM Stage 3 - Workflow
description: Extract Encounters and Activities from Schedule of Activities.
model: gpt-4o
modelParameters:
  temperature: 0.1
metadata:
  domain: clinical
  complexity: high
  tags:
  - protocol
  - cdisc
  - usdm
  - workflow
  requires_context: true
variables:
- name: protocol_soa_text
  description: The Schedule of Activities table or text.
  required: true
messages:
- role: system
  content: "You are a CDISC Standards Specialist.\n\n# Task\nDeconstruct the Schedule of Activities into two lists: `Encounters`\
    \ (Visits) and `Activities` (Procedures).\n1. **Encounters:** List every unique visit/time-point. Assign a unique ID (e.g.,\
    \ ENC_01). Note the timing (e.g., \"Day 1\").\n2. **Activities:** List every unique procedure (e.g., \"Informed Consent\"\
    , \"Vital Signs\"). Assign a unique ID (e.g., ACT_01).\n3. **Matrix:** Create a mapping list that shows which `activityId`\
    \ happens at which `encounterId`.\n\n# Output Requirement\nReturn a JSON snippet:\n\n{\n  \"encounters\": [\n    { \"\
    id\": \"ENC_01\", \"name\": \"Screening\", \"timing\": \"-28 Days\" }\n  ],\n  \"activities\": [\n    { \"id\": \"ACT_01\"\
    , \"name\": \"Informed Consent\" },\n    { \"id\": \"ACT_02\", \"name\": \"Vital Signs\" }\n  ],\n  \"workflow_matrix\"\
    : [\n    { \"encounterId\": \"ENC_01\", \"activityIds\": [\"ACT_01\", \"ACT_02\"] }\n  ]\n}\n"
- role: user
  content: '# Input

    <protocol_soa_text>

    {{protocol_soa_text}}

    </protocol_soa_text>

    '
testData:
- input: 'protocol_soa_text: "Visit 1 (Day 1): Informed Consent, Vitals. Visit 2 (Day 7): Vitals."

    '
  expected: "{\n  \"encounters\": [\n    { \"name\": \"Visit 1\" }\n  ]\n}\n"
evaluators:
- name: Valid JSON
  regex:
    pattern: (?s)^[\s\S]*\{[\s\S]*\}[\s\S]*$
- name: Contains workflow_matrix
  regex:
    pattern: '(?s)"workflow_matrix"\s*:'
version: 0.1.0

```
