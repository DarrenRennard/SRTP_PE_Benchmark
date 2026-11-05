# SRTP Research Plan

## Objective and scope

Improve selected agents in PE-MAS and evaluate whether the changes increase correctness and reliability. Begin with flyback converter workflows, then expand the evaluation harness to additional DC-DC tasks and, later, traction inverter tasks.

The current repository contains the imported PE-GPT 2.0 implementation. The changes and experiments below are planned; they do not describe completed benchmark capabilities.

## Establish the engineering foundation

Work through a 48 V DC to 12 V, 2 A flyback example. Explain the MOSFET ON and OFF current paths, magnetizing energy, winding polarity, CCM and DCM operation, component stress, and output ripple. Trace how the corresponding requirements and design evidence move through the agent workflow.

Deliver a worked example, annotated waveforms when available, and notes explaining assumptions and unresolved questions.

## Work package A Requirements agent

Primary implementation location: [requirements.py](../core/flyback_mas/nodes/requirements.py), with focused helpers and tests as needed.

1. Reproduce current behavior and identify failures in unit conversion, missing information, conflicting requirements, or follow-up updates.
2. Define each field's meaning, internal units, and expected treatment of unresolved values.
3. Implement deterministic normalization and validation where appropriate.
4. Preserve the distinction between user-supplied, derived, assumed, and unresolved values.
5. Generate targeted clarification questions for unresolved critical fields.
6. Apply follow-up updates while preserving unchanged confirmed fields.
7. Keep the output contract compatible with downstream agents.

Example: a request containing 2000 mA and 100 mV ripple should normalize to 2 A and 0.1 V peak-to-peak. Changing output current later should not silently alter the voltage or ripple requirements.

## Work package B Reporter agent

Primary implementation location: [reporter.py](../core/flyback_mas/nodes/reporter.py), with focused helpers and tests as needed.

1. Reproduce missing-value crashes, unsupported statements, incorrect numbers, and inconsistent verdicts.
2. Build a structured report payload with a source for each fact.
3. Distinguish targets, analytical estimates, simulated measurements, and unavailable information.
4. Render numerical tables and supplied validation statuses deterministically.
5. Check LLM-generated explanations against the report payload.
6. Apply consistency checks to all report-generation paths.
7. Surface conflicting evidence for review.

Example: if simulation failed and measured efficiency is absent, report that efficiency compliance is unknown. Do not substitute the target efficiency, a formula estimate, or a zero measurement.

## Before and after experiment

### Baseline

The imported baseline is commit `75177eb1736ea78c3eb3626af8fdf9d9310a629b`. Record Python and dependency versions, model/provider identifiers, prompts, generation settings, tool availability, and memory configuration alongside the evaluation outputs.

### Cases and expected outcomes

Propose 30 cases per agent, divided into 20 development cases and 10 held-out cases. Each case should have a unique ID, input or saved state, independently reviewed expected outcomes, and explicit scoring rules.

Requirements cases should cover complete requests, equivalent unit expressions, missing fields, conflicts, and follow-up changes. Reporter cases should cover valid results, failed simulation, unavailable measurements, analytical estimates, conflicting records, and incomplete component information.

Each partner reviews the other's labels. Define numerical tolerances, missing-value semantics, required fields, and the checks applicable to each case before scoring.

### Controlled comparison

Use the same cases, initial state, model settings, tool access, and budgets for the original and improved versions. Reset or freeze memory between independent cases. Repeat LLM-dependent held-out cases three times. Keep development and held-out cases separate.

Evaluate the agents independently before testing them together. Requirements receives fixed messages and starting specifications. Reporter receives identical saved states; it does not require a new PLECS run for every report test.

### Metrics

| Metric | Definition |
| --- | --- |
| Requirements field accuracy | Correct normalized values divided by evaluated field values. |
| Missing-field recall | Correctly identified missing required fields divided by all missing required fields. |
| Update preservation | Follow-up cases preserving every unchanged confirmed field divided by follow-up cases. |
| Unsupported assumption rate | Cases presenting an unconfirmed value as confirmed divided by evaluated cases. |
| Reporter numerical fidelity | Correct reported values divided by reported values checked. |
| Reporter status consistency | Reports consistent with the supplied validation status, or explicitly flagging conflicting records, divided by evaluated reports. |
| Unsupported claim rate | Reports containing at least one unsupported factual claim divided by evaluated reports. |
| Report generation success | Reports produced without errors divided by evaluated cases. |

Report numerator and denominator, not just percentages. Record omissions and required-section coverage separately so that deleting difficult content cannot inflate report accuracy. Track runtime, token use where available, and variation across repeats. For cases with no applicable checks, record not applicable rather than dividing by zero.

### Experiment record

Retain the baseline and improved commit IDs, case IDs, dataset version, settings, expected outputs, raw outputs, evaluator version, per-case scores, runtime, and remaining limitations. Summaries should link to their underlying records.

## Planned working sequence

| Stage | Requirements work | Reporter work | Shared outcome |
| --- | --- | --- | --- |
| Baseline and labels | Inspect extraction and update failures. | Inspect report and evidence failures. | Reviewed cases and original outputs. |
| First implementation | Normalize units and detect unresolved fields. | Handle missing values and preserve numerical facts. | Focused changes and regression checks. |
| Integration | Preserve follow-up specifications. | Enforce consistency across report paths. | Reviewed pull requests. |
| Evaluation | Run fixed held-out cases and repeats. | Run fixed held-out states and repeats. | Before-and-after tables and failure analysis. |

This sequence is a working plan; dates and ownership can be recorded in Issues as tasks are assigned.

## Demonstrating the contribution

Present a comparison table with measured results, then show three side-by-side examples: a corrected Requirements failure, a corrected Reporter failure, and a remaining limitation. Include the input, expected behavior, original output, improved output, and the code change responsible.

After these checks pass, run an end-to-end regression on the flyback workflow and record any downstream changes.

## Later extensions

Expand the DC-DC benchmark only after the initial evaluator and reference cases are reviewed. Investigate traction inverter tasks as a later track, with independently defined engineering checks and appropriate simulation evidence.

Return to the [project overview](../README.md) or the [original PE-GPT 2.0 documentation](../README_PE_GPT_2_0.md).
