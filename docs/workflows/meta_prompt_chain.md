---
title: Meta-Prompt Chain: L1 -> L2 -> L3 -> L4
---

# Meta-Prompt Chain: L1 -> L2 -> L3 -> L4

A workflow that implements the full meta-prompt generative chain.

## Workflow Diagram

```mermaid
graph TD
    INPUT_end_task([Input: end_task])
    INPUT_policy_block([Input: policy_block])
    INPUT_token_budget_l3([Input: token_budget_l3])
    INPUT_token_limit_l4([Input: token_limit_l4])
    INPUT_task_description([Input: task_description])
    INPUT_input_block([Input: input_block])
    INPUT_output_schema([Input: output_schema])
    generate_l2_prompt[generate_l2_prompt<br><i>01_L1_meta-prompt-architect.prompt.md</i>]
    INPUT_end_task -. end_task .-> generate_l2_prompt
    INPUT_policy_block -. policy_block .-> generate_l2_prompt
    generate_l2_prompt -->|sequential| generate_l3_prompt
    generate_l3_prompt[generate_l3_prompt<br><i>02_L2_prompt-engineer.prompt.md</i>]
    generate_l2_prompt -. generated_prompt .-> generate_l3_prompt
    INPUT_end_task -. end_task .-> generate_l3_prompt
    INPUT_token_budget_l3 -. token_budget_l3 .-> generate_l3_prompt
    generate_l3_prompt -->|sequential| generate_l4_prompt
    generate_l4_prompt[generate_l4_prompt<br><i>03_L3_task-prototyper.prompt.md</i>]
    generate_l3_prompt -. generated_prompt .-> generate_l4_prompt
    INPUT_end_task -. end_task .-> generate_l4_prompt
    INPUT_policy_block -. policy_block .-> generate_l4_prompt
    INPUT_token_budget_l3 -. token_budget_l3 .-> generate_l4_prompt
    generate_l4_prompt -->|sequential| execute_task
    execute_task[execute_task<br><i>04_L4_worker_prompt.prompt.md</i>]
    generate_l4_prompt -. generated_prompt .-> execute_task
    INPUT_task_description -. task_description .-> execute_task
    INPUT_input_block -. input_block .-> execute_task
    INPUT_output_schema -. output_schema .-> execute_task
    INPUT_policy_block -. policy_block .-> execute_task
    INPUT_token_limit_l4 -. token_limit_l4 .-> execute_task
```


