---
title: Adjudication Workflow
---

# Adjudication Workflow

A workflow to design an adjudication dashboard, create a source document checklist, and analyze adjudication KPIs.

## Workflow Diagram

```mermaid
graph TD
    INPUT_charter_excerpt([Input: charter_excerpt])
    INPUT_adjudication_log_csv([Input: adjudication_log_csv])
    design_dashboard[design_dashboard<br><i>01_real_time_adjudication_dashboard.prompt.md</i>]
    design_dashboard -->|sequential| create_checklist
    create_checklist[create_checklist<br><i>02_source_document_endpoint_checklist.prompt.md</i>]
    INPUT_charter_excerpt -. charter_excerpt .-> create_checklist
    create_checklist -->|sequential| analyze_kpis
    analyze_kpis[analyze_kpis<br><i>03_analyze_adjudication_kpis.prompt.md</i>]
    INPUT_adjudication_log_csv -. adjudication_log .-> analyze_kpis
```


