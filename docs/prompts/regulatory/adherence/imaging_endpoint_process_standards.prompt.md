---
title: Imaging Endpoint Process Standards Checklist
---

# Imaging Endpoint Process Standards Checklist

Review FDA guidance on imaging endpoints and create process checklists.

[View Source YAML](../../../../prompts/regulatory/adherence/imaging_endpoint_process_standards.prompt.yaml)

```yaml
---
name: Imaging Endpoint Process Standards Checklist
version: 0.1.0
description: Review FDA guidance on imaging endpoints and create process checklists.
metadata:
  domain: regulatory
  complexity: medium
  tags:
  - regulatory-adherence
  - imaging
  - endpoint
  - process
  - standards
  requires_context: false
variables:
- name: endpoint
  description: The endpoint to use for this prompt
  required: true
- name: modality
  description: The modality to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.1
messages:
- role: system
  content: 'You are a Clinical Imaging Scientist and Regulatory Specialist. Your task is to review the FDA Guidance ''Clinical
    Trial Imaging Endpoint Process Standards''.


    Your output should be a checklist of trial-specific imaging process standards to be included in an imaging charter or
    site operations manual, using Markdown headers:


    1.  **## Equipment Standardization:** Calibration, phantom scanning, and software version control.

    2.  **## Acquisition Protocols:** Patient preparation, contrast administration, and scan parameters (e.g., slice thickness).

    3.  **## Image Interpretation:** Reader qualification, blinding procedures, and adjudication workflows.

    4.  **## Data Management:** Transfer protocols, de-identification, and archival.


    Ensure the checklist is practical for site staff and core labs.

    '
- role: user
  content: '<imaging_modality>

    {{modality}} (e.g., MRI, CT, PET)

    </imaging_modality>


    <primary_endpoint>

    {{endpoint}} (e.g., Tumor Response via RECIST 1.1)

    </primary_endpoint>


    Generate the process standards checklist.

    '
testData:
- input: 'modality: Brain MRI

    endpoint: Progression-Free Survival (PFS) in Glioblastoma

    '
  expected: Checklist for MRI scanner standardization (field strength), contrast timing, and blinded central review process.
evaluators:
- name: Standardization Check
  regex:
    pattern: (?i)(calibration|phantom|protocol)
- name: Reader Check
  regex:
    pattern: (?i)(reader|blind|adjudication)

```
