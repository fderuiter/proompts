---
title: Part 11 Closed System Audit
---

# Part 11 Closed System Audit

Audit a software supplier's closed system for electronic record integrity.

[View Source YAML](../../../../prompts/regulatory/quality/part_11_closed_system_audit.prompt.yaml)

```yaml
---
name: Part 11 Closed System Audit
version: 0.1.0
description: Audit a software supplier's closed system for electronic record integrity.
metadata:
  domain: regulatory
  complexity: low
  tags:
  - quality
  - part
  - closed
  - system
  - audit
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

    21 CFR Part 11


    ## Objective

    Audit a software supplier''s closed system for electronic record integrity.


    ## Output Format

    Audit report with checklist.'
- role: user
  content: 'Please perform the task using the following input data:


    <input>

    {{input}}

    </input>'
testData:
- input: Record retrieval protocols and audit trail logs. (Example data)
  expected: Expected output as per instructions.
evaluators:
- name: Validation Check
  regex: (?i)Compare

```
