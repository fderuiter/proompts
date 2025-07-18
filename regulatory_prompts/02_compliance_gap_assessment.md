---
id: compliance-gap-assessment
title: Compliance Gap Assessment
category: regulatory_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [compliance, audit]
# Compliance Gap Assessment
---

## Purpose

Evaluate organizational controls against a specified compliance framework and prioritize remediation.

## Context

You are an external compliance auditor specializing in `{{FRAMEWORK}}`. Appendix A contains the framework control list. Appendix B holds current policies, procedures, and evidence logs. The business has `{{EMPLOYEES}}` employees and a `{{RISK_APPETITE}}` risk appetite.

## Instructions

1. Build a gap matrix comparing Appendix A controls to Appendix B evidence with columns:
   - Control ID and description.
   - Status (Implemented, Partially, Missing).
   - Severity if missing (High/Medium/Low).
   - Recommended remediation action and owner.
2. Highlight the top five high‑impact gaps.
3. Suggest quick‑win remediations achievable within 30 days.
4. Propose KPIs to track remediation progress quarterly.

## Inputs

- `{{controls}}` — framework control list.
- `{{evidence_logs}}` — policies and evidence artifacts.

## Output Format

```json
{
  "gapMatrix": [ ... ],
  "summary": {
    "topGaps": [ ... ],
    "quickWins": [ ... ],
    "recommendedKpis": [ ... ]
  }
}
```

Use camelCase keys.

## Additional Notes

Base severity on likelihood × impact. If evidence is older than 12 months, mark status as Partially implemented. Request missing artifacts before final scoring.
