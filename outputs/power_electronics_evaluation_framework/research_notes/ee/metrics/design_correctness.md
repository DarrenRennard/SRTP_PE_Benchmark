---
title: Design Correctness Metrics
type: topic
field: ee
created: 2026-07-14
updated: 2026-07-14
status: unverified
evidence: theoretical
tags: [ee, benchmark, simulation-grounded]
sources: [docs/citations.md#srtp-proposal]
contradicts: []
review_by: 2026-08-14
---

# Design Correctness Metrics

Design correctness measures whether an agent output satisfies the electrical behavior required by a task.

For early benchmarks, correctness should include:

- Required output format is valid.
- Calculated or simulated operating point satisfies the specification.
- Reported values use expected units.
- Claimed topology or operating mode matches the task.
- Any simulation file compiles or executes.

## Red Team

**Steelman against:** A benchmark can reward superficial numerical agreement while missing dynamics, parasitics, thermal stress, or unsafe design choices.

**How it could be false:** Simple deterministic checks may pass designs that fail in PLECS, MATLAB, or hardware.

**What would change my mind:** Higher-fidelity simulation or experimental validation shows the correctness score predicts real converter behavior.

**Residual doubt:** Correctness needs domain-specific simulators before it can support strong claims.

