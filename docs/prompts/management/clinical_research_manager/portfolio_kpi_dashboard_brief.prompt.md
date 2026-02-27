---
title: Portfolio KPI Dashboard Brief
---

# Portfolio KPI Dashboard Brief

Produce a one-page executive dashboard of enrollment, deviation, SDV, and budget KPIs for live studies.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/management/clinical_research_manager/portfolio_kpi_dashboard_brief.prompt.yaml)

```yaml
---
name: Portfolio KPI Dashboard Brief
version: 0.1.0
description: Produce a one-page executive dashboard of enrollment, deviation, SDV, and budget KPIs for live studies.
metadata:
  domain: management
  complexity: medium
  tags:
  - clinical-research-management
  - portfolio
  - kpi
  - dashboard
  - brief
  requires_context: false
variables:
- name: input
  description: The primary input or query text for the prompt
  required: true
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: "You are a data-driven clinical-project manager.\nTask: Produce a one-page executive dashboard summarizing operational\
    \ KPIs for my live studies (IDs [XYZ-01, XYZ-02, XYZ-03]).\nMetrics: enrollment rate vs. plan, screen-failure %, protocol\
    \ deviations/site, SDV completion %, query turnaround time, and budget burn %.\nConstraints & style:\n • Snapshot date\
    \ — [EOD July 18 2025].\n • Traffic-light coding: Green ≥ 90 % target, Yellow 80-89 %, Red < 80 %.\n • Deliver in Markdown\
    \ with a summary paragraph of top 3 risks.\n • Embed clarifying-questions section at top if data gaps exist.\nOutput:\
    \ Markdown table + risk narrative only.\n```"
- role: user
  content: '{{input}}'
testData:
- input: Dashboard request acknowledged.
  expected: XYZ-01
evaluators:
- name: Mentions study ID
  string:
    contains: XYZ-01

```
