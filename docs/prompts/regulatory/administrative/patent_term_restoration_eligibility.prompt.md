---
title: Patent Term Restoration Eligibility
---

# Patent Term Restoration Eligibility

Determine if a medical product's review period qualifies for patent term restoration.

[View Source YAML](../../../../prompts/regulatory/administrative/patent_term_restoration_eligibility.prompt.yaml)

```yaml
---
name: Patent Term Restoration Eligibility
version: 0.1.0
description: Determine if a medical product's review period qualifies for patent term restoration.
metadata:
  domain: regulatory
  complexity: low
  tags:
  - regulatory-admin
  - patent
  - term
  - restoration
  - eligibility
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

    21 CFR Part 60


    ## Objective

    Determine if a medical product''s review period qualifies for patent term restoration.


    ## Output Format

    Formal eligibility assessment letter.'
- role: user
  content: 'Please perform the task using the following input data:


    <input>

    {{input}}

    </input>'
testData:
- input: Marketing approval date, patent number, and chronology. (Example data)
  expected: Expected output as per instructions.
evaluators:
- name: Validation Check
  regex: (?i)Verify

```
