---
title: PMA Supplement (CBE)
---

# PMA Supplement (CBE)

Draft a 'Special PMA Supplement - Changes Being Effected' for safety warnings.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/regulatory/submissions/pma_supplement_cbe.prompt.yaml)

```yaml
---
name: PMA Supplement (CBE)
version: 0.1.0
description: Draft a 'Special PMA Supplement - Changes Being Effected' for safety warnings.
metadata:
  domain: regulatory
  complexity: low
  tags:
  - submissions
  - pma
  - supplement
  - cbe
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

    21 CFR 814.39(d)


    ## Objective

    Draft a ''Special PMA Supplement - Changes Being Effected'' for safety warnings.


    ## Output Format

    Formal letter marked ''Special PMA Supplement—CBE''.'
- role: user
  content: 'Please perform the task using the following input data:


    <input>

    {{input}}

    </input>'
testData:
- input: New safety information and current labeling. (Example data)
  expected: Expected output as per instructions.
evaluators:
- name: Validation Check
  regex: (?i)Compare

```
