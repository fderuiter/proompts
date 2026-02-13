# eClinical Integration Workflow

A workflow for architecting an integration blueprint, creating a data mapping playbook, and compiling a regulatory validation checklist.

## Visual Flow

```mermaid
flowchart TD
    subgraph Inputs [Global Inputs]
        inp_integration_description((integration_description))
        inp_mapping_requirements((mapping_requirements))
        inp_validation_info((validation_info))
    end
    integration_blueprint["integration_blueprint<br/><small>prompts/clinical/eclinical_integration/01_architect_integration_blueprint.prompt.yaml</small>"]
    mapping_playbook["mapping_playbook<br/><small>prompts/clinical/eclinical_integration/02_data_mapping_transformation_playbook.prompt.yaml</small>"]
    validation_checklist["validation_checklist<br/><small>prompts/clinical/eclinical_integration/03_regulatory_validation_checklist.prompt.yaml</small>"]
    inp_integration_description -->|input| integration_blueprint
    inp_mapping_requirements -->|input| mapping_playbook
    inp_validation_info -->|input| validation_checklist
```
