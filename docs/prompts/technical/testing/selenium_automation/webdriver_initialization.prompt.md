---
title: Driver Configuration: WebDriver Initialization
---

# Driver Configuration: WebDriver Initialization

Initialize and configure WebDriver instances with specific browser options.

[View Source YAML](../../../../../prompts/technical/testing/selenium_automation/webdriver_initialization.prompt.yaml)

```yaml
---
name: 'Driver Configuration: WebDriver Initialization'
version: 0.1.0
description: Initialize and configure WebDriver instances with specific browser options.
metadata:
  domain: technical
  complexity: medium
  tags:
  - testing
  - selenium
  - driver
  - configuration
  - web
  requires_context: false
variables:
- name: browser
  description: The target browser (e.g., Chrome, Firefox)
  required: true
- name: proxy_url
  description: The URL to process or reference
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: Write a script to initialize a WebDriver (e.g., InternetExplorerDriver or ChromeDriver) using Capabilities/Options.
    Configure proxy settings for HTTP, FTP, and SSL (e.g., 'localhost:8080'). If using Selenium Base, provide the 'sbase'
    command to install the latest driver executable to the correct directory.
- role: user
  content: 'Create a WebDriver initialization script with the following requirements.


    Browser: {{browser}}

    Proxy: {{proxy_url}}'
testData:
- input: 'browser: Chrome

    proxy_url: localhost:8080'
  expected: ChromeOptions
evaluators:
- name: Configures Options
  regex: Options

```
