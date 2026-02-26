---
title: Stochastic Architect
---

# Stochastic Architect

Analyzes a conversation or scenario to map it into a formal Stochastic State Model, defining states, risk scores, and a transition probability matrix.

[View Source YAML](../../../../../prompts/technical/data_science/stochastic_model_chain_workflow/01_stochastic_architect.prompt.yaml)

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
- input: 'Customer: "I want to return this item."

    Support: "Sure, what is the reason?"

    Customer: "It''s broken."

    Support: "I can offer a replacement."

    Customer: "No, just a refund."

    '
  expected: '<stochastic_model>

    ## State Definitions

    ## Risk Assignments

    ## Transition Matrix

    </stochastic_model>

    '
evaluators:
- name: Output wrapped in stochastic_model tags
  regex:
    pattern: (?s)<stochastic_model>.*</stochastic_model>
- name: Output includes Markdown table
  regex:
    pattern: (?s)\|.*\|.*\|.*
- name: Output includes Risk Score
  regex:
    pattern: (?i)Risk Score
version: 0.1.0

```
