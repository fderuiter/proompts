---
layout: home
title: Home
nav_order: 0
---

# Proompts

Welcome to **Proompts**, a curated collection of high-quality prompts and workflows for AI-assisted product development, regulatory compliance, and clinical research. 

Whether you are a Product Manager, Clinical Lead, or Software Engineer, this repository provides the building blocks to operationalize LLMs in your daily work.

## Getting Started

1. **Browse Categories**: Explore prompts by domain (e.g., [Clinical](clinical.md), [Software Engineering](software_engineering.md)).
2. **Run Workflows**: Use our [Workflows](workflows.md) to chain multiple prompts together for complex tasks like "Idea to Epic".
3. **Copy & Customize**: All prompts are in YAML format, ready to be used in your own tools or agents.

## Key Concepts

- **Prompts**: Single-task instructions for an LLM (e.g., "Review this code", "Draft a protocol").
- **Workflows**: Sequences of prompts that pass data from one step to the next to achieve a larger goal.
- **Agents**: The AI systems that execute these prompts and workflows.

## Browse by Category

- [Architecture](architecture.md)
- [Business](business.md)
- [Clinical](clinical.md)
- [Communication](communication.md)
- [Languages](languages.md)
- [Management](management.md)
- [Meta](meta.md)
- [Regulatory](regulatory.md)
- [Scientific](scientific.md)
- [Software Engineering](software_engineering.md)
- [Technical](technical.md)
- [Testing](testing.md)
- [Workflows](workflows.md)

## Search

<div class="search-container">
    <input type="text" id="search-input" placeholder="Search prompts & workflows..." style="width: 100%; padding: 10px; margin-bottom: 20px;">
    <ul id="results-container"></ul>
</div>

<script src="https://unpkg.com/simple-jekyll-search@latest/dest/simple-jekyll-search.min.js"></script>
<script>
    window.simpleJekyllSearch = new SimpleJekyllSearch({
        searchInput: document.getElementById('search-input'),
        resultsContainer: document.getElementById('results-container'),
        json: '{{ site.baseurl }}/search.json',
        searchResultTemplate: '<li><a href="{{ site.baseurl }}/{url}"><strong>{title}</strong></a><br><span style="font-size:0.8em">{description}</span></li>',
        noResultsText: 'No/results found',
        limit: 10,
        fuzzy: false
    })
</script>

## Contributing

We welcome contributions! Please check out the [GitHub repository](https://github.com/fderuiter/proompts) to submit a Pull Request.
