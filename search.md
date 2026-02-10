---
layout: page
title: Search
permalink: /search/
---

<style>
  #search-input {
    width: 100%;
    padding: 12px;
    font-size: 16px;
    border: 1px solid #ddd;
    border-radius: 4px;
    margin-bottom: 20px;
    box-sizing: border-box;
  }
  #results-container {
    list-style: none;
    padding: 0;
  }
  #results-container li {
    margin-bottom: 20px;
    padding-bottom: 20px;
    border-bottom: 1px solid #eee;
  }
  #results-container li:last-child {
    border-bottom: none;
  }
  #results-container li a {
    font-weight: bold;
    font-size: 18px;
    text-decoration: none;
    color: #0366d6;
    display: block;
    margin-bottom: 5px;
  }
  #results-container li a:hover {
    text-decoration: underline;
  }
  #results-container li p {
    margin: 0;
    color: #586069;
    font-size: 14px;
    line-height: 1.5;
  }
  .category-tag {
    display: inline-block;
    padding: 2px 6px;
    background-color: #f1f8ff;
    color: #0366d6;
    border-radius: 3px;
    font-size: 12px;
    margin-right: 8px;
    vertical-align: middle;
  }
</style>

<div id="search-container">
  <input type="text" id="search-input" placeholder="Type to search prompts...">
  <ul id="results-container"></ul>
</div>

<script src="https://unpkg.com/simple-jekyll-search@latest/dest/simple-jekyll-search.min.js"></script>
<script>
  window.simpleJekyllSearch = new SimpleJekyllSearch({
    searchInput: document.getElementById('search-input'),
    resultsContainer: document.getElementById('results-container'),
    json: '{{ site.baseurl }}/search.json',
    searchResultTemplate: '<li><a href="{{ site.baseurl }}/{url}" target="_blank"><span class="category-tag">{category}</span> {title}</a><p>{description}</p></li>',
    noResultsText: '<li>No results found</li>',
    limit: 50,
    fuzzy: false,
    exclude: []
  });
</script>
