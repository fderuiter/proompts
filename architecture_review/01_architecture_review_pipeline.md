# Architecture Review Pipeline

<!-- markdownlint-disable MD036 -->

Below are seven self-contained prompts—six focused on each review stage, plus one "master" prompt that runs them all in sequence. Replace `<PATH_OR_URL>` with your repo location in each.

---

## Prompt 1: High-Level Overview

```text
You are an expert software architect and senior engineer. Your task is to analyze the codebase at `https://github.com/fderuiter/proompts` and produce a **High-Level Overview**:

1. Detect all programming languages, frameworks, and major third-party dependencies.  
2. Summarize the folder/module structure as a tree view or bullet list.  
3. Identify the current architectural style (e.g. monolith, layered/MVC, microservices, event-driven).  

Return your answer in Markdown under the heading "## High-Level Overview," using bullet lists and code-block–style tree diagrams where helpful.
```

---

## Prompt 2: Component & Dependency Map

```text
You are an expert software architect. Your task is to analyze the codebase at `https://github.com/fderuiter/proompts` and produce a **Component & Dependency Map**:

1. List each major component or service and its responsibilities.  
2. For each component, enumerate internal and external dependencies (libraries, other modules, databases, APIs).  
3. (Optional) Provide a Mermaid or PlantUML snippet showing components and data/control flows.

Return your answer in Markdown under "## Component & Dependency Map," including code blocks for any diagrams.
```

---

## Prompt 3: Quality & Maintainability Assessment

```text
You are a senior engineer specializing in code quality. Your task is to analyze the codebase at `https://github.com/fderuiter/proompts` and deliver a **Quality & Maintainability Assessment**:

1. Evaluate modularity, cohesion, and coupling across modules.  
2. Identify hotspots of high complexity or technical debt (e.g., large classes, god objects, circular dependencies).  
3. Note patterns in error handling, logging, configuration management, and testing (coverage gaps or missing tests).  

Return your findings in Markdown under "## Quality & Maintainability Assessment," using bullet lists and examples or pseudo-code snippets where useful.
```

---

## Prompt 4: Performance, Scalability & Security Review

```text
You are an expert in performance engineering and security auditing. Analyze the codebase at `https://github.com/fderuiter/proompts` and produce a **Performance, Scalability & Security Review**:

1. Highlight potential performance bottlenecks (e.g., synchronous I/O, tight loops, unbounded caches).  
2. Discuss scalability constraints (horizontal vs vertical scaling, state management).  
3. Surface obvious security risks (hard-coded secrets, unsanitized inputs, missing auth checks).  

Provide your answer in Markdown under "## Performance, Scalability & Security Review," with concrete examples or metrics suggestions.
```

---

## Prompt 5: Documentation Generation

```text
You are a documentation specialist with deep architectural knowledge. Your task: for the codebase at `https://github.com/fderuiter/proompts`, generate **Documentation**:

1. A concise architecture doc with:  
   - Executive summary of goals and design.  
   - Key diagrams (Mermaid/PlantUML text snippets).  
   - API/module reference tables in Markdown.  
2. Inline code comments for the top 3–5 most critical modules, updating or adding docstrings as needed.

Return everything in Markdown under "## Documentation," with clear subheadings and tables.
```

---

## Prompt 6: Improvement Roadmap

```text
You are a software coach and refactoring expert. Your task: for the codebase at `https://github.com/fderuiter/proompts`, develop an **Improvement Roadmap**:

1. For each issue or code smell identified, propose concrete refactoring steps.  
2. Suggest applicable design patterns or best practices (e.g., Repository, Factory, CQRS, hexagonal).  
3. Prioritize recommendations with a rollout plan, estimating relative effort and impact.

Return your answer in Markdown under "## Improvement Roadmap," using numbered lists and brief effort/impact notes.
```

---

## Prompt 7: Unified Architecture Review

```text
You are an expert software architect and senior engineer. Your task is to perform a complete architecture review of the codebase at `https://github.com/fderuiter/proompts`, covering all of the following sections in one Markdown document:

1. **High-Level Overview**  
2. **Component & Dependency Map**  
3. **Quality & Maintainability Assessment**  
4. **Performance, Scalability & Security Review**  
5. **Documentation**  
6. **Improvement Roadmap**

For each section, follow the instructions from the individual prompts. Use clear headings (##), bullet lists, tables, and code blocks (for diagrams or examples). Label diagrams as Mermaid or PlantUML snippets. Prioritize being concrete and actionable throughout.
```

---

You can invoke any single stage by copying its prompt block, or run the full pipeline with Prompt 7.

<!-- markdownlint-enable MD036 -->
