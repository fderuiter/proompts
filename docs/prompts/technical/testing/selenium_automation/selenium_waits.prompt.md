---
title: Synchronization Strategy: Explicit Waits
---

# Synchronization Strategy: Explicit Waits

Replace brittle Thread.sleep() calls with dynamic Explicit or Fluent waits.

[View Source YAML](../../../../../prompts/technical/testing/selenium_automation/selenium_waits.prompt.yaml)

```yaml
---
name: 'Synchronization Strategy: Explicit Waits'
version: 0.1.0
description: Replace brittle Thread.sleep() calls with dynamic Explicit or Fluent waits.
metadata:
  domain: technical
  complexity: low
  tags:
  - testing
  - selenium
  - synchronization
  - strategy
  - explicit
  requires_context: false
variables:
- name: code_snippet
  description: The source code to analyze or modify
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: Refactor the provided Selenium script (Java or Python) to remove all 'time.sleep()' or 'Thread.sleep()' calls.
    Replace them with WebDriverWait using 'ExpectedConditions'. Specifically, wait for elements to be visible or clickable
    (e.g., an ID like 'submit-btn' or 'dynamic-content') with a defined timeout (e.g., 10-15 seconds) and handle potential
    TimeoutExceptions gracefully.
- role: user
  content: 'Refactor the following code to use Explicit Waits:


    <code>

    {{code_snippet}}

    </code>'
testData:
- input: "code_snippet: |\n  driver.findElement(By.id(\"submit\")).click();\n  Thread.sleep(5000);\n  driver.findElement(By.id(\"\
    result\")).getText();"
  expected: WebDriverWait wait
evaluators:
- name: Uses WebDriverWait
  regex: WebDriverWait
- name: No Thread.sleep
  regex: (?i)Thread\.sleep
  invert: true

```
