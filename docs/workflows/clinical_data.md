---
title: Clinical Data Workflow
---

# Clinical Data Workflow

A workflow for detecting discrepancies, drafting a DMP section, and building edit check specifications.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_edc_export_csv([Input: edc_export_csv]):::inputNode
    INPUT_dmp_section_requirements([Input: dmp_section_requirements]):::inputNode
    INPUT_edit_check_rules([Input: edit_check_rules]):::inputNode
    discrepancy_detection[discrepancy_detection<br><i>01_discrepancy_detection_query_log.prompt.md</i>]:::stepNode
    INPUT_edc_export_csv -. input .-> discrepancy_detection
    discrepancy_detection -->|sequential| dmp_section
    dmp_section[dmp_section<br><i>02_data_management_plan_section.prompt.md</i>]:::stepNode
    INPUT_dmp_section_requirements -. input .-> dmp_section
    dmp_section -->|sequential| edit_check_specification
    edit_check_specification[edit_check_specification<br><i>03_edit_check_specification_builder.prompt.md</i>]:::stepNode
    INPUT_edit_check_rules -. input .-> edit_check_specification
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```


