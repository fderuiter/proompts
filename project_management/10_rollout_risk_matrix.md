---
id: pm-rollout-risk-matrix
title: Rollout Risk Matrix
category: project_management
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [project management, risk]
---

# Rollout Risk Matrix

## Purpose

Assess rollout risks and propose key mitigation actions.

## Context

You are planning the deployment of project X and need a quick risk overview.

## Instructions

1. List up to 10 identified risks as bullet points.
1. Convert them into a 3×3 risk-matrix table where rows represent Likelihood (Low/Med/High) and columns represent Impact (Low/Med/High). Mark each cell with the applicable risk labels.
1. After the matrix, propose the top two mitigation actions in 35 words or fewer each, citing which risks they address.
1. Keep the total answer under 250 words and prioritize implementation.

## Inputs

- `{{risk_list}}`

## Output Format

Markdown table followed by short mitigation actions.

## Additional Notes

Keep explanations minimal and implementation-focused.
