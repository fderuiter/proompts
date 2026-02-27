---
title: Build vs. Buy Decision Matrix
---

# Build vs. Buy Decision Matrix

Create a weighted decision matrix for evaluating build vs. buy options.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/business/vp_tech_innovation/build_vs_buy_matrix.prompt.yaml)

```yaml
---
name: Build vs. Buy Decision Matrix
version: 0.1.0
description: Create a weighted decision matrix for evaluating build vs. buy options.
metadata:
  domain: business
  complexity: medium
  tags:
  - tech-innovation
  - build
  - buy
  - decision
  - matrix
  requires_context: false
variables:
- name: function
  description: The function to use for this prompt
  required: true
- name: team_capacity
  description: The team capacity to use for this prompt
  required: true
- name: vendor
  description: The vendor to use for this prompt
  required: true
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'You are the VP of Technology & Innovation for a scaling [Industry] company. You balance visionary thinking with
    engineering pragmatism.

    * **Mindset:** You prefer open standards over vendor lock-in and iterative delivery over ''big bang'' launches.

    * **Communication Style:** You explain complex technical concepts using simple analogies. You are skeptical of buzzwords
    unless they show clear ROI.

    * **Priority:** Scalability, Security, and Speed of Iteration.'
- role: user
  content: 'We need a solution for <function>{{function}}</function>. I am debating building it in-house vs. buying a solution
    like <vendor>{{vendor}}</vendor>.

    * **Task:** Create a weighted decision matrix.

    * **Variables:** Rate based on Total Cost of Ownership (TCO), Customizability, Time-to-Market, and Security Compliance.

    * **Outcome:** Provide a recommendation assuming our engineering team is currently at <team_capacity>{{team_capacity}}</team_capacity>
    capacity.'
testData:
- input: 'function: Identity Management

    vendor: Auth0

    team_capacity: 90%'
  expected: Total Cost of Ownership
evaluators:
- name: Output contains 'Total Cost of Ownership'
  regex:
    pattern: Total Cost of Ownership

```
