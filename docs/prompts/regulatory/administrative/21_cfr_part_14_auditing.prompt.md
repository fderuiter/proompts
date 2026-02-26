---
title: 21 CFR Part 14 Auditing
---

# 21 CFR Part 14 Auditing

Audit advisory committee meeting minutes for compliance with record-keeping elements.

[View Source YAML](../../../../prompts/regulatory/administrative/21_cfr_part_14_auditing.prompt.yaml)

```yaml
---
name: 21 CFR Part 14 Auditing
version: 0.1.0
description: Audit advisory committee meeting minutes for compliance with record-keeping elements.
metadata:
  domain: regulatory
  complexity: low
  tags:
  - regulatory-admin
  - cfr
  - part
  - auditing
  requires_context: false
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

    21 CFR Part 14


    ## Objective

    Audit advisory committee meeting minutes for compliance with record-keeping elements.


    ## Output Format

    Markdown compliance checklist.'
- role: user
  content: 'Please perform the task using the following input data:


    <input>

    {{input}}

    </input>'
testData:
- input: Minutes, attendee list, and information considered. (Example data)
  expected: Expected output as per instructions.
evaluators:
- name: Validation Check
  regex: (?i)Verify

```
