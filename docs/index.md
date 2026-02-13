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

## Explore by Domain

<div class="grid-container">
  <a href="clinical.html" class="card">
    <h3>🏥 Clinical</h3>
    <p>Protocols, monitoring, safety, and regulatory workflows.</p>
  </a>
  <a href="business.html" class="card">
    <h3>💼 Business</h3>
    <p>Market research, CFO insights, and operational planning.</p>
  </a>
  <a href="technical.html" class="card">
    <h3>💻 Technical</h3>
    <p>Architecture, software engineering, and code reviews.</p>
  </a>
  <a href="workflows.html" class="card">
    <h3>🔄 Workflows</h3>
    <p>End-to-end chains: "Idea to Epic" and "Protocol Design".</p>
  </a>
  <a href="regulatory.html" class="card">
    <h3>⚖️ Regulatory</h3>
    <p>FDA submissions, compliance checks, and gap analysis.</p>
  </a>
  <a href="management.html" class="card">
    <h3>📊 Management</h3>
    <p>Project tracking, leadership, and team effectiveness.</p>
  </a>
  <a href="system_architecture.html" class="card">
    <h3>🏗️ Architecture</h3>
    <p>System internals, simulation engine, and validation pipeline.</p>
  </a>
</div>

<style>
.grid-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-top: 20px;
}
.card {
  border: 1px solid #30363d; /* Matches dark theme border */
  border-radius: 6px;
  padding: 20px;
  text-decoration: none !important;
  color: inherit;
  transition: transform 0.2s, box-shadow 0.2s;
  background-color: #0d1117; /* Matches dark theme bg */
}
.card:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.4);
  border-color: #58a6ff;
}
.card h3 {
  margin-top: 0;
  color: #58a6ff;
}
</style>

## Search


<div class="search-container">
    <input type="text" id="search-input" placeholder="Search prompts..." style="width: 100%; padding: 10px; margin-bottom: 20px;">
    <ul id="results-container"></ul>
</div>

<script src="https://unpkg.com/simple-jekyll-search@latest/dest/simple-jekyll-search.min.js"></script>
<script>
    window.simpleJekyllSearch = new SimpleJekyllSearch({
        searchInput: document.getElementById('search-input'),
        resultsContainer: document.getElementById('results-container'),
        json: '{{ site.baseurl }}/search.json',
        searchResultTemplate: '<li><a href="{{ site.baseurl }}/{url}"><strong>{title}</strong></a><br><span style="font-size:0.8em">{description}</span></li>',
        noResultsText: 'No prompts found',
        limit: 10,
        fuzzy: false
    })
</script>
