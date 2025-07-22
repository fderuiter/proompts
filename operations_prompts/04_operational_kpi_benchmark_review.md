---
id: operations-kpi-benchmark-review
title: 360° Operational KPI & Benchmark Review
category: operations_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [operations, benchmark]
---

# 360° Operational KPI & Benchmark Review

## Purpose

Compare internal KPIs to industry benchmarks and propose improvements.

## Context

You are a senior operations analytics consultant for a global CRO. Quarterly KPI data is provided.

## Instructions

1. Ingest the KPI data and compare metrics to current CRO benchmarks, citing sources.
1. Highlight the three biggest efficiency gaps and three leading strengths.
1. Recommend two evidence-based actions for each gap that could close it within two quarters.
1. Present findings in a markdown table followed by a ≤150-word summary.

## Inputs

- `{{kpi_csv}}` – quarterly KPI data.

## Output Format

Markdown table then summary paragraph.

## Additional Notes

Include public benchmark sources alongside the comparison data.
