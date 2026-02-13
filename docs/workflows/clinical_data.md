---
layout: default
title: Clinical Data Workflow
parent: Workflows
nav_order: 99
---

# Clinical Data Workflow

A workflow for detecting discrepancies, drafting a DMP section, and building edit check specifications.

## Workflow Diagram\n\n<div class="mermaid">\ngraph TD
    Input_edc_export_csv[Input: edc_export_csv] --> Steps
    Input_dmp_section_requirements[Input: dmp_section_requirements] --> Steps
    Input_edit_check_rules[Input: edit_check_rules] --> Steps
    discrepancy_detection[Step: discrepancy_detection]
    Input_edc_export_csv --> discrepancy_detection
    dmp_section[Step: dmp_section]
    Input_dmp_section_requirements --> dmp_section
    edit_check_specification[Step: edit_check_specification]
    Input_edit_check_rules --> edit_check_specification\n</div>\n
[View Source YAML](../../workflows/clinical/clinical_data.workflow.yaml)
