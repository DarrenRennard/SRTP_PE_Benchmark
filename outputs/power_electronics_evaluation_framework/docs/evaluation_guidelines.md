# Evaluation Guidelines

## Evaluation Principles

Power electronics design agents should be evaluated by executable checks whenever possible. Textual reasoning can explain a design, but the benchmark should verify the design against physical laws, simulation results, schema requirements, and engineering constraints.

The evaluator should answer four questions:

1. Did the agent return a machine-readable output?
2. Can the output be executed or checked by deterministic tools?
3. Does the design satisfy the task specification and engineering constraints?
4. Does the agent's explanation match the verified result?

## Metric Categories

### Design Correctness

Measures whether the design meets required electrical behavior.

Examples:

- Output voltage within tolerance.
- Power delivery above minimum required load.
- Converter topology matches task constraints.
- Waveforms show expected operating mode.

### Performance Optimization

Measures distance from a target or best-known design.

Examples:

- Efficiency gap from baseline or optimum.
- Magnetics size or mass relative to target.
- Cost deviation from selected bill of materials.
- Switching loss or conduction loss gap.

### Constraint Satisfaction

Measures adherence to physical, safety, and operational limits.

Examples:

- Voltage, current, temperature, ripple, and line-loading limits.
- Component derating.
- Isolation and creepage placeholders for later safety review.
- Simulation convergence and stable operating point.

### Robustness

Measures behavior across operating corners.

Examples:

- Line and load sweeps.
- Component tolerance sweeps.
- Temperature corners.
- Startup, transient, and fault conditions.

### Efficiency

Measures computational cost.

Examples:

- Wall-clock evaluation time.
- Number of model calls.
- Simulation runtime.
- Failed or repeated tool calls.

### Explainability and Interpretability

Measures whether the agent's reasoning is useful to an engineer.

Examples:

- Design rationale identifies tradeoffs.
- Assumptions are explicit.
- Explanation cites calculated or simulated evidence.
- Claimed margins match evaluator output.

### Consistency

Measures reproducibility.

Examples:

- Same task produces equivalent design over repeated runs.
- Similar tasks produce monotonic or physically reasonable changes.
- Random seeds and model settings are reported.

### Tool Utilization

Measures correct use of external tools.

Examples:

- PLECS or MATLAB files compile.
- SPICE netlists run without hidden manual fixes.
- Parsed simulation outputs match expected units.
- Tool errors are surfaced rather than ignored.

## Evaluation Workflow

1. Define the task: write a task file with specification, constraints, input data, expected output schema, and scoring weights.
2. Run the agent: capture the exact prompt, model, settings, tool calls, and output artifact.
3. Validate format: reject missing fields, invalid units, or non-machine-readable outputs.
4. Execute checks: run deterministic Python checks and, when available, PLECS, MATLAB, or SPICE simulations.
5. Score results: compute normalized score plus explicit violations.
6. Red-team results: record failure modes, suspicious passes, and evidence gaps.
7. Report: save the task, agent output, evaluator report, logs, and conclusions in `results/`.

## Reporting Standards

Every evaluation report should include:

- Task ID and benchmark version.
- Agent name, version, model, and configuration.
- Date, machine context, and simulator versions.
- Raw agent output.
- Deterministic score and violations.
- Simulation logs or links to artifacts.
- Human review notes when required.
- Claim status update if the evaluation supports or weakens a research note.

## Evidence Gates

Borrowing from PE-MAS, designs should not be marked release-ready unless relevant evidence gates are closed:

- Functional simulation evidence.
- Line and load corner evidence.
- Thermal evidence.
- EMI and safety review evidence.
- Component source-quality evidence.
- Human signoff for safety-critical claims.

For this framework, a benchmark can pass while still being tagged "research-only" if some gates remain out of scope.

## Placeholder for Domain Expansion

[TODO: Add PLECS-backed flyback converter benchmark rules.]

[TODO: Add MATLAB/Simulink traction inverter benchmark rules.]

[TODO: Add waveform parsing conventions for converter startup and steady-state analysis.]

