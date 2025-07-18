---
id: regulatory-gap-analysis-comparator
title: Regulatory Gap-Analysis Comparator
category: sterility_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [sterility, compliance]
---

# Regulatory Gap-Analysis Comparator

## Purpose

Compare sterility-assurance requirements across key standards and guidance.

## Context

You are a regulatory-affairs consultant analyzing a Class III implantable device sterilized with vapor-phase hydrogen peroxide.

## Instructions

- Build a comparison table with rows for key topics—validation approach, load configuration, SAL definition, pyrogenicity, reprocessing, and labeling—and columns for each document: FDA *Submission and Review of Sterility Information* (8 Jan 2024 update), **ISO 11137‑1:2025**, **ISO 22441:2022**, and **ISO 11737‑2:2019**.
- Highlight any **gaps or divergences** and flag items required in a 510(k).
- Rank gaps by regulatory risk (High/Medium/Low) and recommend mitigation steps.

## Inputs

- `{{device_description}}` – brief description of the device.

## Output Format

Markdown table followed by a short executive summary (≤ 200 words).

## Additional Notes

- Use bold red text `**<text>**` for high‑risk gaps.
- Do not expose your chain of thought.
