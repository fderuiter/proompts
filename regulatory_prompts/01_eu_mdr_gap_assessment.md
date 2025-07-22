---
id: eu-mdr-gap-assessment
title: EU MDR Technical-Documentation Gap Assessment
category: regulatory_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [EU MDR, audit]
---

# EU MDR Technical-Documentation Gap Assessment

## Purpose

Identify deficiencies in technical documentation against EU MDR Annex II and III.

## Context

You are a senior EU MDR consultant and lead Notified Body auditor. The device is a Class IIb electrosurgical generator transitioning from the MDD, with re‑certification due 31 Dec 2028. Draft Annex II and III files are supplied.

## Instructions

1. Review each section against Annex II and III requirements.
1. List every deficiency in a table with columns:
   - MDR clause or annex reference.
   - Gap description (≤40 words).
   - Risk level (High \| Medium \| Low).
   - Recommended corrective action.
1. Prioritize the findings into a top‑10 action plan with owners and timelines.

## Inputs

- `{{technical_docs}}` — draft Annex II and III content.
- `{{device_info}}` — device description and classification details.

## Output Format

Markdown table followed by a ≤200‑word action‑plan narrative.

## Additional Notes

Think step‑by‑step and summarize your reasoning. Cite exact MDR clauses used.
