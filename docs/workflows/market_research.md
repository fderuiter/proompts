---
title: Market Research Workflow
---

# Market Research Workflow

A workflow for market landscape analysis, user needs assessment, barrier mapping, and executive summary generation.

## Workflow Diagram

```mermaid
graph TD
    INPUT_device_or_assay([Input: device_or_assay])
    INPUT_application([Input: application])
    INPUT_device([Input: device])
    INPUT_markets([Input: markets])
    INPUT_market_report([Input: market_report])
    landscape_analysis[landscape_analysis<br><i>01_market_landscape_trend_analysis.prompt.md</i>]
    INPUT_device_or_assay -. device_or_assay .-> landscape_analysis
    landscape_analysis -->|sequential| needs_assessment
    needs_assessment[needs_assessment<br><i>02_target_segment_user_needs_assessment.prompt.md</i>]
    INPUT_device_or_assay -. device_or_assay .-> needs_assessment
    INPUT_application -. application .-> needs_assessment
    needs_assessment -->|sequential| barrier_mapping
    barrier_mapping[barrier_mapping<br><i>03_regulatory_commercial_barrier_mapping.prompt.md</i>]
    INPUT_device -. device .-> barrier_mapping
    INPUT_markets -. markets .-> barrier_mapping
    barrier_mapping -->|sequential| executive_summary
    executive_summary[executive_summary<br><i>04_market_report_exec_summary.prompt.md</i>]
    INPUT_market_report -. market_report .-> executive_summary
```


