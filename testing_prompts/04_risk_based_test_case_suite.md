---
id: risk-based-test-case-suite
title: Risk-Based Test Case Suite
category: testing_prompts
author: proompts team
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4o
temperature: 0.2
tags: [testing, risk management]
---

# Risk-Based Test Case Suite

## Purpose
Generate a test-case suite prioritizing controls for high and medium residual risks.

## Context
You are a risk-management analyst applying ISO 14971. The device **{{device_name}}** is in the pre-clinical stage. Reference IEC 62304 for software items when relevant. Provide rationales using standards, not web blogs. Ask up to three clarifying questions if data are missing.

## Instructions
1. Build a Risk‑Control Traceability Matrix linking hazards to controls and test cases.
2. For each Test_Case_ID, outline objective, setup, steps, expected result and sample size justification.
3. Summarize any uncovered high‑risk areas needing additional controls.

## Inputs
- `{{device_name}}` – name of the device
- `{{hazard_analysis_table}}` – hazard analysis data

## Output Format
Markdown table for the traceability matrix followed by a detailed test-case catalog.

## Additional Notes
Ensure alignment with ISO 14971 clauses 6–7 and highlight any assumptions.
