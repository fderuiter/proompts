---
title: Project Management Workflow
---

# Project Management Workflow

A workflow to create a project charter, risk register, status report, and timeline.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_project_name([Input: project_name]):::inputNode
    INPUT_project_description([Input: project_description]):::inputNode
    INPUT_budget([Input: budget]):::inputNode
    INPUT_deadline([Input: deadline]):::inputNode
    INPUT_stakeholders([Input: stakeholders]):::inputNode
    INPUT_business_outcome([Input: business_outcome]):::inputNode
    INPUT_update_notes([Input: update_notes]):::inputNode
    INPUT_project_type([Input: project_type]):::inputNode
    INPUT_objectives([Input: objectives]):::inputNode
    INPUT_milestone_data([Input: milestone_data]):::inputNode
    project_charter[project_charter<br><i>01_project_charter_scope.prompt.md</i>]:::stepNode
    INPUT_project_name -. project_name .-> project_charter
    INPUT_project_description -. project_description .-> project_charter
    INPUT_budget -. budget .-> project_charter
    INPUT_deadline -. deadline .-> project_charter
    INPUT_stakeholders -. stakeholders .-> project_charter
    INPUT_business_outcome -. business_outcome .-> project_charter
    project_charter -->|sequential| risk_register
    risk_register[risk_register<br><i>02_risk_register_mitigation.prompt.md</i>]:::stepNode
    project_charter -. project_overview .-> risk_register
    risk_register -->|sequential| status_report
    status_report[status_report<br><i>03_weekly_exec_status_report.prompt.md</i>]:::stepNode
    INPUT_update_notes -. update_notes .-> status_report
    status_report -->|sequential| timeline
    timeline[timeline<br><i>04_detailed_project_blueprint_timeline.prompt.md</i>]:::stepNode
    INPUT_project_type -. project_type .-> timeline
    INPUT_objectives -. objectives .-> timeline
    INPUT_milestone_data -. milestone_data .-> timeline
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/workflows/management/project_management.workflow.yaml)
