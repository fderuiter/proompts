---
title: Draft a Data Management Plan Section
---

# Draft a Data Management Plan Section

Act as a Clinical Data Management subject-matter expert.

[View Source YAML](../../../../../prompts/clinical/data/clinical_data_workflow/02_data_management_plan_section.prompt.yaml)

```yaml
---
name: Draft a Data Management Plan Section
version: 0.1.0
description: Act as a Clinical Data Management subject-matter expert.
metadata:
  domain: clinical
  complexity: low
  tags:
  - data
  - draft
  - management
  - plan
  - section
  requires_context: false
variables:
- name: input
  description: The primary input or query text for the prompt
  required: true
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: '**Objective**: Draft the "Data Validation & Cleaning" section for the DMP of a global, randomized, double-blind
    Phase II study (Protocol YY456) using Medidata Rave.'
- role: user
  content: '{{input}}'
testData:
- input: Include handling of out-of-range lab values.
  expected: Data Validation & Cleaning includes automated edit checks in Medidata Rave to flag out-of-range lab values.
evaluators:
- name: Mentions Data Validation & Cleaning
  string:
    contains: Data Validation & Cleaning
- name: References Medidata Rave
  string:
    contains: Medidata Rave

```
