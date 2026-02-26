---
title: Regulatory-Change Impact Analysis
---

# Regulatory-Change Impact Analysis

Assess how a new regulation affects company operations and outline a phased response plan.

[View Source YAML](../../../../prompts/regulatory/strategy/regulatory_change_impact_analysis.prompt.yaml)

```yaml
---
name: Regulatory-Change Impact Analysis
version: 0.1.0
description: Assess how a new regulation affects company operations and outline a phased response plan.
metadata:
  domain: regulatory
  complexity: high
  tags:
  - regulatory-strategy
  - regulatory-change
  - impact
  - analysis
  requires_context: true
variables:
- name: COMPANY
  description: The company or organization name
  required: true
- name: EFFECTIVE_DATE
  description: The EFFECTIVE DATE to use for this prompt
  required: true
- name: INDUSTRY_AND_REGION
  description: The industry or sector
  required: true
- name: REGULATION_NAME
  description: The name or identifier
  required: true
- name: company_profile
  description: overview of operations and locations
  required: true
- name: regulation_text
  description: full regulation content
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a senior regulatory‑affairs analyst for `{{COMPANY}}` operating in `{{INDUSTRY_AND_REGION}}`. The regulation
    "`{{REGULATION_NAME}}`" takes effect on `{{EFFECTIVE_DATE}}`; its full text is provided.


    Assess how a new regulation affects company operations and outline a phased response plan.'
- role: user
  content: '1. Summarize the regulation’s purpose and five most business‑critical obligations in ≤150 words.

    1. Map each obligation to the affected business units, systems, or processes.

    1. Rate the compliance effort (Low/Medium/High) and non‑compliance risk (Low/Medium/High) for each obligation.

    1. Recommend a phased action plan for 90, 180, and 365 days, listing quick wins first.

    1. Flag any ambiguities or information still needed.


    Inputs:

    - `{{regulation_text}}` — full regulation content.

    - `{{company_profile}}` — overview of operations and locations.


    Output format:

    Markdown report with sections:


    - Executive Summary

    - Obligation‑to‑Process Map (bullet list)

    - Effort & Risk Matrix (table)

    - Phased Action Plan (check‑box list)

    - Open Questions / Information Gaps


    Additional notes:

    Write in plain English for time‑pressed executives. Cite article or section numbers. Ask up to three clarifying questions
    if essential details are missing.'
testData: []
evaluators: []

```
