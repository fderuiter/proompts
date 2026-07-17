---
title: Principal Architect Workflow (PAW)
---

# Principal Architect Workflow (PAW)

A state-machine workflow for disciplined software engineering tasks, enforcing Design, Refactor, Implementation, and QA phases.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:var(--md-default-fg-color,var(--text-color,#0d3a4d)),stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:var(--md-default-fg-color,var(--text-color,#183b27)),stroke-width:2px,color:#ffffff;
    INPUT_todo_content([Input: todo_content]):::inputNode
    INPUT_file_structure([Input: file_structure]):::inputNode
    INPUT_relevant_source_code([Input: relevant_source_code]):::inputNode
    tactical_recon[tactical_recon<br><i>paw_01_tactical_recon.prompt.md</i>]:::stepNode
    INPUT_todo_content -. todo_content .-> tactical_recon
    INPUT_file_structure -. file_structure .-> tactical_recon
    tactical_recon -->|sequential| architectural_blueprint
    architectural_blueprint[architectural_blueprint<br><i>paw_02_architectural_blueprint.prompt.md</i>]:::stepNode
    tactical_recon -. tactical_brief .-> architectural_blueprint
    INPUT_relevant_source_code -. relevant_source_code .-> architectural_blueprint
    architectural_blueprint -->|sequential| precision_strike
    precision_strike[precision_strike<br><i>paw_03_precision_strike.prompt.md</i>]:::stepNode
    architectural_blueprint -. design_spec .-> precision_strike
    INPUT_relevant_source_code -. relevant_source_code .-> precision_strike
    precision_strike -->|sequential| qa_verification
    qa_verification[qa_verification<br><i>paw_04_qa_verification.prompt.md</i>]:::stepNode
    precision_strike -. implementation_code .-> qa_verification
    INPUT_todo_content -. todo_content .-> qa_verification
    linkStyle default stroke:var(--md-default-fg-color,var(--text-color,#767676)),stroke-width:2px;
```

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/workflows/technical/software_engineering/paw_workflow.workflow.yaml)
