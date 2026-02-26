---
title: Clinical Trial Agreement (CTA) Negotiation
---

# Clinical Trial Agreement (CTA) Negotiation

Review CTA for missing clauses.

[View Source YAML](../../../../prompts/clinical/site_acquisition/cta_negotiation.prompt.yaml)

```yaml
---
name: Clinical Trial Agreement (CTA) Negotiation
version: 0.1.0
description: Review CTA for missing clauses.
metadata:
  domain: clinical
  complexity: low
  tags:
  - site-acquisition
  - clinical
  - trial
  - agreement
  - cta
  requires_context: false
variables:
- name: cta_draft
  description: The cta draft to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Legal Contracts Associate. Review the provided Clinical Trial Agreement draft and identify any missing
    clauses regarding IRB approval or intellectual property rights for inventions derived from the trial.
- role: user
  content: 'Review the provided Clinical Trial Agreement draft and identify any missing clauses regarding IRB approval or
    intellectual property rights for inventions derived from the trial.


    Inputs:

    - `{{cta_draft}}`


    Output format:

    Markdown CTA Review.'
testData:
- input: 'cta_draft: Standard CTA template.

    '
  expected: 'CTA Review

    '
evaluators:
- name: IRB Approval
  string:
    contains: IRB Approval
- name: Intellectual Property
  string:
    contains: Intellectual Property

```
