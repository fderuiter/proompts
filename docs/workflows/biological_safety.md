---
title: Biological Safety Assessment and Planning
---

# Biological Safety Assessment and Planning

A workflow to perform a risk assessment for a medical device, develop a biological safety plan, and prepare for regulatory submission. This follows the sequence in the biological_safety_prompts directory.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_medical_device_type([Input: medical_device_type]):::inputNode
    perform_risk_assessment[perform_risk_assessment<br><i>01_risk_assessment_expert.prompt.md</i>]:::stepNode
    INPUT_medical_device_type -. medical_device_type .-> perform_risk_assessment
    perform_risk_assessment -->|sequential| develop_safety_plan
    develop_safety_plan[develop_safety_plan<br><i>02_biological_safety_plan_developer.prompt.md</i>]:::stepNode
    perform_risk_assessment -. risk_assessment .-> develop_safety_plan
    INPUT_medical_device_type -. device_description .-> develop_safety_plan
    develop_safety_plan -->|sequential| prepare_submission
    prepare_submission[prepare_submission<br><i>03_regulatory_submission_support.prompt.md</i>]:::stepNode
    develop_safety_plan -. biological_safety_plan .-> prepare_submission
    INPUT_medical_device_type -. device_description .-> prepare_submission
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```


