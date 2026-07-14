---
title: Flyback Evaluation Plan
type: topic
field: ee
created: 2026-07-14
updated: 2026-07-14
status: unverified
evidence: theoretical
tags: [ee, flyback, dc-dc, plecs, matlab, simulation]
sources: [docs/citations.md#srtp-proposal, docs/citations.md#pemas-repo, docs/citations.md#pegpt-repo]
contradicts: []
review_by: 2026-08-14
---

# Flyback Evaluation Plan

The first domain benchmark track should focus on isolated flyback converter workflows.

## Stages

1. Specification-to-design: generate component-level design parameters from voltage, power, switching frequency, ripple, isolation, and efficiency targets.
2. Simulator setup: produce PLECS, MATLAB, or SPICE artifacts from the design.
3. Waveform analysis: interpret voltage and current traces for expected operating mode and failure signatures.
4. Engineering verification: check losses, temperature, ripple, stress margins, and component limits.

## Candidate Metrics

- Format validity.
- Simulation execution success.
- Output voltage error.
- Efficiency estimate or simulated efficiency.
- Switch voltage and current stress margin.
- Transformer turns ratio and magnetizing inductance plausibility.
- Thermal and BOM evidence gates.

## Red Team

**Steelman against:** Flyback design contains practical magnetics, isolation, EMI, and compensation details that simple benchmarks can miss.

**How it could be false:** An agent may pass a nominal calculation but fail loop stability, manufacturability, or safety review.

**What would change my mind:** A staged benchmark catches seeded flyback design errors and agrees with simulator or expert review.

**Residual doubt:** Magnetics validation needs more than simple equations.

