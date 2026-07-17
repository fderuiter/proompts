---
title: Market Research Workflow
---

# Market Research Workflow

A workflow for market landscape analysis, user needs assessment, barrier mapping, and executive summary generation.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_device_or_assay([Input: device_or_assay]):::inputNode
    INPUT_application([Input: application]):::inputNode
    INPUT_device([Input: device]):::inputNode
    INPUT_markets([Input: markets]):::inputNode
    INPUT_market_report([Input: market_report]):::inputNode
    landscape_analysis[landscape_analysis<br><i>01_market_landscape_trend_analysis.prompt.md</i>]:::stepNode
    INPUT_device_or_assay -. device_or_assay .-> landscape_analysis
    landscape_analysis -->|sequential| needs_assessment
    needs_assessment[needs_assessment<br><i>02_target_segment_user_needs_assessment.prompt.md</i>]:::stepNode
    INPUT_device_or_assay -. device_or_assay .-> needs_assessment
    INPUT_application -. application .-> needs_assessment
    needs_assessment -->|sequential| barrier_mapping
    barrier_mapping[barrier_mapping<br><i>03_regulatory_commercial_barrier_mapping.prompt.md</i>]:::stepNode
    INPUT_device -. device .-> barrier_mapping
    INPUT_markets -. markets .-> barrier_mapping
    barrier_mapping -->|sequential| executive_summary
    executive_summary[executive_summary<br><i>04_market_report_exec_summary.prompt.md</i>]:::stepNode
    INPUT_market_report -. market_report .-> executive_summary
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/workflows/business/market_research.workflow.yaml)
