# SRTP PE Benchmark

*SRTP research on improving and evaluating AI agents for power electronics design, building on PE-GPT 2.0.*

A research framework for rigorously evaluating AI agents that perform power electronics design tasks. The project focuses on executable benchmarks, evidence-based reporting, and reusable research notes rather than building a new design agent.

The first benchmark track targets DC-DC converter workflows, especially flyback converter design. Later tracks extend the same harness to traction inverter tasks for electric vehicle power systems.

**Current status:** The PE-GPT 2.0 source has been imported as the starting baseline. The SRTP agent improvements, evaluation harness, and benchmark results described below are planned work.

[Research plan](docs/RESEARCH_PLAN.md) · [Research notes](docs/RESEARCH_NOTES.md) · [Original PE-GPT 2.0 documentation](README_PE_GPT_2_0.md) · [Upstream repository](https://github.com/spongelovesorange/PE-GPT-2.0)

## Research objective

We aim to measure whether targeted changes to existing PE-MAS agents improve the correctness and reliability of power electronics design workflows. Each improvement will be compared with the original implementation using fixed test cases, independently reviewed expected outcomes, and reproducible experiment records.

## Initial agent improvements

| Agent | Planned improvement | Evaluation focus |
| --- | --- | --- |
| Requirements | Normalize units, identify missing or conflicting specifications, and preserve confirmed values during follow-up changes. | Field accuracy, missing-field detection, update preservation, and unsupported assumptions. |
| Reporter | Distinguish requirements, calculations, simulation results, and missing evidence; preserve numerical values and validation status. | Numerical fidelity, status consistency, unsupported claims, and report generation success. |

These are the first two improvement targets. We will inspect existing behavior and reproduce failures before deciding which changes are needed.

## Research roadmap

| Phase | Planned work | Deliverable |
| --- | --- | --- |
| 1. Understand flyback converters | Study switching operation, magnetics, CCM/DCM, component stress, and simulation waveforms; trace one PE-MAS request. | Worked design example and technical notes. |
| 2. Establish the baseline | Record the original code version and environment; define evaluation cases and scoring rules. | Baseline outputs and reviewed test fixtures. |
| 3. Improve selected agents | Implement focused Requirements and Reporter changes on separate branches. | Reviewed pull requests with regression checks. |
| 4. Compare before and after | Evaluate both versions with the same inputs, model settings, and runtime budgets. | Raw outputs, comparison tables, and failure analysis. |
| 5. Extend the benchmark | Expand DC-DC coverage, then investigate traction inverter tasks for electric vehicle power systems. | Additional tasks and evaluators after the initial track is validated. |

## How improvements will be measured

The initial study will evaluate each agent in isolation. Requirements tests will reuse identical messages and starting specifications. Reporter tests will reuse identical saved workflow states so that upstream changes do not distort the comparison.

For each agent, we propose 30 reviewed cases: 20 for development and 10 held out for final evaluation. LLM-dependent held-out cases will be repeated three times with fixed model settings and controlled memory.

| Agent | Primary metrics |
| --- | --- |
| Requirements | Correct field values, missing-field recall, preservation of unchanged fields, and unsupported assumption rate. |
| Reporter | Correct reported values, consistency with supplied validation status, unsupported claim rate, and successful report generation. |
| Both | Runtime, token use where available, repeatability, and remaining failure cases. |

**Results:** No SRTP before-and-after evaluation results have been published yet. The research plan defines proposed experiments, not achieved performance.

## Run the imported PE-MAS baseline

Use Python 3.12. For Windows Git Bash:

```bash
git clone https://github.com/DarrenRennard/SRTP_PE_Benchmark.git
cd SRTP_PE_Benchmark

py -3.12 -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
cp -n .env.example .env
```

On macOS or Linux, create the environment with `python3 -m venv .venv` and activate it with `source .venv/bin/activate`.

Configure `.env` for your model provider before model-backed tasks, then run:

```bash
python server.py
```

Open <http://127.0.0.1:8000>. Real PLECS simulation requires a configured, licensed PLECS installation. Full configuration details are in the [original documentation](README_PE_GPT_2_0.md#connect-your-tools).

## Research notes

Brief summaries of papers we have read and ideas to apply to PE-GPT 2.0:

| Paper | Main idea | Possible application |
| --- | --- | --- |
| ReAct | Interleave planning, tool actions, and observations. | Extend existing agent traces with actual tool results and feedback before the next action. |
| EngDesign | Evaluate functional engineering designs with executable checks and simulation. | Check flyback designs against specifications using validated reference cases and simulation evidence. |
| xbench | Build evaluations around real professional tasks and useful outcomes. | Use realistic power electronics requests and measure engineering validity, time, and manual correction effort. |
| PaperBench | Decompose complex tasks into weighted criteria and verify execution separately from implementation. | Score intermediate workflow progress and distinguish generated artifacts, successful runs, and verified results. |

See [Research notes and PE-GPT 2.0 implementation ideas](docs/RESEARCH_NOTES.md) for short summaries, source references, and concrete starting points. All implementation ideas are proposed work.

## Attribution

This SRTP project builds on [PE-GPT 2.0](https://github.com/spongelovesorange/PE-GPT-2.0) by **Shi Qiu, Fanfan Lin, and Xinze Li**, which builds on the original [PE-GPT](https://github.com/XinzeLee/PE-GPT).

The imported implementation is prior work. Our planned contribution is to improve selected agents and develop reproducible evaluation methods. The original README, paper citation, reported results, and acknowledgments are preserved in [README_PE_GPT_2_0.md](README_PE_GPT_2_0.md); those results belong to the upstream project.
