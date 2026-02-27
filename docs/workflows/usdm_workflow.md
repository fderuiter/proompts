---
title: Protocol to USDM Workflow
---

# Protocol to USDM Workflow

A 5-stage chain to convert unstructured Clinical Protocol text into CDISC USDM v3.0 JSON.

## Workflow Diagram

```mermaid
graph TD
    Input_protocol_text[Input: protocol_text] --> Steps
    Input_protocol_objectives_text[Input: protocol_objectives_text] --> Steps
    Input_protocol_soa_text[Input: protocol_soa_text] --> Steps
    stage1_metadata[Step: stage1_metadata]
    Input_protocol_text --> stage1_metadata
    stage2_rationale[Step: stage2_rationale]
    Input_protocol_objectives_text --> stage2_rationale
    stage3_workflow[Step: stage3_workflow]
    Input_protocol_soa_text --> stage3_workflow
    stage4_concepts[Step: stage4_concepts]
    stage3_workflow --> stage4_concepts
    stage5_assembly[Step: stage5_assembly]
    stage1_metadata --> stage5_assembly
    stage2_rationale --> stage5_assembly
    stage3_workflow --> stage5_assembly
    stage4_concepts --> stage5_assembly
```

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/workflows/clinical/usdm_workflow.workflow.yaml)
