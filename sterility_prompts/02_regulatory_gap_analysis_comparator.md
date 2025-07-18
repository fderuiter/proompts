---
id: regulatory-gap-analysis-comparator
title: Regulatory Gap-Analysis Comparator
category: sterility_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [regulatory, sterility]
---

# Regulatory Gap-Analysis Comparator

## Purpose
Compare sterility-assurance requirements for a Class III implantable device sterilized with vapor-phase hydrogen peroxide.

## Context
Act as a regulatory-affairs consultant reviewing these sources:
- FDA *Submission and Review of Sterility Information* (8 Jan 2024)
- **ISO 11137-1 : 2025**
- **ISO 22441 : 2022**
- **ISO 11737-2 : 2019**

## Instructions
1. Build a comparison table with rows for validation approach, load configuration, SAL definition, pyrogenicity, reprocessing, and labeling; columns represent each document.
2. Highlight any **gaps or divergences** and flag items that must appear in a 510(k).
3. Rank gaps by regulatory risk (High / Medium / Low) and recommend mitigation steps.
4. Use bold red text `**<text>**` for high-risk gaps.
5. Do not expose your chain of thought.

## Inputs
None

## Output Format
Markdown table followed by a short executive summary (≤ 200 words).

## Additional Notes
None
