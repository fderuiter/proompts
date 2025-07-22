---
id: site-level-supply-resupply-strategy
title: Forecast Site-Level Drug Supply & Resupply Strategy
category: rtsm_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [RTSM, supply]
---

# Forecast Site-Level Drug Supply & Resupply Strategy

## Purpose

Plan site-level drug supply and resupply for an adaptive trial.

## Context

You are a senior clinical supply planner specializing in RTSM forecasting algorithms. Key parameters:

- Trial: 18‑month adaptive dose‑escalation
- Sites: 28 across US/EU/APAC
- Average enrollment: 10 patients/site/month (Poisson λ = 10)
- Packaging: 2‑visit kits (28‑day supply)
- Lead times: 8 weeks manufacture + 2 weeks shipping
- Depot capacities: USA, Germany, Singapore
- Shelf‑life: 24 months, temperature‑controlled (2–8 °C)
- Preferred strategy: trigger‑based resupply

## Instructions

1. Calculate initial shipment quantities per site to maintain ≥95 % service level for the first six weeks.
1. Design an RTSM resupply algorithm (n‑threshold/percentage or predictive) balancing stock‑out risk ≤1 % and waste ≤10 %.
1. Present a timeline showing manufacturing start, depot release, and the first three automatic resupply points.
1. Provide a one‑paragraph rationale suitable for the Supply Plan appendix.

## Inputs

- `{{trial_enrollment}}` — actual enrollment data if available.

## Output Format

- Markdown table with rows = sites and columns = initial kits, reorder threshold, expected monthly consumption, and safety stock.
- Gantt‑style ASCII timeline.
- Concluding rationale paragraph.

## Additional Notes

Omit internal reasoning; provide only the final deliverable.
