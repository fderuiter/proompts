# SOLID Codebase Analysis

**Objective**  
Evaluate the codebase against the five **SOLID** object-oriented design principles and produce concrete refactoring tasks.

---

## Scope of Analysis

1. **Single Responsibility Principle (SRP)** – Split classes/functions with multiple concerns.  
1. **Open/Closed Principle (OCP)** – Enable extension without modifying existing code.  
1. **Liskov Substitution Principle (LSP)** – Ensure subclasses honor base-type contracts.  
1. **Interface Segregation Principle (ISP)** – Decompose broad interfaces into cohesive ones.  
1. **Dependency Inversion Principle (DIP)** – Depend on abstractions, not concretes; introduce dependency injection.

---

## Task-Stub Specification

Generate one task stub per SOLID violation.

| Field | Description |
|-------|-------------|
| **ID** | `SOLID-NNN` (sequential) |
| **Principle** | `SRP`, `OCP`, `LSP`, `ISP`, or `DIP` |
| **Location** | File/class/function and line range |
| **Issue&nbsp;Summary** | One-sentence description of the violation |
| **Suggested&nbsp;Change** | Specific refactor (e.g., “Extract `EmailSender` from `UserService` to satisfy SRP”) |
| **Rationale** | How the change aligns with the principle |
| **Dependencies** | Other task IDs, if applicable |
| **Effort** | `S`, `M`, or `L` |

Return the stubs in a markdown table, **grouped by principle** and sorted by effort within each group.

---

## Input

- Root path to the codebase  
- Programming languages used  
- Framework or architectural context if applicable  
