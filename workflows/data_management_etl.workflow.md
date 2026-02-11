# Clinical ETL Pipeline Design and Review

A workflow to create an ETL mapping spec, define QC transformations, and review the final pipeline. This follows the sequence in the data_management_prompts directory (04, 05, 06).

## Visual Flow

```mermaid
flowchart TD
    subgraph Inputs [Global Inputs]
        inp_etl_requirements((etl_requirements))
    end
    create_mapping_spec["create_mapping_spec<br/><small>data_management_prompts/04_clinical_etl_mapping_spec.prompt.yaml</small>"]
    define_qc_checks["define_qc_checks<br/><small>data_management_prompts/05_clinical_etl_transformation_qc.prompt.yaml</small>"]
    review_pipeline["review_pipeline<br/><small>data_management_prompts/06_clinical_etl_pipeline_review.prompt.yaml</small>"]
    inp_etl_requirements -->|etl_requirements| create_mapping_spec
    create_mapping_spec -->|etl_mapping_spec| define_qc_checks
    define_qc_checks -->|etl_qc_plan| review_pipeline
```
