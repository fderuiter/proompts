---
title: eClinical Integration Workflow
---

# eClinical Integration Workflow

A workflow for architecting an integration blueprint, creating a data mapping playbook, and compiling a regulatory validation checklist.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:#0d3a4d,stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:#183b27,stroke-width:2px,color:#ffffff;
    INPUT_integration_description([Input: integration_description]):::inputNode
    INPUT_mapping_requirements([Input: mapping_requirements]):::inputNode
    INPUT_validation_info([Input: validation_info]):::inputNode
    integration_blueprint[integration_blueprint<br><i>01_architect_integration_blueprint.prompt.md</i>]:::stepNode
    INPUT_integration_description -. input .-> integration_blueprint
    integration_blueprint -->|sequential| mapping_playbook
    mapping_playbook[mapping_playbook<br><i>02_data_mapping_transformation_playbook.prompt.md</i>]:::stepNode
    INPUT_mapping_requirements -. input .-> mapping_playbook
    mapping_playbook -->|sequential| validation_checklist
    validation_checklist[validation_checklist<br><i>03_regulatory_validation_checklist.prompt.md</i>]:::stepNode
    INPUT_validation_info -. input .-> validation_checklist
    linkStyle default stroke:#767676,stroke-width:2px;
```


