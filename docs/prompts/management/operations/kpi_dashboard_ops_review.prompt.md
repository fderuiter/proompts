---
title: KPI Dashboard & Monthly Ops-Review Pack
---

# KPI Dashboard & Monthly Ops-Review Pack

Summarize operational performance and highlight required actions for the monthly review.

[View Source YAML](../../../../prompts/management/operations/kpi_dashboard_ops_review.prompt.yaml)

```yaml
---
name: KPI Dashboard & Monthly Ops-Review Pack
version: 0.1.0
description: Summarize operational performance and highlight required actions for the monthly review.
metadata:
  domain: management
  complexity: medium
  tags:
  - operations
  - kpi
  - dashboard
  - monthly
  - ops-review
  requires_context: false
variables:
- name: kpi_data
  description: CSV of recent KPIs
  required: true
- name: strategic_priorities
  description: bullet list
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are an operations-performance coach preparing the COO’s monthly review.

    Latest KPI data for Q3 FY‑25 and strategic priorities are provided.


    1. Identify the three KPIs furthest off‑target and explain their root causes.

    2. Recommend corrective initiatives with RACI owner and due date.

    3. Draft three narrative slides titled **State of Operations**, **Key Risks & Mitigations**, and **Next Steps** (up to
    five bullets each).

    4. End with an **Ask** slide listing decisions needed from the executive team.


    Keep the briefing concise and action oriented.'
- role: user
  content: '- `{{kpi_data}}` – CSV of recent KPIs.

    - `{{strategic_priorities}}` – bullet list.


    Output format: Markdown bullet lists for each slide.'
testData: []
evaluators: []

```
