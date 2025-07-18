---
id: eto-sterilization-process-fmea
title: EtO Sterilization Process FMEA
category: sterility_prompts
author: proompts
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [sterility, risk analysis]
---

# EtO Sterilization Process FMEA

## Purpose

Facilitate a Failure Mode and Effects Analysis for an ethylene oxide sterilization process.

## Context

You are a sterility-risk analyst reviewing a Category A EtO process for a multilumen catheter.

## Instructions

- List each unit-operation step from preconditioning to aeration.
- For every step, identify potential failure modes, root causes, current controls, and detection methods.
- Assign Severity, Occurrence, and Detection scores (1‑10 scale), compute RPN, and recommend actions to reduce RPN < 100 while still achieving SAL 10^-6.
- Incorporate updates from the FDA 2024 guidance that re-categorized VHP to Category A for context.

## Inputs

- `{{process_description}}` – overview of the EtO sterilization process.

## Output Format

Sortable Markdown table with columns: Step \| Failure Mode \| Cause \| S \| O \| D \| RPN \| Mitigation, followed by a bullet list summary of the three highest-risk failures.

## Additional Notes

Think step-by-step internally and share only the finished FMEA table and summary.
