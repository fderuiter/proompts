---
id: protocol-optimization-risk-simulation
title: Protocol Optimization and Risk Simulation
category: trial_execution_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [clinical operations, planning]
---

# Protocol Optimization and Risk Simulation

## Purpose

Evaluate a draft clinical protocol and simulate the effects of simplifying key elements.

## Context

You are a clinical operations expert with extensive experience in protocol design and risk management. Review the protocol to identify operational bottlenecks such as site activation delays, complex eligibility requirements or data collection challenges. Then simulate outcomes under two scenarios: reducing eligibility criteria by 20 % and consolidating data collection points by 30 %.

## Instructions

1. Summarize the main operational bottlenecks.
1. For Scenario 1, estimate the impact on timeline, enrollment rate and budget.
1. For Scenario 2, estimate the same metrics.
1. Provide recommendations with quantified justification for each change.

## Inputs

- `{{draft_protocol}}` – proposed protocol text

## Output Format

Markdown sections:

- **Section A:** Bottlenecks
- **Section B:** Scenario 1 – metrics and narrative
- **Section C:** Scenario 2 – metrics and narrative
- **Section D:** Recommendations

## Additional Notes

Use data‑driven assumptions when estimating impact.
