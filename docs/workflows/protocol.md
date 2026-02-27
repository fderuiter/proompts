---
title: Protocol Workflow
---

# Protocol Workflow

A workflow to create, review, and refine a clinical trial protocol.

## Workflow Diagram

```mermaid
graph TD
    Input_summary_sheet[Input: summary_sheet] --> Steps
    Input_process_information[Input: process_information] --> Steps
    Input_condition[Input: condition] --> Steps
    Input_draft_section[Input: draft_section] --> Steps
    protocol_creator[Step: protocol_creator]
    Input_summary_sheet --> protocol_creator
    sop_architect[Step: sop_architect]
    Input_process_information --> sop_architect
    protocol_reviewer[Step: protocol_reviewer]
    protocol_creator --> protocol_reviewer
    protocol_refinement[Step: protocol_refinement]
    Input_condition --> protocol_refinement
    Input_draft_section --> protocol_refinement
```

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/workflows/clinical/protocol.workflow.yaml)
