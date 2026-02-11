---
layout: default
title: Imaging Workflow
parent: Workflows
nav_order: 99
---

# Imaging Workflow

A workflow for various imaging-related tasks, including charter drafting, QC, central reading design, and regulatory packaging.

## Workflow Diagram

<div class="mermaid">
graph TD
    Input_charter_draft_protocol_synopsis[Input: charter_draft_protocol_synopsis] --> Steps
    Input_charter_draft_modalities[Input: charter_draft_modalities] --> Steps
    Input_charter_draft_endpoints[Input: charter_draft_endpoints] --> Steps
    Input_charter_draft_sites[Input: charter_draft_sites] --> Steps
    Input_charter_draft_regulations[Input: charter_draft_regulations] --> Steps
    Input_upload_log_csv[Input: upload_log_csv] --> Steps
    Input_central_reading_disease[Input: central_reading_disease] --> Steps
    Input_central_reading_timepoints[Input: central_reading_timepoints] --> Steps
    Input_central_reading_endpoints[Input: central_reading_endpoints] --> Steps
    Input_central_reading_reader_pool_size[Input: central_reading_reader_pool_size] --> Steps
    Input_central_reading_budget[Input: central_reading_budget] --> Steps
    Input_reg_charter_study_overview[Input: reg_charter_study_overview] --> Steps
    Input_reg_charter_modalities[Input: reg_charter_modalities] --> Steps
    Input_reg_charter_regions[Input: reg_charter_regions] --> Steps
    Input_reg_charter_endpoint_description[Input: reg_charter_endpoint_description] --> Steps
    Input_qc_workflow_study_description[Input: qc_workflow_study_description] --> Steps
    Input_qc_workflow_modalities[Input: qc_workflow_modalities] --> Steps
    Input_data_package_study_summary[Input: data_package_study_summary] --> Steps
    Input_data_package_metrics_data[Input: data_package_metrics_data] --> Steps
    Input_data_package_reader_agreement[Input: data_package_reader_agreement] --> Steps
    imaging_charter_draft[Step: imaging_charter_draft]
    Input_charter_draft_protocol_synopsis --> imaging_charter_draft
    Input_charter_draft_modalities --> imaging_charter_draft
    Input_charter_draft_endpoints --> imaging_charter_draft
    Input_charter_draft_sites --> imaging_charter_draft
    Input_charter_draft_regulations --> imaging_charter_draft
    site_upload_qc[Step: site_upload_qc]
    Input_upload_log_csv --> site_upload_qc
    central_reading_design[Step: central_reading_design]
    Input_central_reading_disease --> central_reading_design
    Input_central_reading_timepoints --> central_reading_design
    Input_central_reading_endpoints --> central_reading_design
    Input_central_reading_reader_pool_size --> central_reading_design
    Input_central_reading_budget --> central_reading_design
    regulatory_imaging_charter[Step: regulatory_imaging_charter]
    Input_reg_charter_study_overview --> regulatory_imaging_charter
    Input_reg_charter_modalities --> regulatory_imaging_charter
    Input_reg_charter_regions --> regulatory_imaging_charter
    Input_reg_charter_endpoint_description --> regulatory_imaging_charter
    image_acquisition_qc_workflow[Step: image_acquisition_qc_workflow]
    Input_qc_workflow_study_description --> image_acquisition_qc_workflow
    Input_qc_workflow_modalities --> image_acquisition_qc_workflow
    regulatory_imaging_data_package[Step: regulatory_imaging_data_package]
    Input_data_package_study_summary --> regulatory_imaging_data_package
    Input_data_package_metrics_data --> regulatory_imaging_data_package
    Input_data_package_reader_agreement --> regulatory_imaging_data_package
</div>

[View Source YAML](../../workflows/imaging.workflow.yaml)
