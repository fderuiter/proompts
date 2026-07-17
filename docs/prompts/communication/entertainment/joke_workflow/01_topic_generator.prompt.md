---
title: Topic Generator
---

# Topic Generator

Generates a random topic for a joke.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/communication/entertainment/joke_workflow/01_topic_generator.prompt.yaml)

```yaml
name: Topic Generator
description: Generates a random topic for a joke.
model: gpt-4o-mini
modelParameters:
  temperature: 0.7
messages:
  - role: system
    content: "You are a creative assistant."
  - role: user
    content: "Give me a random topic for a joke. Output ONLY the topic name."
testData:
  - inputs: {}
    expected: "Chickens"
evaluators: []

```
