---
title: Clinical ETL Pipeline Design and Review
---

# Clinical ETL Pipeline Design and Review

A workflow to create an ETL mapping spec, define QC transformations, and review the final pipeline. This follows the sequence in the data_management_prompts directory (04, 05, 06).

## Workflow Diagram

```mermaid
graph TD
    INPUT_etl_requirements([Input: etl_requirements])
    create_mapping_spec[create_mapping_spec<br><i>01_clinical_etl_mapping_spec.prompt.md</i>]
    INPUT_etl_requirements -. etl_requirements .-> create_mapping_spec
    create_mapping_spec -->|sequential| define_qc_checks
    define_qc_checks[define_qc_checks<br><i>02_clinical_etl_transformation_qc.prompt.md</i>]
    create_mapping_spec -. etl_mapping_spec .-> define_qc_checks
    define_qc_checks -->|sequential| review_pipeline
    review_pipeline[review_pipeline<br><i>03_clinical_etl_pipeline_review.prompt.md</i>]
    define_qc_checks -. etl_qc_plan .-> review_pipeline
```


