---
title: Advanced Design Patterns: Fluent Interface
---

# Advanced Design Patterns: Fluent Interface

Extend Page Objects with method chaining to create a more readable test API.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/technical/testing/selenium_automation/fluent_interface_selenium.prompt.yaml)

```yaml
---
name: 'Advanced Design Patterns: Fluent Interface'
version: 0.1.0
description: Extend Page Objects with method chaining to create a more readable test API.
metadata:
  domain: technical
  complexity: low
  tags:
  - testing
  - selenium
  - advanced
  - design
  - patterns
  requires_context: false
variables:
- name: java_class
  description: The java class to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: 'Modify existing Page Object classes to implement a Fluent Interface. Ensure that every method performing an action
    (e.g., ''setUsername'', ''setPassword'') returns ''this'' (the current page instance). Create an example test method demonstrating
    action chaining: page.open().login(''user'', ''pass'').verifySuccess();.'
- role: user
  content: 'Refactor the following Page Object to use a Fluent Interface.


    <java_class>

    {{java_class}}

    </java_class>'
testData:
- input: "java_class: |\n  public void setUsername(String u) { ... }\n  public void setPassword(String p) { ... }"
  expected: public LoginPage setUsername
evaluators:
- name: Methods return this or object
  regex: return this;

```
