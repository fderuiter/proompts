---
title: Sterility Workflow
---

# Sterility Workflow

A workflow for building a sterility validation protocol, comparing regulatory gaps, and performing a process FMEA.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_device_description([Input: device_description]):::inputNode
    INPUT_process_description([Input: process_description]):::inputNode
    validation_protocol[validation_protocol<br><i>01_sterility_validation_protocol_builder.prompt.md</i>]:::stepNode
    INPUT_device_description -. device_description .-> validation_protocol
    validation_protocol -->|sequential| gap_analysis
    gap_analysis[gap_analysis<br><i>02_regulatory_gap_analysis_comparator.prompt.md</i>]:::stepNode
    INPUT_device_description -. device_description .-> gap_analysis
    gap_analysis -->|sequential| process_fmea
    process_fmea[process_fmea<br><i>03_eto_sterilization_process_fmea.prompt.md</i>]:::stepNode
    INPUT_process_description -. process_description .-> process_fmea
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```


