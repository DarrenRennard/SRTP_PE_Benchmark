---
title: Constraint Satisfaction Metrics
type: topic
field: ee
created: 2026-07-14
updated: 2026-07-14
status: unverified
evidence: theoretical
tags: [ee, constraints, evidence-gate]
sources: [docs/citations.md#srtp-proposal, docs/citations.md#pemas-repo]
contradicts: []
review_by: 2026-08-14
---

# Constraint Satisfaction Metrics

Constraint satisfaction measures whether the candidate design respects limits that matter to engineering review.

Initial constraint groups:

- Electrical limits: voltage, current, power, ripple, and line loading.
- Thermal limits: junction temperature, heatsink assumptions, and capacitor ripple current.
- Safety limits: isolation, creepage, clearance, and derating placeholders.
- Simulation limits: convergence, stable operating point, and expected waveform windows.
- Evidence limits: whether required simulator, thermal, EMI, BOM, and human-review gates are closed.

## Red Team

**Steelman against:** Constraint lists can become checklists that imply safety without proving it.

**How it could be false:** Missing constraints, wrong units, or optimistic derating assumptions can make an invalid design appear acceptable.

**What would change my mind:** A reviewed benchmark suite includes domain expert signoff and catches known bad designs.

**Residual doubt:** Safety constraints require careful standards work beyond the starter benchmark.

