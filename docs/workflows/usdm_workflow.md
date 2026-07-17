---
title: Protocol to USDM Workflow
---

# Protocol to USDM Workflow

A 5-stage chain to convert unstructured Clinical Protocol text into CDISC USDM v3.0 JSON.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_protocol_text([Input: protocol_text]):::inputNode
    INPUT_protocol_objectives_text([Input: protocol_objectives_text]):::inputNode
    INPUT_protocol_soa_text([Input: protocol_soa_text]):::inputNode
    stage1_metadata[stage1_metadata<br><i>01_usdm_stage1_metadata.prompt.md</i>]:::stepNode
    INPUT_protocol_text -. protocol_text .-> stage1_metadata
    stage1_metadata -->|sequential| stage2_rationale
    stage2_rationale[stage2_rationale<br><i>02_usdm_stage2_rationale.prompt.md</i>]:::stepNode
    INPUT_protocol_objectives_text -. protocol_objectives_text .-> stage2_rationale
    stage2_rationale -->|sequential| stage3_workflow
    stage3_workflow[stage3_workflow<br><i>03_usdm_stage3_workflow.prompt.md</i>]:::stepNode
    INPUT_protocol_soa_text -. protocol_soa_text .-> stage3_workflow
    stage3_workflow -->|sequential| stage4_concepts
    stage4_concepts[stage4_concepts<br><i>04_usdm_stage4_concepts.prompt.md</i>]:::stepNode
    stage3_workflow -. activities_json .-> stage4_concepts
    stage4_concepts -->|sequential| stage5_assembly
    stage5_assembly[stage5_assembly<br><i>05_usdm_stage5_assembly.prompt.md</i>]:::stepNode
    stage1_metadata -. metadata_json .-> stage5_assembly
    stage2_rationale -. rationale_json .-> stage5_assembly
    stage3_workflow -. workflow_json .-> stage5_assembly
    stage4_concepts -. concepts_json .-> stage5_assembly
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```


