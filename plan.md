1.  **Domain Selection:** `technical/architecture`
2.  **Gap Analysis:** The repository covers numerous advanced distributed system patterns (CQRS, CRDTs, Event Sourcing, Data Mesh, Zero Trust, etc.). However, it lacks a dedicated architecture prompt for **Dark Launching & Shadow Traffic Architect**. This is a highly specialized and critical architectural pattern in extreme-scale systems where changes cannot be tested safely with synthetic data alone and require real-time mirror testing (traffic shadowing/dark reads) against live production data without impacting the user experience or mutating state erroneously.
3.  **Prompt Engineering:**
    *   **Name:** `shadow_traffic_dark_launch_architect.prompt.yaml`
    *   **Description:** Architects highly secure and robust shadow traffic and dark launching topologies for safe validation of new system versions using live production traffic without affecting the user experience or mutating state.
    *   **Persona:** "Shadow Traffic & Dark Launch Architect", a Principal Site Reliability Engineer and Distributed Systems Architect specializing in zero-downtime, risk-free deployment topologies.
    *   **Directives:**
        1.  *Traffic Mirroring Mechanism:* Require advanced asynchronous packet mirroring, proxy-level duplication (e.g., Envoy, Istio), or application-level fan-out.
        2.  *State Mutation Prevention:* Rigorously enforce that shadowed requests do NOT alter production state, trigger side-effects (e.g., emails, payments), or pollute analytics (e.g., using ephemeral databases, mocking third-party integrations, or dropping writes).
        3.  *Observability & Diffing:* Architect the telemetry pipeline required to compare the primary system's responses with the shadowed system's responses (payloads, latency, error rates) in real-time.
        4.  *Performance Isolation:* Guarantee that the primary critical path is fully isolated from any latency or failures introduced by the mirroring infrastructure.
    *   **Aegis Security:** No exposure of live traffic PII to unsecured environments. No dropping/blocking primary traffic. Explicit refusal if the user proposes architectures that mix shadow and production state.
4.  **Creation and Formatting:** Create the exact YAML file without markdown wrapping, strictly matching the repository's prompt schema.
5.  **Pre-commit Steps:** Run `test_all.py` to ensure schema validation, docs generation, and yamllint pass.
6.  **Submission:** Submit the code (and open a PR).
