---
title: Sterility Workflow
---

# Sterility Workflow

A workflow for building a sterility validation protocol, comparing regulatory gaps, and performing a process FMEA.

## Workflow Diagram

```mermaid
graph TD
    Input_device_description[Input: device_description] --> Steps
    Input_process_description[Input: process_description] --> Steps
    validation_protocol[Step: validation_protocol]
    Input_device_description --> validation_protocol
    gap_analysis[Step: gap_analysis]
    Input_device_description --> gap_analysis
    process_fmea[Step: process_fmea]
    Input_process_description --> process_fmea
```

[View Source YAML](../../workflows/scientific/sterility.workflow.yaml)
