---
layout: default
title: Meta-Prompt Chain: L1 -> L2 -> L3 -> L4
parent: Workflows
nav_order: 99
---

# Meta-Prompt Chain: L1 -> L2 -> L3 -> L4

A workflow that implements the full meta-prompt generative chain.

## Workflow Diagram

<div class="mermaid">
graph TD
    Input_end_task[Input: end_task] --> Steps
    Input_policy_block[Input: policy_block] --> Steps
    Input_token_budget_l3[Input: token_budget_l3] --> Steps
    Input_token_limit_l4[Input: token_limit_l4] --> Steps
    Input_task_description[Input: task_description] --> Steps
    Input_input_block[Input: input_block] --> Steps
    Input_output_schema[Input: output_schema] --> Steps
    generate_l2_prompt[Step: generate_l2_prompt]
    Input_end_task --> generate_l2_prompt
    Input_policy_block --> generate_l2_prompt
    generate_l3_prompt[Step: generate_l3_prompt]
    generate_l2_prompt --> generate_l3_prompt
    Input_end_task --> generate_l3_prompt
    Input_token_budget_l3 --> generate_l3_prompt
    generate_l4_prompt[Step: generate_l4_prompt]
    generate_l3_prompt --> generate_l4_prompt
    Input_end_task --> generate_l4_prompt
    Input_policy_block --> generate_l4_prompt
    execute_task[Step: execute_task]
    generate_l4_prompt --> execute_task
    Input_task_description --> execute_task
    Input_input_block --> execute_task
    Input_output_schema --> execute_task
    Input_policy_block --> execute_task
    Input_token_limit_l4 --> execute_task
</div>

[View Source YAML](../../workflows/meta/meta_prompt_chain.workflow.yaml)
