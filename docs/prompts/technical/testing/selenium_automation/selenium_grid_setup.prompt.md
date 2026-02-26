---
title: Cross-Browser Infrastructure: Selenium Grid
---

# Cross-Browser Infrastructure: Selenium Grid

Configure a Selenium Grid Hub and Nodes to distribute test execution.

[View Source YAML](../../../../../prompts/technical/testing/selenium_automation/selenium_grid_setup.prompt.yaml)

```yaml
---
name: 'Cross-Browser Infrastructure: Selenium Grid'
version: 0.1.0
description: Configure a Selenium Grid Hub and Nodes to distribute test execution.
metadata:
  domain: technical
  complexity: medium
  tags:
  - testing
  - selenium
  - cross-browser
  - infrastructure
  - grid
  requires_context: false
variables:
- name: browser_count
  description: The browser count to use for this prompt
  required: true
- name: grid_version
  description: The grid version to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.1
messages:
- role: system
  content: Provide the command-line instructions to initialize a Selenium Grid (2.0 or 4.0) infrastructure. Show how to launch
    a hub on port 4444 and register a node that supports multiple instances of Chrome and Firefox. Include parameters for
    platform settings and explain how to verify registration via terminal output or the Grid console.
- role: user
  content: Provide instructions for setting up Selenium Grid {{grid_version}} with {{browser_count}} nodes for Chrome and
    Firefox.
testData:
- input: 'grid_version: 4

    browser_count: 2'
  expected: java -jar selenium-server
evaluators:
- name: Contains java -jar command
  regex: java -jar

```
