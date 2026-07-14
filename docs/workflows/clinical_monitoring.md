---
title: Clinical Monitoring Workflow
---

# Clinical Monitoring Workflow

A workflow for creating a site performance dashboard, building a CAPA plan, and critiquing a monitoring visit report.

## Workflow Diagram

```mermaid
graph TD
    INPUT_site_performance_data([Input: site_performance_data])
    INPUT_monitoring_findings([Input: monitoring_findings])
    INPUT_mvr_report([Input: mvr_report])
    performance_dashboard[performance_dashboard<br><i>01_risk_based_site_performance_dashboard.prompt.md</i>]
    INPUT_site_performance_data -. input .-> performance_dashboard
    performance_dashboard -->|sequential| capa_plan
    capa_plan[capa_plan<br><i>02_capa_plan_builder_for_monitoring_findings.prompt.md</i>]
    INPUT_monitoring_findings -. input .-> capa_plan
    capa_plan -->|sequential| mvr_critique
    mvr_critique[mvr_critique<br><i>03_monitoring_visit_report_quality_critique.prompt.md</i>]
    INPUT_mvr_report -. input .-> mvr_critique
```


