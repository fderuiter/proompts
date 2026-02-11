---
layout: default
title: Clinical ETL Pipeline Design and Review
parent: Workflows
nav_order: 99
---

# Clinical ETL Pipeline Design and Review

A workflow to create an ETL mapping spec, define QC transformations, and review the final pipeline. This follows the sequence in the data_management_prompts directory (04, 05, 06).

## Workflow Diagram

<div class="mermaid">
graph TD
    Input_etl_requirements[Input: etl_requirements] --> Steps
    create_mapping_spec[Step: create_mapping_spec]
    Input_etl_requirements --> create_mapping_spec
    define_qc_checks[Step: define_qc_checks]
    create_mapping_spec --> define_qc_checks
    review_pipeline[Step: review_pipeline]
    define_qc_checks --> review_pipeline
</div>

[View Source YAML](../../workflows/data_management_etl.workflow.yaml)
