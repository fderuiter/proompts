# Workflow YAML Schema

This document outlines the structure of `.workflow.yaml` files, which are used to define and run chains of prompts.

## Top-Level Fields

A workflow file has the following top-level keys:

- `name` (string, required): A short, human-readable name for the workflow.
- `description` (string, optional): A concise description of what the workflow accomplishes.
- `inputs` (array, optional): A list of global inputs that the workflow requires. This is the data you provide when you start the workflow.
- `steps` (array, required): An ordered list of prompt execution steps that make up the workflow.

---

### `inputs`

The `inputs` section is an array of objects, where each object defines an input variable for the workflow.

- `name` (string, required): The name of the input variable.
- `description` (string, optional): A description of what this input represents.

**Example:**
```yaml
inputs:
  - name: "product_concept"
    description: "A brief description of the product idea."
```

---

### `steps`

The `steps` section is an array of objects, where each object represents a single step in the workflow. Each step executes a prompt.

- `step_id` (string, required): A unique identifier for the step within the workflow. This is used to reference the step's output in later steps.
- `prompt_file` (string, required): The path to the `.prompt.yaml` file to be executed in this step. The path should be relative to the repository root.
- `map_inputs` (object, required): An object that maps the variables required by the prompt to their data sources.
  - The keys of this object are the variable names in the prompt's messages (e.g., `{{variable_name}}`).
  - The values specify where to get the data from, using a template syntax:
    - `{{inputs.input_name}}`: To use one of the workflow's global inputs.
    - `{{steps.step_id.output}}`: To use the output from a previous step.

**Example:**
```yaml
steps:
  - step_id: "generate_product_brief"
    prompt_file: "agentic_coding/01_product_brief.prompt.yaml"
    map_inputs:
      product_concept: "{{inputs.product_concept}}"

  - step_id: "create_epics"
    prompt_file: "agentic_coding/02_project_brief_epic.prompt.yaml"
    map_inputs:
      product_brief: "{{steps.generate_product_brief.output}}"
```
In this example, the first step takes a global input `product_concept` and runs the `01_product_brief` prompt. The second step then takes the output of the first step (`generate_product_brief.output`) and uses it as the `product_brief` input for the `02_project_brief_epic` prompt.
