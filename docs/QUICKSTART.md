# 🚀 Quickstart: 5-Minute Onboarding

Welcome to the **Proompts** repository! If you're a new developer wondering where to begin, this guide will help you understand the architecture and run your first AI workflows in under 5 minutes.

## 🧭 What is this repository?
Proompts treats **"Prompts as Code"**.
Instead of copying and pasting text into ChatGPT, we store AI instructions as structured `.prompt.yaml` files. This allows us to version control them, test them with `testData`, and chain them together into complex **Workflows**.

## 🤔 Why do we do this?
- **Reproducibility:** A prompt in YAML behaves the same way for everyone.
- **Testing:** We can simulate logic without spending money on LLM API calls.
- **Automation:** We can link prompts to build autonomous agents (e.g., passing a codebase to an Architect prompt, and its output to a Developer prompt).

## 🛠️ How to run your first simulation

### 1. Setup your environment
First, ensure you have Python 3 and install the required tooling:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Search for a Prompt
Let's find a prompt to test. Use the search script to find a "Code Reviewer":

```bash
promptops search "code review"
```

### 3. Run a Workflow Simulation
We don't need an API key to test our logic! Our `promptops workflow` engine simulates LLM responses using the `testData` embedded in our prompts.

Let's simulate the **Agentic Coding Workflow** (which chains multiple engineering prompts together):

```bash
# Run the workflow and provide a starting variable (-i)
promptops workflow workflows/technical/agentic_coding.workflow.yaml -i product_concept="A new time-tracking app"
```

> [!TIP]
> Add the `-v` (verbose) flag to see exactly how inputs map to the prompts at each step!
> ```bash
> promptops workflow workflows/technical/agentic_coding.workflow.yaml -i product_concept="A new time-tracking app" -v
> ```

### 4. Verify your changes
Before pushing any new prompts or documentation, you must run the validation suite to ensure schemas and links are intact:

```bash
./scripts/validate_prompts.sh
```

## 📚 What's Next?
Now that you understand the mechanics, check out these deeper guides:
- **[Agent Integration](mcp_integration.md):** Connect the prompt library to Claude Desktop using the Model Context Protocol (MCP).
- **[Usage Guide](USAGE.md):** How to integrate these prompts with real LLM APIs in Python.
- **[Workflow Guide](workflow_guide.md):** Learn how to build your own `.workflow.yaml` files.
- **[Best Practices](BEST_PRACTICES.md):** The definitive guide to writing high-quality prompts.
