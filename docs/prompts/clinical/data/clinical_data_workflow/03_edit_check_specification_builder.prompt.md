---
title: Edit-Check Specification Builder for New eCRF Fields
---

# Edit-Check Specification Builder for New eCRF Fields

Create edit-check specifications for the new Concomitant Medication module in Medidata Rave.

[View Source YAML](../../../../../prompts/clinical/data/clinical_data_workflow/03_edit_check_specification_builder.prompt.yaml)

```yaml
---
name: Edit-Check Specification Builder for New eCRF Fields
version: 0.1.0
description: Create edit-check specifications for the new Concomitant Medication module in Medidata Rave.
metadata:
  domain: clinical
  complexity: low
  tags:
  - data
  - edit-check
  - specification
  - builder
  - new
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
  content: "You are a Clinical Data Specialist configuring Medidata Rave.  \n**Goal**: Create detailed edit-check specifications\
    \ for the new Concomitant Medication (CMED) module."
- role: user
  content: '{{input}}'
testData:
- input: 'Field: CMSTDTC, CMENDTC

    Rule: End Date must be on or after Start Date.'
  expected: IF CMENDTC < CMSTDTC THEN raise query "End Date precedes Start Date."
evaluators:
- name: Validates date order
  string:
    contains: CMENDTC < CMSTDTC

```
