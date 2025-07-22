---
id: risk-based-monitoring-sop
title: Create a Risk-Based Monitoring & Mitigation SOP for RTSM
category: rtsm_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [RTSM, SOP]
---

# Create a Risk-Based Monitoring & Mitigation SOP for RTSM

## Purpose

Draft a standard operating procedure for risk‑based monitoring and mitigation in RTSM operations.

## Context

You are a GxP compliance officer. Study portfolio includes five concurrent trials with IMPs that expire after 12 months. Integrated systems: RTSM ↔ EDC ↔ temperature‑monitoring IoT. Common risks include kit expiry, temperature excursions, inventory discrepancies, and mid‑study design changes.

## Instructions

1. List the top ten RTSM operational risks ranked by severity × likelihood.
1. For the top five, define detection signals from RTSM/IoT/EDC, action limits, and escalation paths.
1. Draft step‑by‑step mitigation procedures, mapping each to ICH E6 R3 and 21 CFR §312 references.
1. Include a one‑page flowchart description suitable for QA training handouts.

## Inputs

- `{{existing_sop}}` — any current procedures.

## Output Format

- Two‑column markdown table: Risk \| Detection & Escalation Path.
- Numbered mitigation procedures (≤150 words each).
- Text description of the flowchart for later diagramming.
- Provide only the final SOP content.

## Additional Notes

Avoid internal reasoning in the output.
