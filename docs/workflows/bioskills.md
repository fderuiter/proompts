---
title: BioSkills Workflow
---

# BioSkills Workflow

A workflow for coaching, feedback, and assessment of bioskills.

## Workflow Diagram

```mermaid
graph TD
    Input_procedure_name[Input: procedure_name] --> Steps
    Input_procedure_notes[Input: procedure_notes] --> Steps
    coaching[Step: coaching]
    Input_procedure_name --> coaching
    feedback[Step: feedback]
    Input_procedure_notes --> feedback
    assessment[Step: assessment]
    Input_procedure_name --> assessment
```

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/workflows/scientific/bioskills.workflow.yaml)
