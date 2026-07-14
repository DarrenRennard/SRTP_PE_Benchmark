---
title: Hybrid RAG and Simulation Agent Pattern
type: topic
field: cs
created: 2026-07-14
updated: 2026-07-14
status: unverified
evidence: single-study
tags: [cs, rag, tool-use, simulation-grounded]
sources: [docs/citations.md#pegpt-repo, docs/citations.md#pegpt-paper]
contradicts: []
review_by: 2026-08-14
---

# Hybrid RAG and Simulation Agent Pattern

PE-GPT motivates a pattern where an LLM agent is supported by a domain knowledge base, model zoo, optimizer, and simulation repository. This is useful for power electronics because design reasoning often depends on equations, component data, waveform behavior, and simulator feedback.

In this framework, the evaluator should remain separate from the agent. The agent may use RAG or simulation internally, but benchmark scoring should use independent task files and deterministic checks.

## Red Team

**Steelman against:** If the agent and evaluator share the same assumptions, the benchmark may reward memorized design patterns instead of engineering capability.

**How it could be false:** RAG can retrieve plausible but wrong snippets, and simulation integration can be brittle.

**What would change my mind:** Independent benchmarks show RAG plus simulation agents generalize to unseen converter specifications.

**Residual doubt:** Retrieval quality and source reliability need explicit auditing.

