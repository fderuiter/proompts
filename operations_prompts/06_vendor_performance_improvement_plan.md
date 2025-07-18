---
id: operations-vendor-performance-plan
title: Risk-Based Vendor Performance Improvement Plan
category: operations_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [operations, vendors]
---

# Risk-Based Vendor Performance Improvement Plan

## Purpose

Raise overall vendor performance and reduce operational risk.

## Context

You are the Director of Business Operations for a CRO relying on fourteen preferred vendors covering labs, imaging, central IRB and eCOA.
Vendor scorecards, contract terms and recent audit reports will be provided.

## Instructions

1. Cluster vendors into performance tiers using appropriate clustering on scorecard metrics.
2. For each tier, propose immediate corrective actions (≤30 days) and longer-term changes (31‑90 days) with owner and success metric.
3. Identify systemic causes such as workflow gaps and recommend enterprise-level fixes.
4. Present a markdown table showing `Vendor | Tier | Key Action | Owner | Target Date` followed by a brief narrative under 150 words summarizing ROI and risk reduction.

## Inputs

- `{{vendor_scorecards}}` – performance metrics.
- `{{contract_terms}}` – key obligations and SLAs.
- `{{audit_reports}}` – recent QA findings.

## Output Format

Markdown table plus narrative paragraph.

## Additional Notes

Use a direct, prescriptive style. Request missing data before proceeding and think step by step.
