---
id: patient-centered-randomization-scheme
title: Design a Patient-Centered Randomization Scheme
category: rtsm_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [RTSM, randomization]
# Design a Patient-Centered Randomization Scheme
---

## Purpose

Create a randomization scheme that balances patient needs with logistical simplicity.

## Context

You are an RTSM architect with 10 years of global Phase 3 experience. Key study parameters:
- Phase: 3
- Sites: 42
- Arms: active 1 : placebo 1
- Stratification: region (3 levels) and prior therapy (yes/no)
- Blinding: double‑dummy
- Desired balance: 1:1 per stratum
- Regulatory regions: FDA, EMA, PMDA

## Instructions

1. Propose the optimal randomization method (permuted blocks, dynamic/minimization, etc.).
2. Justify block sizes or algorithm parameters to minimize predictability while maintaining simplicity.
3. Draft a concise randomization specification (≤600 words) covering:
   - Algorithm description and parameters.
   - Seed management and audit‑trail requirements.
   - Dummy‑code structure and masking plan.
   - Simulation results showing expected imbalance <2 patients per arm within each stratum at N = 600.

## Inputs

- `{{study_parameters}}` — any additional trial details.

## Output Format

- 4‑bullet executive summary.
- Specification in a markdown table (sections as rows, <80 chars per cell).
- No internal reasoning—only the final deliverable.

## Additional Notes

Ensure the scheme is ready for RTSM vendor implementation.
