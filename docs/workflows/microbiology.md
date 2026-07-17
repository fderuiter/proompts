---
title: Microbiology Workflow
---

# Microbiology Workflow

A workflow for creating a bioburden testing SOP, an EO sterilization validation protocol, and an endotoxin control risk plan.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_device_description([Input: device_description]):::inputNode
    INPUT_device_name([Input: device_name]):::inputNode
    bioburden_sop[bioburden_sop<br><i>01_bioburden_testing_sop.prompt.md</i>]:::stepNode
    INPUT_device_description -. device_description .-> bioburden_sop
    bioburden_sop -->|sequential| sterilization_protocol
    sterilization_protocol[sterilization_protocol<br><i>02_eo_sterilization_validation_protocol.prompt.md</i>]:::stepNode
    INPUT_device_name -. device_name .-> sterilization_protocol
    sterilization_protocol -->|sequential| endotoxin_risk_plan
    endotoxin_risk_plan[endotoxin_risk_plan<br><i>03_endotoxin_control_510k_risk_plan.prompt.md</i>]:::stepNode
    INPUT_device_name -. device_name .-> endotoxin_risk_plan
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/workflows/scientific/microbiology.workflow.yaml)
