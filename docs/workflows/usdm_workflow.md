---
title: Protocol to USDM Workflow
---

# Protocol to USDM Workflow

A 5-stage chain to convert unstructured Clinical Protocol text into CDISC USDM v3.0 JSON.

## Workflow Diagram

```mermaid
graph TD
    INPUT_protocol_text([Input: protocol_text])
    INPUT_protocol_objectives_text([Input: protocol_objectives_text])
    INPUT_protocol_soa_text([Input: protocol_soa_text])
    stage1_metadata[stage1_metadata<br><i>01_usdm_stage1_metadata.prompt.md</i>]
    INPUT_protocol_text -. protocol_text .-> stage1_metadata
    stage1_metadata -->|sequential| stage2_rationale
    stage2_rationale[stage2_rationale<br><i>02_usdm_stage2_rationale.prompt.md</i>]
    INPUT_protocol_objectives_text -. protocol_objectives_text .-> stage2_rationale
    stage2_rationale -->|sequential| stage3_workflow
    stage3_workflow[stage3_workflow<br><i>03_usdm_stage3_workflow.prompt.md</i>]
    INPUT_protocol_soa_text -. protocol_soa_text .-> stage3_workflow
    stage3_workflow -->|sequential| stage4_concepts
    stage4_concepts[stage4_concepts<br><i>04_usdm_stage4_concepts.prompt.md</i>]
    stage3_workflow -. activities_json .-> stage4_concepts
    stage4_concepts -->|sequential| stage5_assembly
    stage5_assembly[stage5_assembly<br><i>05_usdm_stage5_assembly.prompt.md</i>]
    stage1_metadata -. metadata_json .-> stage5_assembly
    stage2_rationale -. rationale_json .-> stage5_assembly
    stage3_workflow -. workflow_json .-> stage5_assembly
    stage4_concepts -. concepts_json .-> stage5_assembly
```


