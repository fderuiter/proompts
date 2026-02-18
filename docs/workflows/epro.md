---
layout: default
title: ePRO Workflow
parent: Workflows
nav_order: 99
---

# ePRO Workflow

A workflow for designing a patient-centric BYOD workflow, optimizing ePRO form design, and creating an ePRO adoption plan.

## Workflow Diagram

<div class="mermaid">
graph TD
    Input_byod_requirements[Input: byod_requirements] --> Steps
    Input_form_details[Input: form_details] --> Steps
    Input_rollout_details[Input: rollout_details] --> Steps
    byod_workflow[Step: byod_workflow]
    Input_byod_requirements --> byod_workflow
    form_design[Step: form_design]
    Input_form_details --> form_design
    adoption_plan[Step: adoption_plan]
    Input_rollout_details --> adoption_plan
</div>

[View Source YAML](../../workflows/clinical/epro.workflow.yaml)
