<!-- markdownlint-disable MD029 -->
---
id: readme-generator
title: README Generator
category: meta_prompts
author: proompts team
created: 2024-01-01
last_modified: 2024-01-01
tested_model: gpt-4o
temperature: 0.2
tags: [meta, documentation]
---

# README Generator

## Purpose

Scan an entire repository and produce a polished README.md covering everything a new developer needs.

## Context

You are an expert technical writer and software engineer.

## Instructions

1. Enumerate all files with emphasis on dependency manifests, configuration, Dockerfiles and CI workflows.
1. Extract package names, version constraints and commands.
1. Generate sections: project title, purpose, features, tech stack, architecture overview, setup instructions, development commands, testing, deployment, usage examples, troubleshooting, contribution guidelines, license and acknowledgements.
1. Use level‑1 heading for the title and level‑2 headings for main sections.
1. Add `<!-- TODO -->` comments where information is missing and keep lines under 100 characters.

## Inputs

- `{{repo_access}}` – repository path or URL

## Output Format

Complete README.md between triple backticks.

## Additional Notes

Return only the README content and mention how to give the agent repository access in the instructions.
