---
title: Clinical Trial Document Archiving
---

# Clinical Trial Document Archiving

Develop archival strategy for TMF.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/data_management/document_archiving.prompt.yaml)

```yaml
---
name: Clinical Trial Document Archiving
version: 0.1.0
description: Develop archival strategy for TMF.
metadata:
  domain: clinical
  complexity: low
  tags:
  - data-management
  - clinical
  - trial
  - document
  - archiving
  requires_context: false
variables:
- name: tmf_details
  description: The tmf details to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Records Manager. Develop an archival strategy for the Trial Master File (TMF) that includes environmental
    monitoring requirements and a 15-year data retention schedule. Ensure compliance with ICH GCP Section 8.
- role: user
  content: 'Develop an archival strategy for the Trial Master File (TMF) that includes environmental monitoring requirements
    and a 15-year data retention schedule.


    Inputs:

    - `{{tmf_details}}`


    Output format:

    Markdown Archival Strategy.'
testData:
- input: 'tmf_details: Paper and electronic records.

    '
  expected: 'Archival Strategy

    '
evaluators:
- name: Retention Schedule
  string:
    contains: Retention Schedule
- name: Environmental Monitoring
  string:
    contains: Environmental Monitoring

```
