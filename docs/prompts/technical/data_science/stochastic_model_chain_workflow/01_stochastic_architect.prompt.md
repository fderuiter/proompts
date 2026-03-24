---
title: Stochastic Architect
---

# Stochastic Architect

Analyzes a conversation or scenario to map it into a formal Stochastic State Model, defining states, risk scores, and a transition probability matrix.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/technical/data_science/stochastic_model_chain_workflow/01_stochastic_architect.prompt.yaml)

```yaml
---
name: Stochastic Architect
description: Analyzes a conversation or scenario to map it into a formal Stochastic State Model, defining states, risk scores,
  and a transition probability matrix.
metadata:
  domain: technical
  complexity: high
  tags:
  - data-science
  - stochastic-modeling
  - architect
  - risk-assessment
  requires_context: true
variables:
- name: conversation_scenario
  description: The conversation transcript or scenario to analyze.
  required: true
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: "# Role\nYou are a Lead Data Scientist specializing in Natural Language Processing and Behavioral Modeling.\n\n\
    # Task\nAnalyze the provided conversation/scenario and map it into a formal Stochastic State Model. Do not write code\
    \ or simulate yet; focus strictly on defining the variables and transition logic.\n\n# Instructions\n1. **Define States:**\
    \ Break the interaction into 5-8 distinct conversational states (e.g., \"Intro,\" \"Objection,\" \"Resolution\").\n2.\
    \ **Assign Risk:** For each state, assign a static Risk Score ($R$) from 0.0 (Safe) to 1.0 (Critical Failure).\n3. **Transition\
    \ Matrix:** Create a Transition Probability Matrix.\n   - Rows must represent the \"Current State.\"\n   - Columns must\
    \ represent the \"Next State.\"\n   - **Constraint:** The sum of probabilities in each row MUST equal exactly 1.0.\n \
    \  - Use a Markdown table for this matrix.\n\n# Output Format\nWrap your entire response in `<stochastic_model>` tags.\n\
    Inside, use these sections:\n- `## State Definitions`\n- `## Risk Assignments`\n- `## Transition Matrix`\n"
- role: user
  content: 'Analyze the following scenario:


    <conversation_context>

    {{conversation_scenario}}

    </conversation_context>

    '
testData:
- input: 'Patient: "I need to speak to someone about my lab results, the portal says they are abnormal."

    Agent: "I understand, I can help you with that. Can I have your date of birth?"

    Patient: "12/04/1982. But I really need to know what this means, I''m very anxious."

    Agent: "Let me pull up your record. While I do that, are you experiencing any chest pain or shortness of breath?"

    Patient: "No, just a headache that won''t go away."

    Agent: "Okay, I see your results. I''ll need to transfer you to the triage nurse. Please hold."

    '
  expected: '<stochastic_model>

    ## State Definitions

    ## Risk Assignments

    ## Transition Matrix

    </stochastic_model>

    '
- input: 'Investigator: "We had a protocol deviation yesterday. A subject took the wrong dose."

    Sponsor: "Which subject? Was it reported?"

    Investigator: "Subject 004-A. Not yet, we are drafting the narrative now."

    Sponsor: "You need to submit it to the IRB within 24 hours. Stop dosing until we review the safety labs."

    Investigator: "Understood, we have halted the subject''s participation pending review."

    '
  expected: '<stochastic_model>

    ## State Definitions

    ## Risk Assignments

    ## Transition Matrix

    </stochastic_model>

    '
- input: ''
  expected: '<stochastic_model>

    ## State Definitions

    ## Risk Assignments

    ## Transition Matrix

    </stochastic_model>

    '
- input: 'DROP TABLE subjects; SELECT * FROM credentials; --'
  expected: '<stochastic_model>

    ## State Definitions

    ## Risk Assignments

    ## Transition Matrix

    </stochastic_model>

    '
evaluators:
- name: Output wrapped in stochastic_model tags
  regex:
    pattern: "(?s)<stochastic_model>.*## State Definitions.*## Risk Assignments.*## Transition Matrix.*</stochastic_model>"
- name: Output includes Markdown table
  regex:
    pattern: "(?s)\\|.*\\|.*\\|.*"
- name: Model checks risk scores and rows sum
  model:
    prompt: "Evaluate if the provided text properly defines 5 to 8 conversational states with risk assignments between 0.0 and 1.0, and a transition matrix where rows sum to exactly 1.0. The input must include '<stochastic_model>' tags. Output 'pass' if the text meets all these conditions, and 'fail' otherwise. Output ONLY 'pass' or 'fail'."
version: 0.1.0

```
