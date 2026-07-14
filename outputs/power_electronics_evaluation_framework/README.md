# Power Electronics Design Agent Evaluation Framework

A research framework for rigorously evaluating AI agents that perform power electronics design tasks. The project focuses on executable benchmarks, evidence-based reporting, and reusable research notes rather than building a new design agent.

The first benchmark track targets DC-DC converter workflows, especially flyback converter design. Later tracks extend the same harness to traction inverter tasks for electric vehicle power systems.

## Key Features

- Executable evaluation harness for agent outputs, benchmark tasks, scoring, and violation reports.
- Research-vault documentation modeled after SRTP_PowerElectronicsAI, with status, evidence strength, and red-team review on claims.
- Agent integration pattern inspired by PE-GPT and PE-MAS: agents can use RAG, model repositories, simulation tools, optimization, and multi-agent workflows, but evaluation remains independent.
- Metrics for engineering validity, constraint satisfaction, robustness, tool use, explainability, and reproducibility.
- Simulation-oriented extension points for PLECS, MATLAB/Simulink, SPICE, and Python evaluators.

## Repository Layout

```text
.github/                 GitHub workflows and issue templates
docs/                    Framework documentation and research-vault rules
research_notes/          Evidence-tracked EE and CS notes
agents/                  Example agent adapters and integration notes
benchmarks/              Executable benchmark tasks and deterministic evaluators
results/                 Evaluation output location
src/evaluation_harness/  Core Python runner, data models, and CLI
tests/                   Harness and benchmark tests
```

## Quick Start

```bash
git clone <your-repo-url>
cd power_electronics_evaluation_framework
python -m venv .venv
.venv\Scripts\activate
python -m pip install -e . --no-build-isolation
python agents/example_agent.py benchmarks/power_flow_benchmark/tasks/example_radial_bus.json results/example_agent_output.json
python -m evaluation_harness.cli run-power-flow benchmarks/power_flow_benchmark/tasks/example_radial_bus.json results/example_agent_output.json --report results/example_report.json
python -m unittest discover -s tests
```

On macOS or Linux, use `source .venv/bin/activate` instead of the Windows activation command.

If editable install is unavailable on a locked-down machine, run from the source tree with:

```powershell
$env:PYTHONPATH = "src;."
python agents/example_agent.py benchmarks/power_flow_benchmark/tasks/example_radial_bus.json results/example_agent_output.json
python -m evaluation_harness.cli run-power-flow benchmarks/power_flow_benchmark/tasks/example_radial_bus.json results/example_agent_output.json --report results/example_report.json
python -m unittest discover -s tests
```

## Documentation

Start with [docs/README.md](docs/README.md). The most important files are:

- [docs/SCHEMA.md](docs/SCHEMA.md) - research-note taxonomy, frontmatter, and red-team process.
- [docs/evaluation_guidelines.md](docs/evaluation_guidelines.md) - evaluation methodology and metrics.
- [docs/reference_research.md](docs/reference_research.md) - how SRTP_PowerElectronicsAI, PE-GPT, PE-MAS, and the project proposal shaped this repository.
- [benchmarks/power_flow_benchmark/README.md](benchmarks/power_flow_benchmark/README.md) - a runnable starter benchmark.

## Scope

This repository evaluates power electronics design agents. It does not assume one agent architecture. A candidate agent may be a single LLM prompt, a PE-GPT-like RAG and simulation workflow, a PE-MAS-style multi-agent system, or a conventional optimizer wrapped in an agent interface.

## Status

Initial research framework scaffold. Benchmark logic is intentionally small and deterministic so new tasks can be reviewed, extended, and replaced with higher-fidelity PLECS, MATLAB, or SPICE checks.
