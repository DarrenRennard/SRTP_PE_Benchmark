# Reference Research Summary

Captured: 2026-07-14

This repository was shaped by the SRTP proposal PDF and three reference GitHub projects.

## SRTP Proposal

The proposal defines the project as an evaluation framework, not a new AI model. Its first target is DC-DC converter design, especially flyback converters, followed by traction inverter tasks for electric vehicle applications. It calls for Python orchestration, simulation integration with MATLAB or PLECS, and metrics such as format validity, execution success, functional correctness, constraint satisfaction, and reasoning consistency.

Design implication: this repository starts with a small executable benchmark and leaves clear extension points for PLECS, MATLAB, waveform parsing, and engineering verification tasks.

## SRTP_PowerElectronicsAI

The `srtp_docs` folder uses a research-vault structure with `SCHEMA.md`, `catalog.md`, `citations.md`, `sources/`, field folders for EE and CS, index notes, changelogs, and lint reports. It also emphasizes truth status, evidence strength, and mandatory red-team review for claims.

Design implication: this repository adopts the same evidence-aware documentation style, but adapts the field folders to `research_notes/ee/` and `research_notes/cs/` so research notes sit beside executable benchmarks.

## PE-GPT

PE-GPT presents a hybrid power electronics design architecture combining an LLM agent, RAG knowledge base, model zoo, optimization, simulation repository, and Streamlit UI. Its examples include flyback converter design, DAB modulation optimization, and buck converter parameter design. It also documents PLECS XML-RPC setup for simulation-backed workflows.

Design implication: this framework treats RAG, model repositories, optimizers, and simulation tools as valid agent internals, but evaluates them through a separate harness.

## PE-MAS

PE-MAS is a multi-agent design studio for isolated flyback converter workflows. It separates `app/` and `core/`, uses explicit runtime configuration, includes PLECS integration, and gates release decisions behind evidence such as simulation, loop, thermal, EMI/safety, BOM source quality, and human signoff.

Design implication: this framework includes evidence-gate language in reporting standards and keeps agent integration modular so PE-MAS-like workflows can be benchmarked without merging their internal code into the evaluator.

## Repository Design Choices

| Choice | Reason |
| --- | --- |
| Research vault plus executable harness | Combines SRTP-style evidence discipline with benchmark reproducibility. |
| Standard-library Python starter code | Keeps the framework easy to run before simulator integrations are added. |
| JSON task and output schemas | Makes agent outputs machine-checkable. |
| Explicit violations in every report | Engineers need to see why a design failed, not only a score. |
| Research notes split by EE and CS | Mirrors the project scope: power electronics validity and AI-agent methodology. |

