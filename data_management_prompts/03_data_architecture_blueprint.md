---
id: data-architecture-blueprint
title: Data Architecture Blueprint
category: data_management_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [architecture, planning]
---

# Data Architecture Blueprint

Title: Recommend Scalable Data Architecture

Role: Enterprise Data-Architect Advisor

Task:

- Compare at least three target architectures.
- For each, outline storage layer, compute engine, governance tooling and estimated 3-year TCO.
- Recommend the best fit with a decision matrix covering scalability, cost, team fit and vendor lock-in.
- List the first five migration milestones with rough durations.
- Ask clarifying questions if assumptions are unclear.

Context:
"""
Current stack: on-prem SQL Server with nightly ETL to S3.
Forecast: 10× data growth over 18 months requiring low-latency ML serving.
Budget: $250k capex + $6k/mo opex.
"""

Constraints:

- Provide decision matrix in Markdown.
- Follow with a Gantt-style milestone table.

## Output Format

Markdown
