---
title: Preclinical Pathology Study Workflow
---

# Preclinical Pathology Study Workflow

A workflow to design a pathology study protocol, evaluate the device-tissue interface, and plan the slide reporting. This follows the sequence in the pathology_prompts directory.

## Workflow Diagram

```mermaid
graph TD
    INPUT_study_details([Input: study_details])
    design_protocol[design_protocol<br><i>01_study_protocol_outline.prompt.md</i>]
    INPUT_study_details -. study_details .-> design_protocol
    design_protocol -->|sequential| evaluate_interface
    evaluate_interface[evaluate_interface<br><i>02_device_tissue_interface_evaluation.prompt.md</i>]
    design_protocol -. study_protocol .-> evaluate_interface
    evaluate_interface -->|sequential| plan_reporting
    plan_reporting[plan_reporting<br><i>03_slides_and_reporting_workflow.prompt.md</i>]
    evaluate_interface -. interface_evaluation .-> plan_reporting
```


