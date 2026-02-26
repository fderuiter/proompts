---
title: Design a Patient-Centered Randomization Scheme
---

# Design a Patient-Centered Randomization Scheme

Create a randomization scheme that balances patient needs with logistical simplicity.

[View Source YAML](../../../../../prompts/clinical/rtsm/rtsm_workflow/01_patient_centered_randomization_scheme.prompt.yaml)

```yaml
---
name: Design a Patient-Centered Randomization Scheme
version: 0.1.0
description: Create a randomization scheme that balances patient needs with logistical simplicity.
metadata:
  domain: clinical
  complexity: medium
  tags:
  - rtsm
  - design
  - patient-centered
  - randomization
  - scheme
  requires_context: false
variables:
- name: study_parameters
  description: any additional trial details
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are an RTSM architect with 10 years of global Phase 3 experience. Key study parameters:


    - Phase: 3

    - Sites: 42

    - Arms: active 1 : placebo 1

    - Stratification: region (3 levels) and prior therapy (yes/no)

    - Blinding: double‑dummy

    - Desired balance: 1:1 per stratum

    - Regulatory regions: FDA, EMA, PMDA


    Create a randomization scheme that balances patient needs with logistical simplicity.'
- role: user
  content: "1. Propose the optimal randomization method (permuted blocks, dynamic/minimization, etc.).\n1. Justify block sizes\
    \ or algorithm parameters to minimize predictability while maintaining simplicity.\n1. Draft a concise randomization specification\
    \ (≤600 words) covering:\n   - Algorithm description and parameters.\n   - Seed management and audit‑trail requirements.\n\
    \   - Dummy‑code structure and masking plan.\n   - Simulation results showing expected imbalance <2 patients per arm within\
    \ each stratum at N = 600.\n\nInputs:\n- `{{study_parameters}}` — any additional trial details.\n\nOutput format:\n- 4‑bullet\
    \ executive summary.\n- Specification in a markdown table (sections as rows, <80 chars per cell).\n- No internal reasoning—only\
    \ the final deliverable.\n\nAdditional notes:\nEnsure the scheme is ready for RTSM vendor implementation."
testData:
- vars:
    study_parameters: example_study_parameters
  expected: 4-bullet executive summary and specification table.
evaluators:
- name: Output starts with bullet list
  string:
    startsWith: '- '

```
