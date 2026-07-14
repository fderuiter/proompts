---
title: Microbiology Workflow
---

# Microbiology Workflow

A workflow for creating a bioburden testing SOP, an EO sterilization validation protocol, and an endotoxin control risk plan.

## Workflow Diagram

```mermaid
graph TD
    INPUT_device_description([Input: device_description])
    INPUT_device_name([Input: device_name])
    bioburden_sop[bioburden_sop<br><i>01_bioburden_testing_sop.prompt.md</i>]
    INPUT_device_description -. device_description .-> bioburden_sop
    bioburden_sop -->|sequential| sterilization_protocol
    sterilization_protocol[sterilization_protocol<br><i>02_eo_sterilization_validation_protocol.prompt.md</i>]
    INPUT_device_name -. device_name .-> sterilization_protocol
    sterilization_protocol -->|sequential| endotoxin_risk_plan
    endotoxin_risk_plan[endotoxin_risk_plan<br><i>03_endotoxin_control_510k_risk_plan.prompt.md</i>]
    INPUT_device_name -. device_name .-> endotoxin_risk_plan
```


