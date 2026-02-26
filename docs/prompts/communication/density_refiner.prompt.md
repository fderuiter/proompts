---
title: Density Refiner
---

# Density Refiner

Craft a concise yet information-rich summary of provided text.

[View Source YAML](../../../prompts/communication/density_refiner.prompt.yaml)

```yaml
---
name: Density Refiner
version: 0.1.0
description: Craft a concise yet information-rich summary of provided text.
metadata:
  domain: communication
  complexity: low
  tags:
  - density
  - refiner
  requires_context: false
variables:
- name: input
  description: The primary input or query text for the prompt
  required: true
model: gpt-4
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'Use Chain-of-Density summarization to tighten coverage without length creep.


    <!-- markdownlint-disable MD029 -->


    1. Produce an entity-sparse gist in 120 words or fewer.

    2. List missing key nouns in 40 words or fewer.

    3. Rewrite a denser summary under 120 words using those nouns.

    4. End with a 15-word reflection on what detail improved.

    5. Label sections **Gist**, **Missing Entities**, **Dense Summary**, and **Reflection**.


    Chain-of-Density helps retain key entities while keeping the summary short.'
- role: user
  content: '{{input}}'
testData:
- input: Elephants migrate long distances for food and water.
  expected: '**Gist**

    Elephants travel for food and water.

    **Missing Entities**

    Savannah, herds.

    **Dense Summary**

    Elephant herds cross savannahs seeking water holes as seasons shift.

    **Reflection**

    Adding locations clarified context.'
evaluators:
- name: Output includes dense summary
  string:
    contains: Dense Summary

```
