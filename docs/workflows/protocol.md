---
title: Protocol Workflow
---

# Protocol Workflow

A workflow to create, review, and refine a clinical trial protocol.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_summary_sheet([Input: summary_sheet]):::inputNode
    INPUT_process_information([Input: process_information]):::inputNode
    INPUT_condition([Input: condition]):::inputNode
    INPUT_draft_section([Input: draft_section]):::inputNode
    protocol_creator[protocol_creator<br><i>01_clinical_trial_protocol_creator.prompt.md</i>]:::stepNode
    INPUT_summary_sheet -. summary_sheet .-> protocol_creator
    protocol_creator -->|sequential| sop_architect
    sop_architect[sop_architect<br><i>02_ultimate_sop_architect.prompt.md</i>]:::stepNode
    INPUT_process_information -. process_information .-> sop_architect
    sop_architect -->|sequential| protocol_reviewer
    protocol_reviewer[protocol_reviewer<br><i>03_protocol_reviewer_gap_analysis_coach.prompt.md</i>]:::stepNode
    protocol_creator -. protocol_text_or_nct .-> protocol_reviewer
    protocol_reviewer -->|sequential| protocol_refinement
    protocol_refinement[protocol_refinement<br><i>04_protocol_section_refinement.prompt.md</i>]:::stepNode
    INPUT_condition -. condition .-> protocol_refinement
    INPUT_draft_section -. draft_section .-> protocol_refinement
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```


