---
title: Risk-Based Quality Management Plan
---

# Risk-Based Quality Management Plan

Create a concise RBQM plan for a first‑in‑human Phase I healthy‑volunteer study.

[View Source YAML](../../../../prompts/regulatory/quality/risk_based_quality_management_plan.prompt.yaml)

```yaml
---
name: Risk-Based Quality Management Plan
version: 0.1.0
description: Create a concise RBQM plan for a first‑in‑human Phase I healthy‑volunteer study.
metadata:
  domain: regulatory
  complexity: medium
  tags:
  - quality
  - risk-based
  - management
  - plan
  requires_context: true
variables:
- name: study_overview
  description: summary of the Phase I trial
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You lead RBQM design and must align with ICH E6(R2)/E8(R1) and FDA risk‑based monitoring guidance.


    Create a concise RBQM plan for a first‑in‑human Phase I healthy‑volunteer study.'
- role: user
  content: '1. Include at least five Critical‑to‑Quality factors.

    1. Provide a risk‑assessment matrix (Severity × Likelihood) with mitigations.

    1. Define Key Risk Indicators with thresholds for centralized monitoring.

    1. Specify roles, data sources, and review frequency.

    1. Outline the escalation and communication pathway.


    Inputs:

    - `{{study_overview}}` — summary of the Phase I trial.


    Output format:

    Numbered sections with a table for the risk matrix, written in plain language. Conclude with a paragraph explaining how
    the plan supports subject safety, data integrity, and inspection readiness.


    Additional notes:

    Ensure guidance references are explicit where relevant.


    <!-- markdownlint-enable MD029 MD036 -->'
testData: []
evaluators: []

```
