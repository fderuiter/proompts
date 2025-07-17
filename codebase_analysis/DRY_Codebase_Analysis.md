# DRY Codebase Analysis

**Objective**  
Identify every meaningful opportunity to remove code duplication and enforce the **DRY** (Don’t Repeat Yourself) principle.

---

## Scope of Analysis

1. Locate duplicated logic, structures, or patterns across modules, classes, functions, and tests.  
1. Recommend consolidation via abstraction, reusable utilities, or modularization.  
1. Flag duplicated tests and propose shared helpers or fixtures.

---

## Task-Stub Specification

For each duplication detected, output a **task stub** using the fields below.  
Create **one stub per distinct duplication site**.

| Field | Description |
|-------|-------------|
| **ID** | `DRY-NNN` (sequential) |
| **Location** | File path(s) and line range(s) where duplication appears |
| **Issue&nbsp;Summary** | One-sentence description of what is duplicated |
| **Suggested&nbsp;Change** | Concrete refactor (e.g., “Extract function `parseUser` to `utils/user.ts` and call from A, B, C”) |
| **Rationale** | Why this reduces repetition or risk |
| **Dependencies** | Other task IDs this change relies on (if any) |
| **Effort** | `S`, `M`, or `L` (author’s estimate) |

Return the stubs as a **markdown table**, sorted by effort (S → L).

---

## Input

- Root path to the codebase  
- Programming languages used  
- Framework or architectural context if applicable  
