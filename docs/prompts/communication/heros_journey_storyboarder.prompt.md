---
title: Hero's Journey Storyboarder
---

# Hero's Journey Storyboarder

Craft a brief marketing narrative following the Hero's Journey structure.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/communication/heros_journey_storyboarder.prompt.yaml)

```yaml
---
name: Hero's Journey Storyboarder
version: 0.1.0
description: Craft a brief marketing narrative following the Hero's Journey structure.
metadata:
  domain: communication
  complexity: low
  tags:
  - hero
  - journey
  - storyboarder
  requires_context: false
variables:
- name: product
  description: The product or offering being discussed
  required: true
model: gpt-4o-mini
modelParameters:
  temperature: 0.7
messages:
- role: system
  content: 'The user provides a product or service to feature. Keep the style friendly.


    Craft a brief marketing narrative following the Hero''s Journey structure.'
- role: user
  content: '1. Write eight one-sentence beats from Ordinary World to Return with Elixir.

    1. Bold each beat title.

    1. After the beats, give a 25-word brand takeaway and one call to action.


    Inputs:

    - `{{product}}`: name of the product or service.


    Output format:

    Short paragraphs in markdown totalling no more than 140 words.


    Additional notes:

    Kid-friendly tone is optional.'
testData:
- vars:
    product: eco-friendly scooter
  expected: '**Ordinary World** - ...

    **Return with Elixir** - ...'
evaluators:
- name: Includes Return with Elixir beat
  string:
    contains: Return with Elixir

```
