---
layout: default
title: VP Statistics Workflow
parent: Workflows
nav_order: 99
---

# VP Statistics Workflow

A workflow for creating an interim results executive brief, a statistical analysis plan, and a data quality risk heat map.

## Workflow Diagram

```mermaid
graph TD
    Input_analysis_results[Input: analysis_results] --> Steps
    Input_statistical_plan[Input: statistical_plan] --> Steps
    Input_safety_listings[Input: safety_listings] --> Steps
    Input_protocol_synopsis[Input: protocol_synopsis] --> Steps
    Input_raw_eds_dump[Input: raw_eds_dump] --> Steps
    Input_query_log[Input: query_log] --> Steps
    executive_brief[Step: executive_brief]
    Input_analysis_results --> executive_brief
    Input_statistical_plan --> executive_brief
    Input_safety_listings --> executive_brief
    sap_draft[Step: sap_draft]
    Input_protocol_synopsis --> sap_draft
    data_quality_heatmap[Step: data_quality_heatmap]
    Input_raw_eds_dump --> data_quality_heatmap
    Input_query_log --> data_quality_heatmap
```

[View Source YAML](../workflows_src/management/vp_statistics.workflow.yaml)
