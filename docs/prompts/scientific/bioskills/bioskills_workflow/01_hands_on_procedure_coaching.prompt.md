---
title: Hands-On Procedure Coaching
---

# Hands-On Procedure Coaching

Coach a trainee through a vascular access technique using a training model.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/scientific/bioskills/bioskills_workflow/01_hands_on_procedure_coaching.prompt.yaml)

```yaml
---
name: Hands-On Procedure Coaching
version: 0.1.0
description: Coach a trainee through a vascular access technique using a training model.
metadata:
  domain: scientific
  complexity: low
  tags:
  - bioskills
  - hands-on
  - procedure
  - coaching
  requires_context: false
variables:
- name: procedure_name
  description: specific procedure being practiced
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are a senior interventional cardiologist. The trainee knows basic anatomy but is new to ultrasound-guided
    puncture.


    Emphasize common mistakes to avoid during training.'
- role: user
  content: '1. Provide 5–7 bullet-step instructions with brief rationale.

    2. Highlight key anatomical landmarks visible via ultrasound.

    3. Offer troubleshooting tips.

    4. Include at least one safety checkpoint.


    Inputs:

    - `{{procedure_name}}` — specific procedure being practiced


    Output format:

    Bullet list of steps and checkpoints.'
testData:
- vars:
    procedure_name: example_procedure_name
  expected: '- '
evaluators:
- name: Output starts with a bullet
  string:
    startsWith: '- '

```
