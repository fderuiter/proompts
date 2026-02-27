---
title: Adjudication Workflow
---

# Adjudication Workflow

A workflow to design an adjudication dashboard, create a source document checklist, and analyze adjudication KPIs.

## Workflow Diagram

```mermaid
graph TD
    Input_charter_excerpt[Input: charter_excerpt] --> Steps
    Input_adjudication_log_csv[Input: adjudication_log_csv] --> Steps
    design_dashboard[Step: design_dashboard]
    create_checklist[Step: create_checklist]
    Input_charter_excerpt --> create_checklist
    analyze_kpis[Step: analyze_kpis]
    Input_adjudication_log_csv --> analyze_kpis
```

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/workflows/clinical/adjudication.workflow.yaml)
