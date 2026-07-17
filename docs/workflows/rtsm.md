---
title: RTSM Workflow
---

# RTSM Workflow

A workflow for designing a randomization scheme, a supply strategy, and a risk-based monitoring SOP.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_study_parameters([Input: study_parameters]):::inputNode
    INPUT_trial_enrollment([Input: trial_enrollment]):::inputNode
    INPUT_existing_sop([Input: existing_sop]):::inputNode
    randomization_scheme[randomization_scheme<br><i>01_patient_centered_randomization_scheme.prompt.md</i>]:::stepNode
    INPUT_study_parameters -. study_parameters .-> randomization_scheme
    randomization_scheme -->|sequential| supply_strategy
    supply_strategy[supply_strategy<br><i>02_site_level_supply_resupply_strategy.prompt.md</i>]:::stepNode
    INPUT_trial_enrollment -. trial_enrollment .-> supply_strategy
    supply_strategy -->|sequential| rbm_sop
    rbm_sop[rbm_sop<br><i>03_risk_based_monitoring_sop.prompt.md</i>]:::stepNode
    INPUT_existing_sop -. existing_sop .-> rbm_sop
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```


