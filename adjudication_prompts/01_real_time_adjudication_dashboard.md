---
id: adjudication-real-time-dashboard
title: Real-Time Adjudication Visibility Dashboard
category: adjudication_prompts
author: fderuiter
created: 2025-07-18
last_modified: 2025-07-18
tested_model: gpt-4
temperature: 0.2
tags: [adjudication, dashboard]
---

# Real-Time Adjudication Visibility Dashboard

## Purpose

Design a dashboard that provides real-time visibility into clinical endpoint adjudication workflows.

## Context

- Phase III cardiovascular device study with ~950 suspected events across 120 sites.
- A blinded Clinical Events Committee adjudicates each event.
- Stakeholders need immediate insight into blocked events and next actions.

## Instructions
1. Draft a textual workflow diagram from site submission to final CEC decision.
1. Define the minimal data model for a role-based dashboard showing:
   - event aging in days
   - disagreement rate
   - percentage of dossiers missing required documents
   - adjudicator workload
1. List five automated alerts or reminders that reduce turnaround time.
1. Recommend two commercial or open-source eAdjudication platforms and justify the choice.

## Inputs

None

## Output Format

- **Section 1:** Workflow diagram
- **Section 2:** Dashboard data model (table)
- **Section 3:** Alert rules (bullets)
- **Section 4:** Platform recommendations (table)

## Additional Notes

Ask clarifying questions if any requirement is unclear before producing the dashboard description.
