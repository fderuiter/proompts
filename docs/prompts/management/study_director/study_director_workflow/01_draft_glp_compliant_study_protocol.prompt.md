---
title: Draft a GLP-Compliant Study Protocol
---

# Draft a GLP-Compliant Study Protocol

Produce a detailed study plan that satisfies OECD and FDA GLP regulations.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/management/study_director/study_director_workflow/01_draft_glp_compliant_study_protocol.prompt.yaml)

```yaml
---
name: Draft a GLP-Compliant Study Protocol
version: 0.1.0
description: Produce a detailed study plan that satisfies OECD and FDA GLP regulations.
metadata:
  domain: management
  complexity: medium
  tags:
  - study-director
  - draft
  - glp-compliant
  - study
  - protocol
  requires_context: false
variables:
- name: protocol_basics
  description: any additional study parameters
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a senior toxicologist preparing a 28‑day oral toxicity study (OECD TG 407) in Sprague‑Dawley rats for
    Test Article X to support an IND.


    Reason step-by-step before writing but reveal only the final protocol.'
- role: user
  content: '1. Outline objectives and scientific rationale.

    2. Specify dose groups with rationale and mg kg⁻¹ day⁻¹ levels.

    3. Describe experimental design—n/group, randomization, critical endpoints, and interim kills.

    4. Provide a Gantt-style timeline of milestones.

    5. List quality-assurance checkpoints and record-keeping requirements.

    6. Summarize potential protocol pitfalls with up to five mitigation bullet points.


    Inputs:

    - `{{protocol_basics}}` – any additional study parameters


    Output Format:

    1. Numbered outline covering all requested sections

    2. CSV-ready risk-mitigation table with columns: Phase, Risk, Impact, Mitigation'
testData:
- input: "protocol_basics: |\n  Test Article: Compound A\n  Species: Sprague-Dawley rats\n  Duration: 28 days\n"
  expected: '1. Objectives and scientific rationale

    Phase,Risk,Impact,Mitigation

    '
evaluators:
- name: Includes mitigation table headers
  string:
    contains: Phase,Risk,Impact,Mitigation

```
