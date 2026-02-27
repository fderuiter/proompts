---
title: Maintainability Codebase Analysis
---

# Maintainability Codebase Analysis

Improve code maintainability by addressing readability, organization, and test quality.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/technical/architecture/maintainability_codebase_analysis.prompt.yaml)

```yaml
---
name: Maintainability Codebase Analysis
version: 0.1.0
description: Improve code maintainability by addressing readability, organization, and test quality.
metadata:
  domain: technical
  complexity: low
  tags:
  - architecture
  - maintainability
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
  content: You are a code reviewer focused on maintainability and long-term sustainability.
- role: user
  content: 'Review the following codebase and propose changes to enhance readability, organisation, and test coverage.


    {{codebase}}'
testData: []
evaluators: []

```
