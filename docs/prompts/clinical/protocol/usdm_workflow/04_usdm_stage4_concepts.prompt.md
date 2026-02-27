---
title: Protocol to USDM Stage 4 - Concepts
---

# Protocol to USDM Stage 4 - Concepts

Map Activities to Biomedical Concepts.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/protocol/usdm_workflow/04_usdm_stage4_concepts.prompt.yaml)

```yaml
---
name: Protocol to USDM Stage 4 - Concepts
description: Map Activities to Biomedical Concepts.
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
  - concepts
  requires_context: true
variables:
- name: activities_json
  description: The JSON list of Activities from Stage 3.
  required: true
messages:
- role: system
  content: "You are a Clinical Data Standards Mapper.\n\n# Task\nFor each Activity identified in the input:\n1. Determine\
    \ the appropriate Biomedical Concept (BC).\n2. If the activity is a composite (e.g., \"Vitals\"), break it down into its\
    \ components (Systolic BP, Diastolic BP, Heart Rate).\n3. Assign a `bcId` to each.\n\n# Output Requirement\nReturn a JSON\
    \ snippet linking Activity IDs to Biomedical Concept definitions:\n\n{\n  \"biomedicalConcepts\": [\n    {\n      \"activityId\"\
    : \"ACT_02\",\n      \"conceptName\": \"Systolic Blood Pressure\",\n      \"ncitCode\": \"C25298\" // Optional: If you\
    \ can infer NCI Thesaurus codes\n    }\n  ]\n}\n"
- role: user
  content: '# Input

    <activities_json>

    {{activities_json}}

    </activities_json>

    '
testData:
- input: 'activities_json: ''[{"id": "ACT_01", "name": "Blood Pressure"}]''

    '
  expected: "{\n  \"biomedicalConcepts\": [\n    { \"activityId\": \"ACT_01\" }\n  ]\n}\n"
evaluators:
- name: Valid JSON
  regex:
    pattern: (?s)^[\s\S]*\{[\s\S]*\}[\s\S]*$
- name: Contains biomedicalConcepts
  regex:
    pattern: '(?s)"biomedicalConcepts"\s*:'
version: 0.1.0

```
