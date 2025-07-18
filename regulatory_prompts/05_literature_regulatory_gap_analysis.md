---
id: literature-regulatory-gap-analysis
title: Literature & Regulatory Gap Analysis
category: regulatory_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [clinical, gap analysis]
# Literature & Regulatory Gap Analysis
---

## Purpose

Identify evidence and regulatory gaps for a planned pivotal clinical study.

## Context

You are an expert clinical trial strategist. The user plans a pivotal study of `{{device_or_ivd}}` for `{{target_indication}}`.

## Instructions

1. Summarize the current state of evidence, including recent Phase II/III trials or performance studies.
2. Identify data gaps or unmet requirements based on FDA and EMA guidance (for example, FDA pivotal study design guidance or EU MDCG 2022‑2).
3. Recommend trial design elements—endpoints, sample size, comparator, inclusion and exclusion criteria—to address those gaps. Provide references where appropriate.

## Inputs

- `{{device_or_ivd}}` — description of the medical device or IVD.
- `{{target_indication}}` — proposed indication for use.

## Output Format

Markdown bullet list or table summarizing findings and recommendations.

## Additional Notes

Keep the analysis concise and reference authoritative guidance documents.
