---
title: ePRO Workflow
---

# ePRO Workflow

A workflow for designing a patient-centric BYOD workflow, optimizing ePRO form design, and creating an ePRO adoption plan.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_byod_requirements([Input: byod_requirements]):::inputNode
    INPUT_form_details([Input: form_details]):::inputNode
    INPUT_rollout_details([Input: rollout_details]):::inputNode
    byod_workflow[byod_workflow<br><i>01_patient-centric_byod_workflow.prompt.md</i>]:::stepNode
    INPUT_byod_requirements -. input .-> byod_workflow
    byod_workflow -->|sequential| form_design
    form_design[form_design<br><i>02_optimize_epro_form_design.prompt.md</i>]:::stepNode
    INPUT_form_details -. input .-> form_design
    form_design -->|sequential| adoption_plan
    adoption_plan[adoption_plan<br><i>03_epro_adoption_plan_for_sponsors.prompt.md</i>]:::stepNode
    INPUT_rollout_details -. input .-> adoption_plan
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/workflows/clinical/epro.workflow.yaml)
