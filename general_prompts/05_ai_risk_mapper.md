---
id: ai-risk-mapper
title: AI Risk Mapper
category: general_prompts
author: Codex
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [risk, compliance]
---

# AI Risk Mapper

## Purpose

Create a quick-look risk register for a specified AI system.

## Context

Regulatory frameworks such as the EU AI Act and NIST AI RMF guide responsible AI deployment.

## Instructions

1. List up to six key risks, each no more than 12 words.
1. Provide a table with columns *Risk*, *Likelihood H/M/L*, *Impact H/M/L*, and *Mitigation* (≤ 15 words).
1. Conclude with a 25-word compliance note referencing the EU AI Act and NIST AI RMF.
1. Keep total response under 150 words.

## Inputs

- `{{AI_SYSTEM}}` — the system being assessed.

## Output Format

Markdown list, table, and concluding note.

## Additional Notes

Focus on brevity and clarity.

## References

Reuters, Osano
