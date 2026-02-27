---
title: Phase II Oncology DMP
---

# Phase II Oncology DMP

Create a Data Management Plan for a Phase II oncology study.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/data_management/phase_ii_oncology_dmp.prompt.yaml)

```yaml
---
name: Phase II Oncology DMP
version: 0.1.0
description: Create a Data Management Plan for a Phase II oncology study.
metadata:
  domain: clinical
  complexity: low
  tags:
  - data-management
  - phase
  - oncology
  - dmp
  requires_context: false
variables:
- name: input
  description: The primary input or query text for the prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a data manager developing a comprehensive data management plan for a

    Phase II oncology trial.

    '
- role: user
  content: '{{input}}'
testData:
- input: Draft key sections of the DMP for a Phase II trial.
  expected: Includes data collection, cleaning, and storage plans.
evaluators:
- name: Output mentions plan
  string:
    contains: plan

```
