---
title: Clinical Monitoring Workflow
---

# Clinical Monitoring Workflow

A workflow for creating a site performance dashboard, building a CAPA plan, and critiquing a monitoring visit report.

## Workflow Diagram

```mermaid
graph TD
    Input_site_performance_data[Input: site_performance_data] --> Steps
    Input_monitoring_findings[Input: monitoring_findings] --> Steps
    Input_mvr_report[Input: mvr_report] --> Steps
    performance_dashboard[Step: performance_dashboard]
    Input_site_performance_data --> performance_dashboard
    capa_plan[Step: capa_plan]
    Input_monitoring_findings --> capa_plan
    mvr_critique[Step: mvr_critique]
    Input_mvr_report --> mvr_critique
```

[View Source YAML](../../workflows/clinical/clinical_monitoring.workflow.yaml)
