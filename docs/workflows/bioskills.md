---
title: BioSkills Workflow
---

# BioSkills Workflow

A workflow for coaching, feedback, and assessment of bioskills.

## Workflow Diagram

```mermaid
graph TD
    classDef stepNode fill:#1a5f7a,stroke:#0d3a4d,stroke-width:2px,color:#ffffff;
    classDef inputNode fill:#2c5e43,stroke:#183b27,stroke-width:2px,color:#ffffff;
    INPUT_procedure_name([Input: procedure_name]):::inputNode
    INPUT_procedure_notes([Input: procedure_notes]):::inputNode
    coaching[coaching<br><i>01_hands_on_procedure_coaching.prompt.md</i>]:::stepNode
    INPUT_procedure_name -. procedure_name .-> coaching
    coaching -->|sequential| feedback
    feedback[feedback<br><i>02_simulated_clinical_scenario_feedback.prompt.md</i>]:::stepNode
    INPUT_procedure_notes -. procedure_notes .-> feedback
    feedback -->|sequential| assessment
    assessment[assessment<br><i>03_objective_skills_assessment.prompt.md</i>]:::stepNode
    INPUT_procedure_name -. procedure_name .-> assessment
    linkStyle default stroke:#767676,stroke-width:2px;
```


