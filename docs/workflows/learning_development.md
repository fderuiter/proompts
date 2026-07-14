---
title: Learning and Development Workflow
---

# Learning and Development Workflow

A workflow for creating a competency-based onboarding blueprint, a scenario-based microlearning series, and a training impact analytics plan.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:#0d3a4d,stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:#183b27,stroke-width:2px,color:#ffffff;
    INPUT_existing_modules([Input: existing_modules]):::inputNode
    INPUT_audience_role([Input: audience_role]):::inputNode
    INPUT_analysis_goal([Input: analysis_goal]):::inputNode
    onboarding_blueprint[onboarding_blueprint<br><i>01_competency_based_onboarding_blueprint.prompt.md</i>]:::stepNode
    INPUT_existing_modules -. existing_modules .-> onboarding_blueprint
    onboarding_blueprint -->|sequential| microlearning_series
    microlearning_series[microlearning_series<br><i>02_scenario_based_microlearning_series.prompt.md</i>]:::stepNode
    INPUT_audience_role -. audience_role .-> microlearning_series
    microlearning_series -->|sequential| analytics_plan
    analytics_plan[analytics_plan<br><i>03_training_impact_analytics_targeted_intervention_planner.prompt.md</i>]:::stepNode
    INPUT_analysis_goal -. analysis_goal .-> analytics_plan
    linkStyle default stroke:#767676,stroke-width:2px;
```


