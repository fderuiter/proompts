---
title: Test Environment: Python & Selenium Base
---

# Test Environment: Python & Selenium Base

Install the Selenium Base framework and environment using the Python package manager.

[View Source YAML](https://github.com/fderuiter/proompts/blob/main/prompts/technical/testing/selenium_automation/selenium_python_setup.prompt.yaml)

```yaml
---
name: 'Test Environment: Python & Selenium Base'
version: 0.1.0
description: Install the Selenium Base framework and environment using the Python package manager.
metadata:
  domain: technical
  complexity: low
  tags:
  - testing
  - selenium
  - test
  - environment
  - python
  requires_context: false
variables: []
model: gpt-4o
modelParameters:
  temperature: 0.1
messages:
- role: system
  content: Using pip3, provide the command to install the 'selenium-base' package within a Python virtual environment and
    explain how to verify the installation with the 'sbase' command.
- role: user
  content: Provide instructions to set up SeleniumBase in a python virtual environment.
testData:
- input: N/A
  expected: pip install seleniumbase
evaluators:
- name: Install command
  regex: pip install seleniumbase

```
