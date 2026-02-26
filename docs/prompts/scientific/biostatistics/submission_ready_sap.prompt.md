---
title: Submission-Ready Statistical Analysis Plan
---

# Submission-Ready Statistical Analysis Plan

Generate sections of a submission-ready statistical analysis plan.

[View Source YAML](../../../../prompts/scientific/biostatistics/submission_ready_sap.prompt.yaml)

```yaml
---
name: Submission-Ready Statistical Analysis Plan
version: 0.1.0
description: Generate sections of a submission-ready statistical analysis plan.
metadata:
  domain: scientific
  complexity: medium
  tags:
  - biostatistics
  - submission-ready
  - statistical
  - analysis
  - plan
  requires_context: false
variables:
- name: study_overview
  description: The study overview to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are an expert CRO biostatistician writing FDA- and EMA-compliant SAPs. The study is a Phase IIb adaptive dose-ranging
    trial in NASH with five arms (≈250 participants). Primary endpoint: change in ALT from baseline to Week 24.


    Ensure language is concise and submission ready.'
- role: user
  content: "1. Draft Sections 1–8 of the SAP template:\n   - Title page and administrative details\n   - Study objectives\
    \ and hypotheses\n   - Study design overview with schematic\n   - Analysis populations and handling of protocol deviations\n\
    \   - Endpoints and estimands per ICH E9(R1)\n   - Statistical methods (models, covariance structure, interim rules)\n\
    \   - Missing-data strategy (MI with δ-adjustment sensitivity)\n   - Mock TLF shells (summary stats and forest-plot layout)\n\
    2. Use numbered H2 headings.\n3. Keep each subsection ≤250 words.\n4. Present mock tables/figures as markdown tables with\
    \ placeholder cells.\n5. Do not include internal reasoning steps.\n\nInputs:\n- `{{study_overview}}`\n\nOutput format:\n\
    Markdown document with numbered sections and mock tables."
testData:
- vars:
    study_overview: example_study_overview
  expected: Markdown document with numbered sections and mock tables.
evaluators:
- name: Output starts with '## 1'
  string:
    startsWith: '## 1'

```
