---
title: BioSkills Workflow
---

# BioSkills Workflow

A workflow for coaching, feedback, and assessment of bioskills.

## Workflow Diagram

```mermaid
graph TD
    INPUT_procedure_name([Input: procedure_name])
    INPUT_procedure_notes([Input: procedure_notes])
    coaching[coaching<br><i>01_hands_on_procedure_coaching.prompt.md</i>]
    INPUT_procedure_name -. procedure_name .-> coaching
    coaching -->|sequential| feedback
    feedback[feedback<br><i>02_simulated_clinical_scenario_feedback.prompt.md</i>]
    INPUT_procedure_notes -. procedure_notes .-> feedback
    feedback -->|sequential| assessment
    assessment[assessment<br><i>03_objective_skills_assessment.prompt.md</i>]
    INPUT_procedure_name -. procedure_name .-> assessment
```


