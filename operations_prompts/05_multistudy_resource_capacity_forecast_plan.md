---
id: operations-multistudy-capacity-plan
title: Multistudy Resource & Capacity Forecast Plan
category: operations_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [operations, capacity]
---

# Multistudy Resource & Capacity Forecast Plan

## Purpose

Outline a data-driven approach for forecasting resources across multiple upcoming trials.

## Context

You are a senior CRO resource-planning consultant. Twelve new Phase II/III trials are expected over the next nine months with varying FTE mixes and technology costs.

## Instructions

1. Show a step-by-step methodology with formulas for forecasting headcount and spend using historical utilization data.
1. Provide a sample RACI matrix for collaboration between Operations, Finance, HR and IT.
1. Suggest three automation opportunities to streamline capacity planning.

## Inputs

- `{{historical_utilization}}` – past FTE and spend data.

## Output Format

Section A: numbered steps (max seven).
Section B: markdown RACI table.
Section C: bullet list of automation ideas (≤25 words each).

## Additional Notes

Use workflow-optimization principles and emphasise data-driven decision making.
