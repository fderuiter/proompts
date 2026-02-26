---
title: Framework Best Practices: Locator Strategy
---

# Framework Best Practices: Locator Strategy

Transition from brittle XPaths to robust locators like ID or CSS selectors.

[View Source YAML](../../../../../prompts/technical/testing/selenium_automation/locator_optimization.prompt.yaml)

```yaml
---
name: 'Framework Best Practices: Locator Strategy'
version: 0.1.0
description: Transition from brittle XPaths to robust locators like ID or CSS selectors.
metadata:
  domain: technical
  complexity: low
  tags:
  - testing
  - selenium
  - framework
  - best
  - practices
  requires_context: false
variables:
- name: locators
  description: The locators to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: Review the provided code snippet containing dynamic or brittle XPaths (e.g., '//div@class="dynamic-class"'). Refactor
    the locators to use By.id, CSS selectors targeting data-action attributes, or other robust selection strategies as per
    best practices.
- role: user
  content: 'Optimize the following Selenium locators for stability.


    <locators>

    {{locators}}

    </locators>'
testData:
- input: "locators: |\n  driver.findElement(By.xpath(\"//div[3]/span[2]\"));"
  expected: By.id
evaluators:
- name: Suggests robust locators
  regex: (By\.id|By\.cssSelector|data-)

```
