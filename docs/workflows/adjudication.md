---
title: Adjudication Workflow
---

# Adjudication Workflow

A workflow to design an adjudication dashboard, create a source document checklist, and analyze adjudication KPIs.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:#0d3a4d,stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:#183b27,stroke-width:2px,color:#ffffff;
    INPUT_charter_excerpt([Input: charter_excerpt]):::inputNode
    INPUT_adjudication_log_csv([Input: adjudication_log_csv]):::inputNode
    design_dashboard[design_dashboard<br><i>01_real_time_adjudication_dashboard.prompt.md</i>]:::stepNode
    design_dashboard -->|sequential| create_checklist
    create_checklist[create_checklist<br><i>02_source_document_endpoint_checklist.prompt.md</i>]:::stepNode
    INPUT_charter_excerpt -. charter_excerpt .-> create_checklist
    create_checklist -->|sequential| analyze_kpis
    analyze_kpis[analyze_kpis<br><i>03_analyze_adjudication_kpis.prompt.md</i>]:::stepNode
    INPUT_adjudication_log_csv -. adjudication_log .-> analyze_kpis
    linkStyle default stroke:#767676,stroke-width:2px;
```


