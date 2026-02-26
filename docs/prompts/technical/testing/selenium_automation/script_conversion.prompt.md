---
title: Selenium Migration: Script Conversion
---

# Selenium Migration: Script Conversion

Translate recorded browser actions (Selenese) from Selenium IDE into structured Java test scripts.

[View Source YAML](../../../../../prompts/technical/testing/selenium_automation/script_conversion.prompt.yaml)

```yaml
---
name: 'Selenium Migration: Script Conversion'
version: 0.1.0
description: Translate recorded browser actions (Selenese) from Selenium IDE into structured Java test scripts.
metadata:
  domain: technical
  complexity: medium
  tags:
  - testing
  - selenium
  - migration
  - script
  - conversion
  requires_context: false
variables:
- name: package_name
  description: The name or identifier
  required: true
- name: selenese_code
  description: The source code to analyze or modify
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.2
messages:
- role: system
  content: You are a Selenium developer. Analyze the provided Selenese HTML or project file and convert the commands into
    a functional Java test class. Use the Page Object Model (POM) pattern, include explicit WebDriverWait commands for each
    interaction, and ensure compatibility with TestNG or JUnit. Refactor any hardcoded pauses into ExpectedConditions and
    ensure correct imports (e.g., from com.thoughtworks.selenium or Selenium 4).
- role: user
  content: 'Convert the following Selenese code/script to a robust Java Selenium test class.


    <selenese_code>

    {{selenese_code}}

    </selenese_code>


    <package_name>

    {{package_name}}

    </package_name>'
testData:
- input: "selenese_code: |\n  open /login\n  type id=user admin\n  type id=pass secret\n  click id=submit\npackage_name: com.example.tests"
  expected: public class LoginTest {
evaluators:
- name: Contains Java class definition
  regex: public class \w+

```
