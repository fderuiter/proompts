---
layout: default
title: Microbiology Workflow
parent: Workflows
nav_order: 99
---

# Microbiology Workflow

A workflow for creating a bioburden testing SOP, an EO sterilization validation protocol, and an endotoxin control risk plan.

## Workflow Diagram\n\n<div class="mermaid">\ngraph TD
    Input_device_description[Input: device_description] --> Steps
    Input_device_name[Input: device_name] --> Steps
    bioburden_sop[Step: bioburden_sop]
    Input_device_description --> bioburden_sop
    sterilization_protocol[Step: sterilization_protocol]
    Input_device_name --> sterilization_protocol
    endotoxin_risk_plan[Step: endotoxin_risk_plan]
    Input_device_name --> endotoxin_risk_plan\n</div>\n
[View Source YAML](../../workflows/scientific/microbiology.workflow.yaml)
