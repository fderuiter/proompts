---
title: Protocol to USDM Stage 5 - Assembly
---

# Protocol to USDM Stage 5 - Assembly

Assemble the final USDM JSON from previous stages.

[View Source YAML](../../../../../prompts/clinical/protocol/usdm_workflow/05_usdm_stage5_assembly.prompt.yaml)

```yaml
---
name: Protocol to USDM Stage 5 - Assembly
description: Assemble the final USDM JSON from previous stages.
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
  - assembly
  requires_context: true
variables:
- name: metadata_json
  description: Output from Stage 1.
  required: true
- name: rationale_json
  description: Output from Stage 2.
  required: true
- name: workflow_json
  description: Output from Stage 3.
  required: true
- name: concepts_json
  description: Output from Stage 4.
  required: true
messages:
- role: system
  content: 'You are a JSON Systems Integrator.


    # Task

    Merge these four JSON snippets into a single, valid CDISC USDM v3.0 JSON object.

    - Place `study_meta` at the root.

    - Place `criteria` under the `study.criteria` array.

    - Construct the `workflow` section using the `encounters`, `activities`, and `workflow_matrix`.

    - Ensure all ID references (e.g., `activityId` inside `workflow`) remain consistent.


    # Output Requirement

    Produce **only** the final JSON object. Do not add conversational text.

    '
- role: user
  content: '# Inputs

    1. Metadata:

    <metadata_json>

    {{metadata_json}}

    </metadata_json>


    2. Rationale:

    <rationale_json>

    {{rationale_json}}

    </rationale_json>


    3. Workflow:

    <workflow_json>

    {{workflow_json}}

    </workflow_json>


    4. Concepts:

    <concepts_json>

    {{concepts_json}}

    </concepts_json>

    '
testData:
- input: 'metadata_json: ''{"study_meta": {"id": "123"}}''

    rationale_json: ''{"criteria": []}''

    workflow_json: ''{"encounters": []}''

    concepts_json: ''{"biomedicalConcepts": []}''

    '
  expected: "{\n  \"study\": {\n    \"id\": \"123\"\n  }\n}\n"
evaluators:
- name: Valid JSON
  regex:
    pattern: (?s)^[\s\S]*\{[\s\S]*\}[\s\S]*$
- name: Contains study root
  regex:
    pattern: '(?s)"study"\s*:'
version: 0.1.0

```
