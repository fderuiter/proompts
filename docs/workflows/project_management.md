---
layout: default
title: Project Management Workflow
parent: Workflows
nav_order: 99
---

# Project Management Workflow

A workflow to create a project charter, risk register, status report, and timeline.

## Workflow Diagram

<div class="mermaid">
graph TD
    Input_project_name[Input: project_name] --> Steps
    Input_project_description[Input: project_description] --> Steps
    Input_budget[Input: budget] --> Steps
    Input_deadline[Input: deadline] --> Steps
    Input_stakeholders[Input: stakeholders] --> Steps
    Input_business_outcome[Input: business_outcome] --> Steps
    Input_update_notes[Input: update_notes] --> Steps
    Input_project_type[Input: project_type] --> Steps
    Input_objectives[Input: objectives] --> Steps
    Input_milestone_data[Input: milestone_data] --> Steps
    project_charter[Step: project_charter]
    Input_project_name --> project_charter
    Input_project_description --> project_charter
    Input_budget --> project_charter
    Input_deadline --> project_charter
    Input_stakeholders --> project_charter
    Input_business_outcome --> project_charter
    risk_register[Step: risk_register]
    project_charter --> risk_register
    status_report[Step: status_report]
    Input_update_notes --> status_report
    timeline[Step: timeline]
    Input_project_type --> timeline
    Input_objectives --> timeline
    Input_milestone_data --> timeline
</div>

[View Source YAML](../../workflows/project_management.workflow.yaml)
