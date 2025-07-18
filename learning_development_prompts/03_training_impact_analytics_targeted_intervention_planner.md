---
id: ld-training-impact-analytics
title: Training Impact Analytics Planner
category: learning_development_prompts
author: prompt-team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [analytics, training]
---

# Training-Impact Analytics and Targeted Intervention Planner

## Purpose
Correlate training data with audit deviations and design interventions for high-risk learners.

## Context
You are acting as a learning data scientist for a mid-size global CRO. Available data includes:
- 18 months of LMS records (course IDs, completion dates, assessment scores, time-in-module).
- Monthly audit findings with counts and categories of GCP deviations per study.
- Employee metadata such as role, tenure, and geography.

## Instructions
1. Provide a data-prep checklist covering cleansing and feature engineering.
2. Propose two predictive model options and explain their pros and cons.
3. Create a visualization storyboard showing insights for executives and managers.
4. Outline an action framework with automated nudges, remedial micro-courses, and mentor assignments.
5. Emphasize privacy (GDPR) and small-sample precautions.
6. Reference at least one open-source Python library for each step.
7. Think through potential confounders before proposing models.

## Inputs
- `{{analysis_goal}}` – specific compliance or performance metric to improve.

## Output Format
Ordered list summarizing each step; include SQL or pseudocode snippets where helpful.

## Additional Notes
Keep recommendations concise and grounded in the provided dataset.
