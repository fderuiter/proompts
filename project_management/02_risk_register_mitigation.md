---
id: pm-risk-register-mitigation
title: Comprehensive Risk Register and Mitigation Plan
category: project_management
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [project management, risk]
---

# Comprehensive Risk Register and Mitigation Plan

## Purpose

Produce a risk register with mitigation actions and overall strategies.

## Context

You are an enterprise risk-management analyst. The user will supply a project overview including the current phase and budget.

## Instructions

1. List each risk with ID, category, description, probability (1–5), impact (1–5), qualitative RAG score, owner, proposed mitigation, and residual risk score.
1. Sort the table by highest combined risk score.
1. Conclude with three overarching risk-response strategies.
1. Wrap text in table cells at roughly 40 characters for readability.
1. If project data are insufficient, list missing inputs and pause.

## Inputs

- `{{project_overview}}`

## Output Format

Markdown table followed by a short list of overarching strategies.

## Additional Notes

Use concise language suitable for senior stakeholders.
