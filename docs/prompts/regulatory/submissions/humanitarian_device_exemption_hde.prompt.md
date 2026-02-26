---
title: Humanitarian Device Exemption (HDE)
---

# Humanitarian Device Exemption (HDE)

Explain why the health benefit of a HUD outweighs the risk of injury.

[View Source YAML](../../../../prompts/regulatory/submissions/humanitarian_device_exemption_hde.prompt.yaml)

```yaml
---
name: Humanitarian Device Exemption (HDE)
version: 0.1.0
description: Explain why the health benefit of a HUD outweighs the risk of injury.
metadata:
  domain: regulatory
  complexity: low
  tags:
  - submissions
  - humanitarian
  - device
  - exemption
  - hde
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

    21 CFR Part 814 Subpart H


    ## Objective

    Explain why the health benefit of a HUD outweighs the risk of injury.


    ## Output Format

    Formal narrative explanation.'
- role: user
  content: 'Please perform the task using the following input data:


    <input>

    {{input}}

    </input>'
testData:
- input: HUD designation and risk-benefit analysis of alternatives. (Example data)
  expected: Expected output as per instructions.
evaluators:
- name: Validation Check
  regex: (?i)Check

```
