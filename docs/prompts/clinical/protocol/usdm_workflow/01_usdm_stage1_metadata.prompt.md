---
title: Protocol to USDM Stage 1 - Metadata
---

# Protocol to USDM Stage 1 - Metadata

Extract Study Level Metadata and Design from Protocol.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/protocol/usdm_workflow/01_usdm_stage1_metadata.prompt.yaml)

```yaml
---
name: Protocol to USDM Stage 1 - Metadata
description: Extract Study Level Metadata and Design from Protocol.
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
  - metadata
  requires_context: true
variables:
- name: protocol_text
  description: The full text or synopsis of the protocol.
  required: true
messages:
- role: system
  content: "You are a Clinical Data Architect.\n\n# Task\nAnalyze the text to extract Study Level Metadata and Study Design.\n\
    1. Identify the Protocol Title, ID, Phase, and Medical Condition.\n2. Identify the Study Design (e.g., Parallel, Crossover).\n\
    3. Identify all Study Arms (e.g., Placebo, Experimental 10mg).\n\n# Output Requirement\nReturn a JSON snippet with the\
    \ following structure. **Assign a unique ID (e.g., ARM_01) to each Arm.**\n\n{\n  \"study_meta\": {\n    \"title\": \"\
    String\",\n    \"id\": \"String\",\n    \"phase\": \"String\",\n    \"condition\": \"String\"\n  },\n  \"study_design\"\
    : {\n    \"type\": \"String\",\n    \"arms\": [\n      { \"id\": \"ARM_XX\", \"name\": \"String\", \"description\": \"\
    String\", \"type\": \"String\" }\n    ]\n  }\n}\n"
- role: user
  content: '# Input

    <protocol_text>

    {{protocol_text}}

    </protocol_text>

    '
testData:
- input: 'protocol_text: "Protocol 123: A Phase 2 Study for Hypertension. Parallel design with Placebo and Drug X."

    '
  expected: "{\n  \"study_meta\": {\n    \"id\": \"Protocol 123\"\n  }\n}\n"
evaluators:
- name: Valid JSON
  regex:
    pattern: (?s)^[\s\S]*\{[\s\S]*\}[\s\S]*$
- name: Contains study_meta
  regex:
    pattern: '(?s)"study_meta"\s*:'
version: 0.1.0

```
