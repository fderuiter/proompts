---
title: Prepare Pathology Slides and Reporting Plan
---

# Prepare Pathology Slides and Reporting Plan

Plan slide preparation and review activities for a GLP cardiovascular stent study.

[View Source YAML](../../../../../prompts/scientific/pathology/pathology_study_workflow/03_slides_and_reporting_workflow.prompt.yaml)

```yaml
---
name: Prepare Pathology Slides and Reporting Plan
version: 0.1.0
description: Plan slide preparation and review activities for a GLP cardiovascular stent study.
metadata:
  domain: scientific
  complexity: medium
  tags:
  - pathology
  - prepare
  - slides
  - reporting
  - plan
  requires_context: false
variables:
- name: interface_evaluation
  description: The device-tissue interface evaluation from the previous step
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are designing a pathology workflow that assesses thrombogenicity, endothelialization, and neointimal formation.


    Plan slide preparation and review activities for a GLP cardiovascular stent study.'
- role: user
  content: "1. List histology slide types, stains, sampling locations, and imaging needs (e.g., SEM, plastic embedding).\n\
    1. Outline a slide transfer and peer-review schedule with key milestones such as gross review, processing, first pathologist\
    \ review, peer review, and sign-off.\n1. Present the information in two tables:\n   - **Slides, Stains & Imaging**\n \
    \  - **Pathology Review Workflow** with timelines in days post‑necropsy.\n\nInputs:\n- `{{interface_evaluation}}` – The\
    \ device-tissue interface evaluation from the previous step.\n\nBased on the provided evaluation, create a detailed plan\
    \ for slide preparation and reporting.\n\nOutput format:\nTwo Markdown tables as described above.\n\nAdditional notes:\n\
    Keep the schedule concise and GLP compliant."
testData: []
evaluators: []

```
