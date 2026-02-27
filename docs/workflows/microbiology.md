---
title: Microbiology Workflow
---

# Microbiology Workflow

A workflow for creating a bioburden testing SOP, an EO sterilization validation protocol, and an endotoxin control risk plan.

## Workflow Diagram

```mermaid
graph TD
    Input_device_description[Input: device_description] --> Steps
    Input_device_name[Input: device_name] --> Steps
    bioburden_sop[Step: bioburden_sop]
    Input_device_description --> bioburden_sop
    sterilization_protocol[Step: sterilization_protocol]
    Input_device_name --> sterilization_protocol
    endotoxin_risk_plan[Step: endotoxin_risk_plan]
    Input_device_name --> endotoxin_risk_plan
```

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/workflows/scientific/microbiology.workflow.yaml)
