---
layout: default
title: eClinical Integration Workflow
parent: Workflows
nav_order: 99
---

# eClinical Integration Workflow

A workflow for architecting an integration blueprint, creating a data mapping playbook, and compiling a regulatory validation checklist.

## Workflow Diagram

<div class="mermaid">
graph TD
    Input_integration_description[Input: integration_description] --> Steps
    Input_mapping_requirements[Input: mapping_requirements] --> Steps
    Input_validation_info[Input: validation_info] --> Steps
    integration_blueprint[Step: integration_blueprint]
    Input_integration_description --> integration_blueprint
    mapping_playbook[Step: mapping_playbook]
    Input_mapping_requirements --> mapping_playbook
    validation_checklist[Step: validation_checklist]
    Input_validation_info --> validation_checklist
</div>

[View Source YAML](../../workflows/eclinical_integration.workflow.yaml)
