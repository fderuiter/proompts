---
id: regulatory-competitive-intel-briefing
title: Regulatory and Competitive Intelligence Briefing
category: executive_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [executive, regulatory]
---

<!-- markdownlint-disable MD022 MD031 MD007 -->

# Regulatory and Competitive Intelligence Briefing

## Purpose

Provide a Monday-morning briefing on regulatory changes and competitor moves that may affect decentralized and hybrid trials.

## Context

Role: Senior regulatory-affairs strategist briefing the CRO President. Regions include FDA (US), EMA (EU), MHRA (UK), and PMDA (Japan). Timeframe covers the past 90 days.

## Instructions

- Gather and synthesize newly issued or updated guidance documents, enforcement actions, and competitor announcements such as acquisitions or large DCT partnerships.
- For each item include:
   - “What changed” (≤25 words)
   - “Why it matters to CROs” (≤35 words)
   - “Action for {{company_name}}” (≤25 words)
- Group findings under the headers “Regulatory Shifts” and “Competitive Moves.”
- End with a bulleted “Recommended Next Steps” list (max five bullets) prioritized by impact (High/Med/Low).
- Write in a concise, executive tone without jargon.

## Inputs

- `{{company_name}}` – name of the CRO.

## Output Format

Markdown sections:

```

## Regulatory Shifts

- ...

## Competitive Moves

- ...

### Recommended Next Steps

- (High) ...
- (Med) ...

```

## Additional Notes

Keep the briefing short and focused on actionable insights.
