<!-- markdownlint-disable MD029 -->
---
id: strategic-consultant-swot
title: "Strategic Consultant SWOT"
category: executive_prompts
author: "OpenAI"
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.7
tags: [strategy, swot]
---

# Strategic Consultant SWOT

## Purpose

Provide a concise SWOT analysis and immediate roadmap.

## Context

The user will specify `{{business}}`.

## Instructions

1. Deliver a four-row table (Strengths, Weaknesses, Opportunities, Threats) with two bullets ≤ 15 words each.
1. Suggest three SMART actions that use strengths and opportunities while mitigating weaknesses and threats; each ≤ 25 words.
1. Add one KPI sentence the CEO should track.
1. Keep the entire reply under 120 words.

## Inputs

- `{{business}}`: organization under review.

## Output Format

Markdown table followed by numbered actions and KPI sentence.

## References

- Bizway
- U.S. Chamber of Commerce
