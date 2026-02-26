---
title: Compliance Gap Assessment
---

# Compliance Gap Assessment

Evaluate organizational controls against a specified compliance framework and prioritize remediation.

[View Source YAML](../../../../prompts/regulatory/strategy/compliance_gap_assessment.prompt.yaml)

```yaml
---
name: Compliance Gap Assessment
version: 0.1.0
description: Evaluate organizational controls against a specified compliance framework and prioritize remediation.
metadata:
  domain: regulatory
  complexity: high
  tags:
  - regulatory-strategy
  - compliance
  - gap
  - assessment
  requires_context: false
variables:
- name: EMPLOYEES
  description: The EMPLOYEES to use for this prompt
  required: true
- name: FRAMEWORK
  description: The FRAMEWORK to use for this prompt
  required: true
- name: RISK_APPETITE
  description: The RISK APPETITE to use for this prompt
  required: true
- name: controls
  description: framework control list
  required: true
- name: evidence_logs
  description: policies and evidence artifacts
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are an external compliance auditor specializing in `{{FRAMEWORK}}`. Appendix A contains the framework control
    list. Appendix B holds current policies, procedures, and evidence logs. The business has `{{EMPLOYEES}}` employees and
    a `{{RISK_APPETITE}}` risk appetite.


    Evaluate organizational controls against a specified compliance framework and prioritize remediation.'
- role: user
  content: "1. Build a gap matrix comparing Appendix A controls to Appendix B evidence with columns:\n   - Control ID and\
    \ description.\n   - Status (Implemented, Partially, Missing).\n   - Severity if missing (High/Medium/Low).\n   - Recommended\
    \ remediation action and owner.\n1. Highlight the top five high‑impact gaps.\n1. Suggest quick‑win remediations achievable\
    \ within 30 days.\n1. Propose KPIs to track remediation progress quarterly.\n\nInputs:\n- `{{controls}}` — framework control\
    \ list.\n- `{{evidence_logs}}` — policies and evidence artifacts.\n\nOutput format:\n```json\n\n{\n  \"gapMatrix\": [\
    \ ... ],\n  \"summary\": {\n    \"topGaps\": [ ... ],\n    \"quickWins\": [ ... ],\n    \"recommendedKpis\": [ ... ]\n\
    \  }\n}\n```\n\nUse camelCase keys.\n\nAdditional notes:\nBase severity on likelihood × impact. If evidence is older than\
    \ 12 months, mark status as Partially implemented. Request missing artifacts before final scoring."
testData: []
evaluators: []

```
