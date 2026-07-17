---
title: CRA Workflow
---

# CRA Workflow

A workflow for generating a monitoring visit report, tracking investigator follow-up emails, and building an RBM plan.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_visit_info([Input: visit_info]):::inputNode
    INPUT_pending_actions([Input: pending_actions]):::inputNode
    INPUT_study_info([Input: study_info]):::inputNode
    report_generator[report_generator<br><i>01_monitoring_visit_report_generator.prompt.md</i>]:::stepNode
    INPUT_visit_info -. input .-> report_generator
    report_generator -->|sequential| email_tracker
    email_tracker[email_tracker<br><i>02_investigator_follow_up_email_tracker.prompt.md</i>]:::stepNode
    INPUT_pending_actions -. input .-> email_tracker
    email_tracker -->|sequential| rbm_plan_builder
    rbm_plan_builder[rbm_plan_builder<br><i>03_rbm_plan_builder.prompt.md</i>]:::stepNode
    INPUT_study_info -. input .-> rbm_plan_builder
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/workflows/clinical/cra.workflow.yaml)
