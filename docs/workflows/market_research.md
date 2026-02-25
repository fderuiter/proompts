---
title: Market Research Workflow
---

# Market Research Workflow

A workflow for market landscape analysis, user needs assessment, barrier mapping, and executive summary generation.

## Workflow Diagram

```mermaid
graph TD
    Input_device_or_assay[Input: device_or_assay] --> Steps
    Input_application[Input: application] --> Steps
    Input_device[Input: device] --> Steps
    Input_markets[Input: markets] --> Steps
    Input_market_report[Input: market_report] --> Steps
    landscape_analysis[Step: landscape_analysis]
    Input_device_or_assay --> landscape_analysis
    needs_assessment[Step: needs_assessment]
    Input_device_or_assay --> needs_assessment
    Input_application --> needs_assessment
    barrier_mapping[Step: barrier_mapping]
    Input_device --> barrier_mapping
    Input_markets --> barrier_mapping
    executive_summary[Step: executive_summary]
    Input_market_report --> executive_summary
```

[View Source YAML](../../workflows/business/market_research.workflow.yaml)
