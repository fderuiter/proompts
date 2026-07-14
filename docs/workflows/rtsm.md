---
title: RTSM Workflow
---

# RTSM Workflow

A workflow for designing a randomization scheme, a supply strategy, and a risk-based monitoring SOP.

## Workflow Diagram

```mermaid
graph TD
    INPUT_study_parameters([Input: study_parameters])
    INPUT_trial_enrollment([Input: trial_enrollment])
    INPUT_existing_sop([Input: existing_sop])
    randomization_scheme[randomization_scheme<br><i>01_patient_centered_randomization_scheme.prompt.md</i>]
    INPUT_study_parameters -. study_parameters .-> randomization_scheme
    randomization_scheme -->|sequential| supply_strategy
    supply_strategy[supply_strategy<br><i>02_site_level_supply_resupply_strategy.prompt.md</i>]
    INPUT_trial_enrollment -. trial_enrollment .-> supply_strategy
    supply_strategy -->|sequential| rbm_sop
    rbm_sop[rbm_sop<br><i>03_risk_based_monitoring_sop.prompt.md</i>]
    INPUT_existing_sop -. existing_sop .-> rbm_sop
```


