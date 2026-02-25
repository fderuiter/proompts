# Meta Prompt Chain Overview

## Prompts
- **[Master Ultrameta Prompt Architect](00_L0_master-ultrameta.prompt.yaml)**: Construct a five-layer prompt stack (L0–L4) that reliably executes `{{end_task}}`.
- **[Meta Prompt Architect](01_L1_meta-prompt-architect.prompt.yaml)**: Design an L2 prompt that instructs a Prompt Engineer to create a domain-specific template achieving `{{end_task}}`.
- **[Prompt Engineer Template](02_L2_prompt-engineer.prompt.yaml)**: Produce an L3 task template that enables a Task Prototyper to fulfil `{{end_task}}`.
- **[Task Prototyper](03_L3_task-prototyper.prompt.yaml)**: Generate a domain-specific L3 prompt that accomplishes `{{end_task}}`.
- **[Worker Prompt](04_L4_worker_prompt.prompt.yaml)**: Execute the concrete task defined by the L3 template and return structured output.
- **[Agent Persona Generator](05_L5_agent_persona_generator.prompt.yaml)**: Generate detailed, high-integrity agent personas based on a provided role and goal, using a strict structural framework.
- **[AGENTS.md Checklist Generator](05_L5_agents-md-checklist.prompt.yaml)**: Create a best-practice checklist for writing an AGENTS.md file and provide a meta‑prompt to generate one from any repository.
- **[AI Coding Agent Plan Generator](05_L5_ai_coding_agent.prompt.yaml)**: Provide a structured plan for completing a coding task in an existing repository.
- **[Comprehensive Task Template](05_L5_comprehensive_task_template.prompt.yaml)**: Provide a reusable prompt that guides an AI through planning, execution and self-checking for any complex task.
- **[MECE Structuring Consultant](05_L5_mece_structuring.prompt.yaml)**: Reorganize brainstorm ideas into three mutually exclusive, collectively exhaustive buckets.
- **[Prompt Engineer Fact Checker](05_L5_prompt_engineer_fact_checker.prompt.yaml)**: Rewrite an original prompt so it is clear, fully sourced and produces accurate answers with inline citations.
- **[PromptCrafter GPT](05_L5_promptcrafter_gpt.prompt.yaml)**: Generate three distinct, best-practice prompts for a given topic.
- **[README Generator](05_L5_readme-generator.prompt.yaml)**: Scan an entire repository and produce a polished README.md covering everything a new developer needs.
