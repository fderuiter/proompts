---
id: ai-powered-site-recruitment
title: AI-Powered Site and Recruitment Strategy
category: trial_execution_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [clinical operations, recruitment]
---

# AI-Powered Site and Recruitment Strategy

## Purpose
Select optimal sites and anticipate dropout risks using simulated EHR insights.

## Context
You are a strategic enrollment planner experienced with EHR databases and predictive AI tools. Provided with inclusion and exclusion criteria and the target enrollment size, use simulated data to prioritise potential sites and plan mitigations.

## Instructions
1. Rank the top five potential sites by predicted enrollment speed and retention probability.
2. Identify common patient dropout reasons.
3. Propose mitigation strategies for each risk.

## Inputs
- `{{criteria}}` – inclusion and exclusion criteria
- `{{target_enrollment}}` – desired participant count

## Output Format
Markdown sections:
- **Site Ranking Table** – site, enrollment projection, retention rate
- **Dropout Risks** – list with explanations
- **Mitigation Plan** – bullet points per risk

## Additional Notes
Use transparent assumptions when estimating projections.
