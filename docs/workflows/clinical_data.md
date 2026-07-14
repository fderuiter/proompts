---
title: Clinical Data Workflow
---

# Clinical Data Workflow

A workflow for detecting discrepancies, drafting a DMP section, and building edit check specifications.

## Workflow Diagram

```mermaid
graph TD
    INPUT_edc_export_csv([Input: edc_export_csv])
    INPUT_dmp_section_requirements([Input: dmp_section_requirements])
    INPUT_edit_check_rules([Input: edit_check_rules])
    discrepancy_detection[discrepancy_detection<br><i>01_discrepancy_detection_query_log.prompt.md</i>]
    INPUT_edc_export_csv -. input .-> discrepancy_detection
    discrepancy_detection -->|sequential| dmp_section
    dmp_section[dmp_section<br><i>02_data_management_plan_section.prompt.md</i>]
    INPUT_dmp_section_requirements -. input .-> dmp_section
    dmp_section -->|sequential| edit_check_specification
    edit_check_specification[edit_check_specification<br><i>03_edit_check_specification_builder.prompt.md</i>]
    INPUT_edit_check_rules -. input .-> edit_check_specification
```


