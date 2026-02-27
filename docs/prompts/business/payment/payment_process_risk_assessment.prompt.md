---
title: Payment-Process Risk Assessment and Mitigation
---

# Payment-Process Risk Assessment and Mitigation

Identify weak points in the site-payment workflow and propose mitigations.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/business/payment/payment_process_risk_assessment.prompt.yaml)

```yaml
---
name: Payment-Process Risk Assessment and Mitigation
version: 0.1.0
description: Identify weak points in the site-payment workflow and propose mitigations.
metadata:
  domain: business
  complexity: medium
  tags:
  - payment
  - payment-process
  - risk
  - assessment
  - mitigation
  requires_context: false
variables:
- name: kpi_metrics
  description: key performance indicators and targets
  required: true
- name: technology_stack
  description: systems and tools in use
  required: true
- name: workflow_description
  description: description of current payment workflow
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a process‑improvement lead tasked with reducing payment errors and increasing transparency.


    Identify weak points in the site-payment workflow and propose mitigations.'
- role: user
  content: "1. Review the current workflow, KPI metrics, and technology stack.\n1. List the top five accuracy or transparency\
    \ risks and their root causes.\n1. For each risk, recommend one or two mitigations drawing on industry best practice (e.g.,\
    \ automated disbursements, real-time dashboards, milestone advances, blockchain audit trails).\n1. Prioritize mitigations\
    \ using a RICE or effort-vs-impact matrix.\n1. Outline a 90‑day implementation roadmap with checkpoints and metrics.\n\
    1. Use bullet lists and a text-based Gantt-style schedule.\n1. Ask clarifying questions if any workflow details are missing.\n\
    \n  Inputs:\n  - `{{workflow_description}}` – description of current payment workflow\n  - `{{kpi_metrics}}` – key performance\
    \ indicators and targets\n  - `{{technology_stack}}` – systems and tools in use\n\nOutput format:\nBullet lists for risks\
    \ and mitigations, followed by a plain-text roadmap table.\n\nAdditional notes:\nCite external benchmarks or stats where\
    \ relevant."
testData:
- workflow_description: Manual invoice tracking in spreadsheets
  kpi_metrics: 'error_rate: 5%'
  technology_stack: Excel; Email
  expected: risk
evaluators:
- name: Mentions risk in output
  string:
    contains: risk

```
