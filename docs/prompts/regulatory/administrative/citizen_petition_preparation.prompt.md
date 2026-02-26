---
title: Citizen Petition Preparation
---

# Citizen Petition Preparation

Draft a Citizen Petition requesting administrative action by the Commissioner.

[View Source YAML](../../../../prompts/regulatory/administrative/citizen_petition_preparation.prompt.yaml)

```yaml
---
name: Citizen Petition Preparation
version: 0.1.0
description: Draft a Citizen Petition requesting administrative action by the Commissioner.
metadata:
  domain: regulatory
  complexity: low
  tags:
  - regulatory-admin
  - citizen
  - petition
  - preparation
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

    21 CFR Part 10.30


    ## Objective

    Draft a Citizen Petition requesting administrative action by the Commissioner.


    ## Output Format

    Structured petition following 21 CFR 10.30(b)(3) format.'
- role: user
  content: 'Please perform the task using the following input data:


    <input>

    {{input}}

    </input>'
testData:
- input: Factual/legal grounds, action requested, and environmental impact assessment. (Example data)
  expected: Expected output as per instructions.
evaluators:
- name: Validation Check
  regex: (?i)Verify

```
