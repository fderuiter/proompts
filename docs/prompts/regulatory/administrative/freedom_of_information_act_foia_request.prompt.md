---
title: Freedom of Information Act (FOIA) Request
---

# Freedom of Information Act (FOIA) Request

Draft a request for records regarding a specific 510(k) clearance.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/regulatory/administrative/freedom_of_information_act_foia_request.prompt.yaml)

```yaml
---
name: Freedom of Information Act (FOIA) Request
version: 0.1.0
description: Draft a request for records regarding a specific 510(k) clearance.
metadata:
  domain: regulatory
  complexity: low
  tags:
  - regulatory-admin
  - freedom
  - information
  - act
  - foia
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

    21 CFR Part 20


    ## Objective

    Draft a request for records regarding a specific 510(k) clearance.


    ## Output Format

    Formal letter following 21 CFR 20.40.'
- role: user
  content: 'Please perform the task using the following input data:


    <input>

    {{input}}

    </input>'
testData:
- input: Description of records sought and requester contact information. (Example data)
  expected: Expected output as per instructions.
evaluators:
- name: Validation Check
  regex: (?i)Check

```
