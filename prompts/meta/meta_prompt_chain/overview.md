# Meta Prompt Chain Overview

## Prompts
- **[Meta Prompt Architect](01_L1_meta-prompt-architect.prompt.yaml)**: Design an L2 prompt that instructs a Prompt Engineer to create a domain-specific template achieving `{{ end_task }}`.
- **[Prompt Engineer Template](02_L2_prompt-engineer.prompt.yaml)**: Produce an L3 task template that enables a Task Prototyper to fulfil `{{ end_task }}`.
- **[Task Prototyper](03_L3_task-prototyper.prompt.yaml)**: Generate a domain-specific L3 prompt that accomplishes `{{ end_task }}`.
- **[Worker Prompt](04_L4_worker_prompt.prompt.yaml)**: Execute the concrete task defined by the L3 template and return structured output.
