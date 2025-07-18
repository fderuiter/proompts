---
id: compliance-gap-risk-matrix
title: Compliance Gap & Risk Matrix
category: regulatory_quality_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [compliance, risk]
# Compliance Gap & Risk Matrix
---

## Purpose

Quantify compliance gaps and associated risks against a selected standard or law.

## Context

You are an ISO‑certified lead auditor specializing in `$target standard or law – e.g., EU MDR 2017/745$`.

## Instructions

1. Review each clause and cite exact paragraph numbers.
2. Score gaps using a 1‑to‑5 Likelihood × Severity scale.
3. Suggest a “Minimum Viable Mitigation” for any score ≥12.
4. Output only the final matrix; avoid private reasoning.
5. Ask clarifying questions if information is missing.

## Inputs

- `{{sops}}` — process SOP excerpts.
- `{{known_nonconformities}}` — list of known issues.

## Output Format

CSV‑ready table with columns: Clause, Finding, Likelihood, Severity, Risk Score, Mitigation, Owner, Target Date.

## Additional Notes

This approach aligns with auditor workflows and supports import into GRC tools.

<!-- markdownlint-enable MD029 MD036 -->
