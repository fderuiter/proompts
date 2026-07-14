---
title: CRA Workflow
---

# CRA Workflow

A workflow for generating a monitoring visit report, tracking investigator follow-up emails, and building an RBM plan.

## Workflow Diagram

```mermaid
graph TD
    INPUT_visit_info([Input: visit_info])
    INPUT_pending_actions([Input: pending_actions])
    INPUT_study_info([Input: study_info])
    report_generator[report_generator<br><i>01_monitoring_visit_report_generator.prompt.md</i>]
    INPUT_visit_info -. input .-> report_generator
    report_generator -->|sequential| email_tracker
    email_tracker[email_tracker<br><i>02_investigator_follow_up_email_tracker.prompt.md</i>]
    INPUT_pending_actions -. input .-> email_tracker
    email_tracker -->|sequential| rbm_plan_builder
    rbm_plan_builder[rbm_plan_builder<br><i>03_rbm_plan_builder.prompt.md</i>]
    INPUT_study_info -. input .-> rbm_plan_builder
```


