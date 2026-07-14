---
title: Clinical Monitoring Workflow
---

# Clinical Monitoring Workflow

A workflow for creating a site performance dashboard, building a CAPA plan, and critiquing a monitoring visit report.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_site_performance_data([Input: site_performance_data]):::inputNode
    INPUT_monitoring_findings([Input: monitoring_findings]):::inputNode
    INPUT_mvr_report([Input: mvr_report]):::inputNode
    performance_dashboard[performance_dashboard<br><i>01_risk_based_site_performance_dashboard.prompt.md</i>]:::stepNode
    INPUT_site_performance_data -. input .-> performance_dashboard
    performance_dashboard -->|sequential| capa_plan
    capa_plan[capa_plan<br><i>02_capa_plan_builder_for_monitoring_findings.prompt.md</i>]:::stepNode
    INPUT_monitoring_findings -. input .-> capa_plan
    capa_plan -->|sequential| mvr_critique
    mvr_critique[mvr_critique<br><i>03_monitoring_visit_report_quality_critique.prompt.md</i>]:::stepNode
    INPUT_mvr_report -. input .-> mvr_critique
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```


