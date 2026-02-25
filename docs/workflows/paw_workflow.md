---
title: Principal Architect Workflow (PAW)
---

# Principal Architect Workflow (PAW)

A state-machine workflow for disciplined software engineering tasks, enforcing Design, Refactor, Implementation, and QA phases.

## Workflow Diagram

```mermaid
graph TD
    Input_todo_content[Input: todo_content] --> Steps
    Input_file_structure[Input: file_structure] --> Steps
    Input_relevant_source_code[Input: relevant_source_code] --> Steps
    tactical_recon[Step: tactical_recon]
    Input_todo_content --> tactical_recon
    Input_file_structure --> tactical_recon
    architectural_blueprint[Step: architectural_blueprint]
    tactical_recon --> architectural_blueprint
    Input_relevant_source_code --> architectural_blueprint
    precision_strike[Step: precision_strike]
    architectural_blueprint --> precision_strike
    Input_relevant_source_code --> precision_strike
    qa_verification[Step: qa_verification]
    precision_strike --> qa_verification
    Input_todo_content --> qa_verification
```

[View Source YAML](../../workflows/technical/software_engineering/paw_workflow.workflow.yaml)
