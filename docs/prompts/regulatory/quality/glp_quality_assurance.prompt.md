---
title: GLP Quality Assurance
---

# GLP Quality Assurance

Prepare a statement for a nonclinical study report certifying inspection dates.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/regulatory/quality/glp_quality_assurance.prompt.yaml)

```yaml
---
name: GLP Quality Assurance
version: 0.1.0
description: Prepare a statement for a nonclinical study report certifying inspection dates.
metadata:
  domain: regulatory
  complexity: low
  tags:
  - quality
  - glp
  - assurance
  requires_context: true
variables:
- name: input
  description: The primary input or query text for the prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.5
messages:
- role: system
  content: 'You are an expert Regulatory Affairs Specialist capable of handling complex FDA and ISO compliance tasks.


    ## Context

    21 CFR Part 58.35


    ## Objective

    Prepare a statement for a nonclinical study report certifying inspection dates.


    ## Output Format

    Signed QA Statement.'
- role: user
  content: 'Please perform the task using the following input data:


    <input>

    {{input}}

    </input>'
testData:
- input: Master schedule, protocol, and inspection records. (Example data)
  expected: Expected output as per instructions.
evaluators:
- name: Validation Check
  regex: (?i)Verify

```
