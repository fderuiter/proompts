---
title: ePRO Workflow
---

# ePRO Workflow

A workflow for designing a patient-centric BYOD workflow, optimizing ePRO form design, and creating an ePRO adoption plan.

## Workflow Diagram

```mermaid
graph TD
    INPUT_byod_requirements([Input: byod_requirements])
    INPUT_form_details([Input: form_details])
    INPUT_rollout_details([Input: rollout_details])
    byod_workflow[byod_workflow<br><i>01_patient-centric_byod_workflow.prompt.md</i>]
    INPUT_byod_requirements -. input .-> byod_workflow
    byod_workflow -->|sequential| form_design
    form_design[form_design<br><i>02_optimize_epro_form_design.prompt.md</i>]
    INPUT_form_details -. input .-> form_design
    form_design -->|sequential| adoption_plan
    adoption_plan[adoption_plan<br><i>03_epro_adoption_plan_for_sponsors.prompt.md</i>]
    INPUT_rollout_details -. input .-> adoption_plan
```


