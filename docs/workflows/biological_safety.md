---
layout: default
title: Biological Safety Assessment and Planning
parent: Workflows
nav_order: 99
---

# Biological Safety Assessment and Planning

A workflow to perform a risk assessment for a medical device, develop a biological safety plan, and prepare for regulatory submission. This follows the sequence in the biological_safety_prompts directory.

## Workflow Diagram\n\n<div class="mermaid">\ngraph TD
    Input_medical_device_type[Input: medical_device_type] --> Steps
    perform_risk_assessment[Step: perform_risk_assessment]
    Input_medical_device_type --> perform_risk_assessment
    develop_safety_plan[Step: develop_safety_plan]
    perform_risk_assessment --> develop_safety_plan
    prepare_submission[Step: prepare_submission]
    develop_safety_plan --> prepare_submission\n</div>\n
[View Source YAML](../../workflows/scientific/biological_safety.workflow.yaml)
