---
title: Testing Workflow
---

# Testing Workflow

A workflow for end-to-end test discovery, design verification, human factors validation, and risk-based test case suite generation.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:#0d3a4d,stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:#183b27,stroke-width:2px,color:#ffffff;
    INPUT_project_name([Input: project_name]):::inputNode
    INPUT_languages_frameworks([Input: languages_frameworks]):::inputNode
    INPUT_business_goal([Input: business_goal]):::inputNode
    INPUT_device_name([Input: device_name]):::inputNode
    INPUT_device_class([Input: device_class]):::inputNode
    INPUT_hazard_analysis_table([Input: hazard_analysis_table]):::inputNode
    e2e_test_discovery[e2e_test_discovery<br><i>01_e2e_test_discovery.prompt.md</i>]:::stepNode
    INPUT_project_name -. project_name .-> e2e_test_discovery
    INPUT_languages_frameworks -. languages_frameworks .-> e2e_test_discovery
    INPUT_business_goal -. business_goal .-> e2e_test_discovery
    e2e_test_discovery -->|sequential| design_verification
    design_verification[design_verification<br><i>02_design_verification_test_plan.prompt.md</i>]:::stepNode
    INPUT_device_name -. device_name .-> design_verification
    design_verification -->|sequential| human_factors_validation
    human_factors_validation[human_factors_validation<br><i>03_human_factors_validation_study_protocol.prompt.md</i>]:::stepNode
    INPUT_device_name -. device_name .-> human_factors_validation
    INPUT_device_class -. class .-> human_factors_validation
    human_factors_validation -->|sequential| risk_based_test_suite
    risk_based_test_suite[risk_based_test_suite<br><i>04_risk_based_test_case_suite.prompt.md</i>]:::stepNode
    INPUT_device_name -. device_name .-> risk_based_test_suite
    INPUT_hazard_analysis_table -. hazard_analysis_table .-> risk_based_test_suite
    linkStyle default stroke:#767676,stroke-width:2px;
```


