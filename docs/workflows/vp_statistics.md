---
title: VP Statistics Workflow
---

# VP Statistics Workflow

A workflow for creating an interim results executive brief, a statistical analysis plan, and a data quality risk heat map.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:#0d3a4d,stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:#183b27,stroke-width:2px,color:#ffffff;
    INPUT_analysis_results([Input: analysis_results]):::inputNode
    INPUT_statistical_plan([Input: statistical_plan]):::inputNode
    INPUT_safety_listings([Input: safety_listings]):::inputNode
    INPUT_protocol_synopsis([Input: protocol_synopsis]):::inputNode
    INPUT_raw_eds_dump([Input: raw_eds_dump]):::inputNode
    INPUT_query_log([Input: query_log]):::inputNode
    executive_brief[executive_brief<br><i>01_interim_results_executive_brief.prompt.md</i>]:::stepNode
    INPUT_analysis_results -. analysis_results .-> executive_brief
    INPUT_statistical_plan -. statistical_plan .-> executive_brief
    INPUT_safety_listings -. safety_listings .-> executive_brief
    executive_brief -->|sequential| sap_draft
    sap_draft[sap_draft<br><i>02_sap_first_draft_builder.prompt.md</i>]:::stepNode
    INPUT_protocol_synopsis -. protocol_synopsis .-> sap_draft
    sap_draft -->|sequential| data_quality_heatmap
    data_quality_heatmap[data_quality_heatmap<br><i>03_data_quality_risk_heatmap.prompt.md</i>]:::stepNode
    INPUT_raw_eds_dump -. raw_eds_dump .-> data_quality_heatmap
    INPUT_query_log -. query_log .-> data_quality_heatmap
    linkStyle default stroke:#767676,stroke-width:2px;
```


