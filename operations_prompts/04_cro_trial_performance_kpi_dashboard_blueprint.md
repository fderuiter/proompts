---
id: operations-cro-kpi-dashboard-blueprint
title: CRO Trial-Performance KPI Dashboard Blueprint
category: operations_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [operations, dashboard]
---

# CRO Trial-Performance KPI Dashboard Blueprint

## Purpose

Outline metrics and visuals for a CRO trial-performance dashboard.

## Context

You are an expert clinical-trial operations analyst. Leadership needs a Power BI or Excel dashboard showing pipeline flow, start-up timing, enrollment velocity and budget adherence across 35 sites.

## Instructions

1. List 10‑12 actionable KPIs with definition, formula, data source and refresh cadence.
1. Recommend the best visual for each KPI and justify the choice in one sentence.
1. Flag any data-quality risks or required system integrations.

## Inputs

- `{{portfolio_summary}}` – snapshot of active studies.

## Output Format

Markdown table with columns `KPI \| Formula \| Visual \| Data Source \| Refresh Cadence \| Notes`.

## Additional Notes

Prioritize metrics sponsors value and keep explanations under 40 words per bullet. Dashboard clarity influences site selection and revenue growth.
