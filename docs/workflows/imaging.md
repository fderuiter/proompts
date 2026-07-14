---
title: Imaging Workflow
---

# Imaging Workflow

A workflow for various imaging-related tasks, including charter drafting, QC, central reading design, and regulatory packaging.

## Workflow Diagram

```mermaid
graph TD
    INPUT_charter_draft_protocol_synopsis([Input: charter_draft_protocol_synopsis])
    INPUT_charter_draft_modalities([Input: charter_draft_modalities])
    INPUT_charter_draft_endpoints([Input: charter_draft_endpoints])
    INPUT_charter_draft_sites([Input: charter_draft_sites])
    INPUT_charter_draft_regulations([Input: charter_draft_regulations])
    INPUT_upload_log_csv([Input: upload_log_csv])
    INPUT_central_reading_disease([Input: central_reading_disease])
    INPUT_central_reading_timepoints([Input: central_reading_timepoints])
    INPUT_central_reading_endpoints([Input: central_reading_endpoints])
    INPUT_central_reading_reader_pool_size([Input: central_reading_reader_pool_size])
    INPUT_central_reading_budget([Input: central_reading_budget])
    INPUT_reg_charter_study_overview([Input: reg_charter_study_overview])
    INPUT_reg_charter_modalities([Input: reg_charter_modalities])
    INPUT_reg_charter_regions([Input: reg_charter_regions])
    INPUT_reg_charter_endpoint_description([Input: reg_charter_endpoint_description])
    INPUT_qc_workflow_study_description([Input: qc_workflow_study_description])
    INPUT_qc_workflow_modalities([Input: qc_workflow_modalities])
    INPUT_data_package_study_summary([Input: data_package_study_summary])
    INPUT_data_package_metrics_data([Input: data_package_metrics_data])
    INPUT_data_package_reader_agreement([Input: data_package_reader_agreement])
    imaging_charter_draft[imaging_charter_draft<br><i>01_imaging_charter_draft.prompt.md</i>]
    INPUT_charter_draft_protocol_synopsis -. protocol_synopsis .-> imaging_charter_draft
    INPUT_charter_draft_modalities -. modalities .-> imaging_charter_draft
    INPUT_charter_draft_endpoints -. endpoints .-> imaging_charter_draft
    INPUT_charter_draft_sites -. sites .-> imaging_charter_draft
    INPUT_charter_draft_regulations -. regulations .-> imaging_charter_draft
    imaging_charter_draft -->|sequential| site_upload_qc
    site_upload_qc[site_upload_qc<br><i>02_site_upload_qc.prompt.md</i>]
    INPUT_upload_log_csv -. upload_log_csv .-> site_upload_qc
    site_upload_qc -->|sequential| central_reading_design
    central_reading_design[central_reading_design<br><i>03_central_reading_design.prompt.md</i>]
    INPUT_central_reading_disease -. disease .-> central_reading_design
    INPUT_central_reading_timepoints -. timepoints .-> central_reading_design
    INPUT_central_reading_endpoints -. endpoints .-> central_reading_design
    INPUT_central_reading_reader_pool_size -. reader_pool_size .-> central_reading_design
    INPUT_central_reading_budget -. budget .-> central_reading_design
    central_reading_design -->|sequential| regulatory_imaging_charter
    regulatory_imaging_charter[regulatory_imaging_charter<br><i>04_regulatory_imaging_charter_generator.prompt.md</i>]
    INPUT_reg_charter_study_overview -. study_overview .-> regulatory_imaging_charter
    INPUT_reg_charter_modalities -. modalities .-> regulatory_imaging_charter
    INPUT_reg_charter_regions -. regions .-> regulatory_imaging_charter
    INPUT_reg_charter_endpoint_description -. endpoint_description .-> regulatory_imaging_charter
    regulatory_imaging_charter -->|sequential| image_acquisition_qc_workflow
    image_acquisition_qc_workflow[image_acquisition_qc_workflow<br><i>05_image_acquisition_qc_workflow_blueprint.prompt.md</i>]
    INPUT_qc_workflow_study_description -. study_description .-> image_acquisition_qc_workflow
    INPUT_qc_workflow_modalities -. modalities .-> image_acquisition_qc_workflow
    image_acquisition_qc_workflow -->|sequential| regulatory_imaging_data_package
    regulatory_imaging_data_package[regulatory_imaging_data_package<br><i>06_regulatory_imaging_data_package.prompt.md</i>]
    INPUT_data_package_study_summary -. study_summary .-> regulatory_imaging_data_package
    INPUT_data_package_metrics_data -. metrics_data .-> regulatory_imaging_data_package
    INPUT_data_package_reader_agreement -. reader_agreement .-> regulatory_imaging_data_package
```


