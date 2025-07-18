---
id: second-order-thinking-oracle
title: "Second-Order Thinking Oracle"
category: productivity_prompts
author: codex
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.7
tags: [strategy, decision-making]
---

<!-- markdownlint-disable MD029 -->

# Second-Order Thinking Oracle

## Purpose

Assess first- and second-order effects of a decision.

## Context

The user wants a short analysis of expected outcomes over time.

## Instructions

1. Create a table with rows for Now, 6 months and 2 years.
1. Columns: First-Order Outcome (≤15 words) and Second-Order Consequence (≤20 words).
1. Rate the net strategic value from -5 to +5.
1. If the score is negative, provide a 40-word mitigation plan.

## Inputs

- `{{decision}}`: the decision under review.

## Output Format

Markdown table followed by the score and optional mitigation plan.

## Additional Notes

Keep the entire response under 140 words and use plain language.
