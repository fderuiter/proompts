---
title: RTSM Workflow
---

# RTSM Workflow

A workflow for designing a randomization scheme, a supply strategy, and a risk-based monitoring SOP.

## Workflow Diagram

```mermaid
graph TD
    Input_study_parameters[Input: study_parameters] --> Steps
    Input_trial_enrollment[Input: trial_enrollment] --> Steps
    Input_existing_sop[Input: existing_sop] --> Steps
    randomization_scheme[Step: randomization_scheme]
    Input_study_parameters --> randomization_scheme
    supply_strategy[Step: supply_strategy]
    Input_trial_enrollment --> supply_strategy
    rbm_sop[Step: rbm_sop]
    Input_existing_sop --> rbm_sop
```

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/workflows/clinical/rtsm.workflow.yaml)
