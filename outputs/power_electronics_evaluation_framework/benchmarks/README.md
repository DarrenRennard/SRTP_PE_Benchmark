# Benchmarks

Benchmarks define tasks, expected output schemas, deterministic evaluators, and scoring rules.

## Current Benchmarks

- [power_flow_benchmark](power_flow_benchmark/README.md) - starter executable benchmark for schema validity, voltage limits, line limits, served load, and approximate power-flow consistency.

## Benchmark Requirements

Each benchmark should provide:

- Task JSON schema.
- Agent output JSON schema.
- Deterministic evaluator.
- Scoring weights.
- Explicit violation messages.
- Example passing output.
- Notes on simulator dependencies, if any.

## Planned Benchmarks

- Flyback specification-to-design benchmark.
- Flyback simulation setup benchmark for PLECS or MATLAB.
- Waveform analysis benchmark.
- Engineering verification benchmark.
- Traction inverter extension benchmark.

