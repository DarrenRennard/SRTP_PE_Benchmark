# Agents

This folder documents how candidate agents connect to the evaluation framework.

An agent can be:

- A single prompt or script.
- A PE-GPT-like RAG, model-zoo, optimization, and simulation workflow.
- A PE-MAS-like multi-agent system with specialist nodes and evidence gates.
- A conventional optimizer wrapped with a JSON interface.

## Required Interface

For each benchmark task, an agent should produce one JSON file. The benchmark README defines the required schema.

Minimum metadata:

```json
{
  "agent": {
    "name": "example-agent",
    "version": "0.1.0",
    "model": "none",
    "notes": "Deterministic baseline"
  },
  "solution": {}
}
```

## Example

Run the deterministic example agent:

```bash
python agents/example_agent.py benchmarks/power_flow_benchmark/tasks/example_radial_bus.json results/example_agent_output.json
```

Then evaluate it:

```bash
python -m evaluation_harness.cli run-power-flow benchmarks/power_flow_benchmark/tasks/example_radial_bus.json results/example_agent_output.json --report results/example_report.json
```

