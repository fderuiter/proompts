---
title: Preclinical Pathology Study Workflow
---

# Preclinical Pathology Study Workflow

A workflow to design a pathology study protocol, evaluate the device-tissue interface, and plan the slide reporting. This follows the sequence in the pathology_prompts directory.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_study_details([Input: study_details]):::inputNode
    design_protocol[design_protocol<br><i>01_study_protocol_outline.prompt.md</i>]:::stepNode
    INPUT_study_details -. study_details .-> design_protocol
    design_protocol -->|sequential| evaluate_interface
    evaluate_interface[evaluate_interface<br><i>02_device_tissue_interface_evaluation.prompt.md</i>]:::stepNode
    design_protocol -. study_protocol .-> evaluate_interface
    evaluate_interface -->|sequential| plan_reporting
    plan_reporting[plan_reporting<br><i>03_slides_and_reporting_workflow.prompt.md</i>]:::stepNode
    evaluate_interface -. interface_evaluation .-> plan_reporting
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```


