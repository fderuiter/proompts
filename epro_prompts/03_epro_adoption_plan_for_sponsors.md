---
id: epro-adoption-plan-for-sponsors
title: ePRO Adoption Plan for Sponsors
category: epro_prompts
author: Frederick de Ruiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [epro, adoption]
---

# ePRO Adoption Plan for Sponsors

## Purpose

Outline a six-month plan for rolling out ePRO across multiple sites.

## Context

You are an eClinical program manager. The sponsor is implementing ePRO across five global sites and needs guidance on device strategy, integration points, training, and metrics.

## Instructions

1. Provide a timeline with milestones for vendor selection, UAT, IRB approval, and training.
1. List criteria for choosing between BYOD and provisioned devices.
1. Detail coordination steps for integrating with EDC/IWRS and reconciling data.
1. Summarize patient training materials and components for a site support guide.
1. Recommend metrics to monitor (compliance rate, missing data, time-to-entry) and how to use them for iteration.

## Inputs

- `{{sites}}` – list of participating sites and regions.

## Output Format

Structured timeline followed by bullet points for each instruction.

## Additional Notes

Highlight risks such as varying site readiness or device availability.
