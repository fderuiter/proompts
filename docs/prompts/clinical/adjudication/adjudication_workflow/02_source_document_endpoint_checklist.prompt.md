---
title: Source Document and Endpoint Checklist
---

# Source Document and Endpoint Checklist

Create a clear checklist of required documents and endpoint criteria for clinical adjudication.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/clinical/adjudication/adjudication_workflow/02_source_document_endpoint_checklist.prompt.yaml)

```yaml
---
name: Source Document and Endpoint Checklist
version: 0.1.0
description: Create a clear checklist of required documents and endpoint criteria for clinical adjudication.
metadata:
  domain: clinical
  complexity: medium
  tags:
  - adjudication
  - source
  - document
  - endpoint
  - checklist
  requires_context: true
variables:
- name: charter_excerpt
  description: relevant sections of the adjudication charter
  required: true
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: '- Draft adjudication charter lists seven primary endpoints but lacks detail on required source documents.

    - Adjudicators previously received incomplete packages.


    Ask any clarifying questions before generating the checklist.'
- role: user
  content: '1. For each endpoint, build a checklist of required documents including imaging, labs, and narrative notes with
    formatting rules.

    2. Convert each endpoint definition into binary inclusion or exclusion criteria.

    3. Suggest concise form-field wording (≤50 characters) for EDC alignment.

    4. Flag ambiguous language in the draft charter that needs clarification from the sponsor.


    Inputs:

    - `{{charter_excerpt}}` – relevant sections of the adjudication charter.


    Output format:

    - Markdown table per endpoint with columns: *Doc Type*, *Required?*, *Acceptable Formats*, *Notes*.

    - Numbered list of **Clarification Needed** items.'
testData:
- vars:
    charter_excerpt: example_charter_excerpt
  expected: '- Markdown table per endpoint with columns: *Doc Type*, *Required?*, *Acceptable Formats*, *Notes*.

    - Numbered list of **Clarification Needed** items.'
evaluators:
- name: Output includes 'Clarification Needed'
  string:
    contains: Clarification Needed

```
