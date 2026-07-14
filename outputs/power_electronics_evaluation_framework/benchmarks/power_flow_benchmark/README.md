# Power Flow Benchmark

## Purpose

This starter benchmark evaluates whether an agent can return a structured engineering solution that satisfies power-flow-like constraints. It is intentionally simple so the framework can be run without PLECS, MATLAB, or SPICE.

The benchmark is not a replacement for a high-fidelity converter simulation. It demonstrates the evaluation pattern that later flyback and traction inverter benchmarks should follow.

## Task Definition

A task JSON file includes:

- `task_id`
- `base_mva`
- `buses`
- `lines`
- `tolerances`
- `scoring`

The included example is [tasks/example_radial_bus.json](tasks/example_radial_bus.json).

## Agent Output Schema

The agent output must be JSON:

```json
{
  "agent": {
    "name": "example-agent",
    "version": "0.1.0",
    "model": "none"
  },
  "solution": {
    "bus_voltages_pu": {
      "slack": 1.0,
      "load_1": 0.997
    },
    "line_flows_mva": {
      "slack->load_1": 1.226
    },
    "served_load_mw": 1.2,
    "explanation": "Short engineering rationale."
  }
}
```

## Evaluation Logic

The deterministic evaluator:

1. Checks required fields and numeric types.
2. Recomputes an approximate radial voltage drop using `V_to = V_from - (R * P_pu + X * Q_pu)`.
3. Recomputes apparent line flow from downstream load.
4. Checks bus voltage limits.
5. Checks line overloads.
6. Checks served load.
7. Returns a normalized score from 0 to 1 and explicit violations.

## Scoring

Default components:

- Format validity: 20 percent.
- Voltage consistency and limits: 30 percent.
- Line flow consistency and limits: 20 percent.
- Served load: 20 percent.
- Explanation presence: 10 percent.

The task file can override these weights.

## Example Usage

```bash
python agents/example_agent.py benchmarks/power_flow_benchmark/tasks/example_radial_bus.json results/example_agent_output.json
python -m evaluation_harness.cli run-power-flow benchmarks/power_flow_benchmark/tasks/example_radial_bus.json results/example_agent_output.json --report results/example_report.json
```

Run tests:

```bash
python -m unittest
```

