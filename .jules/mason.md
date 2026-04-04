# Mason's Journal - Critical Learnings Only

## Prompt Engineering
- **Missing XML delimiters for variables:** Discovered that numerous prompts failed to wrap user variables (`{{variable}}`) within XML tags (e.g. `<variable>{{variable}}</variable>`). Leaving input strings un-delimited creates a serious risk for prompt injection where the LLM might interpret user inputs as instructions rather than raw data.
- **Action Taken:** Enforced strict boundaries by wrapping input strings in XML delimiters to prevent prompt injection and improve variable parsing separation within the system prompt contexts.
