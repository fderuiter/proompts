<!-- markdownlint-disable MD029 -->
---
id: market-report-exec-summary
title: Market Report Executive Summary
category: market_research_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [summary, market, self-critique]
# Market Report Executive Summary
---

## Purpose
Draft and refine an executive summary for the uploaded market report.

## Context
You are a self-optimizing AI analyst.

## Instructions
1. Produce a first-pass summary in 150 words or less.
2. Critique the draft in no more than 75 words focusing on clarity, insights and bias.
3. Rewrite completely, fixing every issue and marking additions **in bold**.
4. Conclude with a 12-word reflection on what changed.
5. Use numbered headings: 1. Initial Summary, 2. Critique, 3. Final Summary.

## Inputs
- `{{market_report}}` – full report text or attachment

## Output Format
Markdown sections for each step.

## Additional Notes
Keep sections concise and label the final version clearly.
