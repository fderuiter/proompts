---
id: operations-kpi-dashboard-review
title: KPI Dashboard & Monthly Ops-Review Pack
category: operations_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [operations, kpi]
---

# KPI Dashboard & Monthly Ops-Review Pack

## Purpose

Summarize operational performance and highlight required actions for the monthly review.

## Context

You are an operations-performance coach preparing the COO’s monthly review.
Latest KPI data for Q3 FY‑25 and strategic priorities are provided.

## Instructions

1. Identify the three KPIs furthest off‑target and explain their root causes.
2. Recommend corrective initiatives with RACI owner and due date.
3. Draft three narrative slides titled **State of Operations**, **Key Risks & Mitigations**, and **Next Steps** (up to five bullets each).
4. End with an **Ask** slide listing decisions needed from the executive team.

## Inputs

- `{{kpi_data}}` – CSV of recent KPIs.
- `{{strategic_priorities}}` – bullet list.

## Output Format

Markdown bullet lists for each slide.

## Additional Notes

Keep the briefing concise and action oriented.
