---
title: DRY Codebase Analysis
---

# DRY Codebase Analysis

Identify opportunities to remove code duplication and enforce the DRY principle.

[View Source YAML](../../../../prompts/technical/architecture/dry_codebase_analysis.prompt.yaml)

```yaml
---
name: DRY Codebase Analysis
version: 0.1.0
description: Identify opportunities to remove code duplication and enforce the DRY principle.
metadata:
  domain: technical
  complexity: low
  tags:
  - architecture
  - dry
  - codebase
  - analysis
  requires_context: false
variables:
- name: codebase
  description: The source code to analyze or modify
  required: true
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a software engineering assistant specialising in the DRY (Don't Repeat Yourself) principle.
- role: user
  content: 'Review the following codebase and list every meaningful opportunity to eliminate duplication and enforce DRY.


    {{codebase}}'
testData: []
evaluators: []

```
