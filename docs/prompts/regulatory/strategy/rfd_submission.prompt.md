---
title: Request for Designation (RFD) Submission
---

# Request for Designation (RFD) Submission

Draft RFD for combination products.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/regulatory/strategy/rfd_submission.prompt.yaml)

```yaml
---
name: Request for Designation (RFD) Submission
version: 0.1.0
description: Draft RFD for combination products.
metadata:
  domain: regulatory
  complexity: low
  tags:
  - regulatory-strategy
  - request
  - designation
  - rfd
  - submission
  requires_context: false
variables:
- name: product_desc
  description: The product or offering being discussed
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Regulatory Affairs Specialist. Draft a Request for Designation for a drug-eluting contact lens, identifying
    the drug component as the PMOA and recommending CDER as the lead review center. Adhere to 21 CFR Part 3.
- role: user
  content: 'Draft a Request for Designation for a drug-eluting contact lens, identifying the drug component as the PMOA and
    recommending CDER as the lead review center.


    Inputs:

    - `{{product_desc}}`


    Output format:

    Markdown RFD Letter.'
testData:
- input: 'product_desc: Contact lens releasing antihistamine.

    '
  expected: 'Request for Designation

    '
evaluators:
- name: Primary Mode of Action
  string:
    contains: Primary Mode of Action
- name: CDER
  string:
    contains: CDER

```
