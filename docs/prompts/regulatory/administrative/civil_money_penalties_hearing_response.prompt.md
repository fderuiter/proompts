---
title: Civil Money Penalties Hearing Response
---

# Civil Money Penalties Hearing Response

Draft a formal 'Answer' to an FDA complaint seeking civil money penalties.

[View Source YAML](../../../../prompts/regulatory/administrative/civil_money_penalties_hearing_response.prompt.yaml)

```yaml
---
name: Civil Money Penalties Hearing Response
version: 0.1.0
description: Draft a formal 'Answer' to an FDA complaint seeking civil money penalties.
metadata:
  domain: regulatory
  complexity: low
  tags:
  - regulatory-admin
  - civil
  - money
  - penalties
  - hearing
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

    21 CFR Part 17


    ## Objective

    Draft a formal ''Answer'' to an FDA complaint seeking civil money penalties.


    ## Output Format

    Formal legal pleading.'
- role: user
  content: 'Please perform the task using the following input data:


    <input>

    {{input}}

    </input>'
testData:
- input: FDA Complaint, alleged violations, and mitigating factors. (Example data)
  expected: Expected output as per instructions.
evaluators:
- name: Validation Check
  regex: (?i)Review

```
