---
title: Clinical ETL Pipeline Design and Review
---

# Clinical ETL Pipeline Design and Review

A workflow to create an ETL mapping spec, define QC transformations, and review the final pipeline. This follows the sequence in the data_management_prompts directory (04, 05, 06).

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:#0d3a4d,stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:#183b27,stroke-width:2px,color:#ffffff;
    INPUT_etl_requirements([Input: etl_requirements]):::inputNode
    create_mapping_spec[create_mapping_spec<br><i>01_clinical_etl_mapping_spec.prompt.md</i>]:::stepNode
    INPUT_etl_requirements -. etl_requirements .-> create_mapping_spec
    create_mapping_spec -->|sequential| define_qc_checks
    define_qc_checks[define_qc_checks<br><i>02_clinical_etl_transformation_qc.prompt.md</i>]:::stepNode
    create_mapping_spec -. etl_mapping_spec .-> define_qc_checks
    define_qc_checks -->|sequential| review_pipeline
    review_pipeline[review_pipeline<br><i>03_clinical_etl_pipeline_review.prompt.md</i>]:::stepNode
    define_qc_checks -. etl_qc_plan .-> review_pipeline
    linkStyle default stroke:#767676,stroke-width:2px;
```


