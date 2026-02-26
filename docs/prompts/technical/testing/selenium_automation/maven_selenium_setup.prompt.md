---
title: Project Configuration: Maven Setup
---

# Project Configuration: Maven Setup

Set up a Maven project structure and pom.xml file with necessary Selenium client libraries.

[View Source YAML](../../../../../prompts/technical/testing/selenium_automation/maven_selenium_setup.prompt.yaml)

```yaml
---
name: 'Project Configuration: Maven Setup'
version: 0.1.0
description: Set up a Maven project structure and pom.xml file with necessary Selenium client libraries.
metadata:
  domain: technical
  complexity: medium
  tags:
  - testing
  - selenium
  - project
  - configuration
  - maven
  requires_context: true
variables:
- name: java_version
  description: The java version to use for this prompt
  required: true
- name: test_framework
  description: The test framework to use for this prompt
  required: true
model: gpt-4o
modelParameters:
  temperature: 0.1
messages:
- role: system
  content: Generate a Maven pom.xml file for a Java-based Selenium automation project. Include dependencies for 'selenium-java',
    'testng' or 'junit', and 'webdrivermanager'. Configure the 'maven-surefire-plugin' for parallel execution, set the modelVersion
    to 4.0.0, and specify Java compiler source/target versions (e.g., 1.8 or 11) as required.
- role: user
  content: 'Generate a pom.xml for a Selenium project.


    Target Java Version: {{java_version}}

    Test Framework: {{test_framework}}'
testData:
- input: 'java_version: 11

    test_framework: testng'
  expected: <artifactId>selenium-java</artifactId>
evaluators:
- name: Contains selenium-java dependency
  regex: selenium-java

```
