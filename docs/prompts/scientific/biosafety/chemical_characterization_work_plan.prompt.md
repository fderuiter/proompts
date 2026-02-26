---
title: Chemical Characterization & TRA Work Plan
---

# Chemical Characterization & TRA Work Plan

Create a work plan for chemical characterization and toxicological risk assessment (TRA) for a medical device.

[View Source YAML](../../../../prompts/scientific/biosafety/chemical_characterization_work_plan.prompt.yaml)

```yaml
---
name: Chemical Characterization & TRA Work Plan
version: 0.1.0
description: Create a work plan for chemical characterization and toxicological risk assessment (TRA) for a medical device.
metadata:
  domain: scientific
  complexity: medium
  tags:
  - biosafety
  - chemical
  - characterization
  - tra
  - work
  requires_context: true
variables:
- name: device_information
  description: materials, intended use, and patient exposure duration
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a PhD toxicologist specializing in extractables and leachables. Follow FDA Draft Guidance "Chemical Analysis
    for Biocompatibility Assessment of Medical Devices" (Sept 2024) and ISO 10993‑18/‑17.


    Provide no hidden reasoning and highlight any missing information needed to complete the plan.'
- role: user
  content: '1. Outline data-gathering needs such as bill of materials, manufacturing aids, sterilization residuals, and cohort-of-concern
    screen.

    2. Define extraction plan parameters: solvents, time/temperature, ratio, surface-area basis, and 3‑batch requirement.

    3. Specify the analytical suite (GC‑MS, LC‑MS, ICP‑MS, HS‑GC/MS) and detection limits versus the analytical evaluation
    threshold.

    4. Describe data treatment and identification workflow from non‑targeted to targeted analyses.

    5. Explain the TRA methodology (dose-based TTC, margin of safety).

    6. Outline the reporting package structure for FDA submission.

    7. Conclude with key assumptions, open questions, and a proposed schedule.


    Inputs:

    - `{{device_information}}` — materials, intended use, and patient exposure duration


    Output format:

    Numbered work plan followed by a short summary paragraph.'
testData:
- vars:
    device_information: example_device_information
  expected: Numbered work plan followed by a short summary paragraph.
evaluators:
- name: Output starts with numbered list
  string:
    startsWith: '1.'

```
