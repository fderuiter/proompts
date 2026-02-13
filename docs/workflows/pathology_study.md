---
layout: default
title: Preclinical Pathology Study Workflow
parent: Workflows
nav_order: 99
---

# Preclinical Pathology Study Workflow

A workflow to design a pathology study protocol, evaluate the device-tissue interface, and plan the slide reporting. This follows the sequence in the pathology_prompts directory.

## Workflow Diagram

<div class="mermaid">
graph TD
    Input_study_details[Input: study_details] --> Steps
    design_protocol[Step: design_protocol]
    Input_study_details --> design_protocol
    evaluate_interface[Step: evaluate_interface]
    design_protocol --> evaluate_interface
    plan_reporting[Step: plan_reporting]
    evaluate_interface --> plan_reporting
</div>

[View Source YAML](../../workflows/pathology_study.workflow.yaml)
