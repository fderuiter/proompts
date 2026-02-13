# Preclinical Pathology Study Workflow

A workflow to design a pathology study protocol, evaluate the device-tissue interface, and plan the slide reporting. This follows the sequence in the pathology_prompts directory.

## Visual Flow

```mermaid
flowchart TD
    subgraph Inputs [Global Inputs]
        inp_study_details((study_details))
    end
    design_protocol["design_protocol<br/><small>prompts/scientific/pathology/pathology_study/01_study_protocol_outline.prompt.yaml</small>"]
    evaluate_interface["evaluate_interface<br/><small>prompts/scientific/pathology/pathology_study/02_device_tissue_interface_evaluation.prompt.yaml</small>"]
    plan_reporting["plan_reporting<br/><small>prompts/scientific/pathology/pathology_study/03_slides_and_reporting_workflow.prompt.yaml</small>"]
    inp_study_details -->|study_details| design_protocol
    design_protocol -->|study_protocol| evaluate_interface
    evaluate_interface -->|interface_evaluation| plan_reporting
```
