---
title: Diversity Action Plan Development
---

# Diversity Action Plan Development

Generate a Diversity Action Plan per FDA guidance.

[View Source YAML](../../../../prompts/clinical/trial_execution/diversity_action_plan_document.prompt.yaml)

```yaml
---
name: Diversity Action Plan Development
version: 0.1.0
description: Generate a Diversity Action Plan per FDA guidance.
metadata:
  domain: clinical
  complexity: low
  tags:
  - trial-execution
  - diversity
  - action
  - plan
  - development
  requires_context: false
variables:
- name: epidemiology_data
  description: The data or dataset to analyze
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Clinical Operations Strategist. Generate a Diversity Action Plan that specifies enrollment goals for
    underrepresented racial and ethnic groups as required by FDA guidance, based on the epidemiology of the target indication.
- role: user
  content: 'Generate a Diversity Action Plan that specifies enrollment goals for underrepresented racial and ethnic groups
    as required by FDA guidance, based on the epidemiology of the target indication.


    Inputs:

    - `{{epidemiology_data}}`


    Output format:

    Markdown Diversity Action Plan.'
testData:
- input: 'epidemiology_data: Hypertension prevalence by race.

    '
  expected: 'Diversity Action Plan

    '
evaluators:
- name: Enrollment Goals
  string:
    contains: Enrollment Goals
- name: Underrepresented Groups
  string:
    contains: Underrepresented Groups

```
