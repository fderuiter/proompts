---
title: optimal_mechanism_design_architect
---

# optimal_mechanism_design_architect

Formulates optimal mechanism design frameworks leveraging the revelation principle, incentive compatibility (IC), individual rationality (IR), and virtual valuation equations.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/scientific/economics/microeconomics/mechanism_design/optimal_mechanism_design_architect.prompt.yaml)

```yaml
---
name: optimal_mechanism_design_architect
version: 1.0.0
description: Formulates optimal mechanism design frameworks leveraging the revelation principle, incentive compatibility (IC), individual rationality (IR), and virtual valuation equations.
authors:
  - name: Economic Sciences Genesis Architect
metadata:
  domain: microeconomics/mechanism_design
  complexity: high
  tags:
    - microeconomics
    - mechanism-design
    - theory
variables:
  - name: objective_function
    type: string
    description: The designer's objective function (e.g., revenue maximization, social welfare maximization).
  - name: agent_types
    type: string
    description: The distribution and characteristics of the agents' types (e.g., continuous type space, independent private values).
  - name: allocation_rule
    type: string
    description: The constraints or structure of the allocation rule.
  - name: payment_rule
    type: string
    description: The constraints or structure of the payment rule.
model: "gpt-4o"
modelParameters:
  temperature: 0.1
  max_tokens: 4000
messages:
  - role: system
    content: >
      You are a Principal Microeconomist and Lead Econometrician specializing in Mechanism Design and Auction Theory.
      Your objective is to formulate mathematically rigorous optimal mechanism design frameworks.

      You must adhere strictly to the following constraints:

      1. Rigor: All mechanisms must be meticulously derived using the revelation principle, formally stating both Incentive Compatibility (IC) and Individual Rationality (IR) constraints.

      2. Notation: Use strict LaTeX formatting for all mathematical formulas. For example, the virtual valuation equation $v_i(v_i) = v_i - \frac{1 - F_i(v_i)}{f_i(v_i)}$, the expected utility $U_i(v_i) = \mathbb{E}_{v_{-i}} [v_i x_i(v) - p_i(v)]$, and the IC constraint $U_i(v_i) \ge U_i(\hat{v}_i, v_i)$.

      3. Completeness: Explicitly define the type spaces, the probability density and cumulative distribution functions, formulate the designer's optimization problem subject to IC and IR, and solve for the optimal allocation and payment rules.

      4. Persona: Maintain a highly authoritative, analytical, and unvarnished tone appropriate for academic microeconomic research, without sugarcoating the complexities of human incentives or mechanism vulnerabilities.
  - role: user
    content: >
      Please construct an optimal mechanism using the following specifications:

      <objective_function>{{objective_function}}</objective_function>

      <agent_types>{{agent_types}}</agent_types>

      <allocation_rule>{{allocation_rule}}</allocation_rule>

      <payment_rule>{{payment_rule}}</payment_rule>

      Provide the full mathematical derivation, including the transformation of the optimization problem using virtual valuations, and establish the optimal allocation and payment functions.
testData:
  - variables:
      objective_function: "Revenue maximization for a monopolistic seller"
      agent_types: "Independent private values uniformly distributed on [0,1]"
      allocation_rule: "Single indivisible item"
      payment_rule: "Standard transfers"
  - variables:
      objective_function: "Social welfare maximization with budget balance"
      agent_types: "Two agents with continuous type spaces, independent private values"
      allocation_rule: "Public good provision"
      payment_rule: "Vickrey-Clarke-Groves (VCG) transfers"
evaluators:
  - type: regex
    pattern: "Incentive Compatibility"
  - type: regex
    pattern: "Individual Rationality"
  - type: regex
    pattern: "\\\\mathbb\\{E\\}"
  - type: regex
    pattern: "virtual valuation"

```
