---
layout: default
title: CRA Workflow
parent: Workflows
nav_order: 99
---

# CRA Workflow

A workflow for generating a monitoring visit report, tracking investigator follow-up emails, and building an RBM plan.

## Workflow Diagram

```mermaid
graph TD
    Input_visit_info[Input: visit_info] --> Steps
    Input_pending_actions[Input: pending_actions] --> Steps
    Input_study_info[Input: study_info] --> Steps
    report_generator[Step: report_generator]
    Input_visit_info --> report_generator
    email_tracker[Step: email_tracker]
    Input_pending_actions --> email_tracker
    rbm_plan_builder[Step: rbm_plan_builder]
    Input_study_info --> rbm_plan_builder
```

[View Source YAML](../workflows_src/clinical/cra.workflow.yaml)
