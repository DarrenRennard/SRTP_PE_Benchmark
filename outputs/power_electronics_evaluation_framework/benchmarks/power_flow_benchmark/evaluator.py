"""Deterministic evaluator for the starter radial power-flow benchmark."""

from __future__ import annotations

import math
from typing import Any

from evaluation_harness.models import EvaluationReport, ScoreComponent, Violation
from evaluation_harness.scoring import clamp01, weighted_score


DEFAULT_WEIGHTS = {
    "format": 0.20,
    "voltage": 0.30,
    "line_flow": 0.20,
    "served_load": 0.20,
    "explanation": 0.10,
}


def evaluate(task: dict[str, Any], agent_output: dict[str, Any]) -> EvaluationReport:
    task_id = str(task.get("task_id", "unknown-task"))
    weights = {**DEFAULT_WEIGHTS, **task.get("scoring", {})}
    violations: list[Violation] = []

    solution = agent_output.get("solution")
    if not isinstance(solution, dict):
        violations.append(Violation("missing_solution", "Agent output must contain a solution object."))
        return _report(task_id, weights, [ScoreComponent("format", 0.0, weights["format"])], violations)

    voltages = solution.get("bus_voltages_pu")
    flows = solution.get("line_flows_mva")
    served_load = solution.get("served_load_mw")
    explanation = solution.get("explanation", "")

    format_score = _validate_format(voltages, flows, served_load, violations)
    components = [ScoreComponent("format", format_score, weights["format"])]

    if format_score < 1.0:
        components.extend(
            [
                ScoreComponent("voltage", 0.0, weights["voltage"], "Skipped because format is invalid."),
                ScoreComponent("line_flow", 0.0, weights["line_flow"], "Skipped because format is invalid."),
                ScoreComponent("served_load", 0.0, weights["served_load"], "Skipped because format is invalid."),
                ScoreComponent("explanation", 1.0 if explanation else 0.0, weights["explanation"]),
            ]
        )
        return _report(task_id, weights, components, violations)

    assert isinstance(voltages, dict)
    assert isinstance(flows, dict)
    assert isinstance(served_load, (int, float))

    components.append(ScoreComponent("voltage", _score_voltage(task, voltages, violations), weights["voltage"]))
    components.append(ScoreComponent("line_flow", _score_line_flow(task, flows, violations), weights["line_flow"]))
    components.append(ScoreComponent("served_load", _score_served_load(task, float(served_load), violations), weights["served_load"]))
    components.append(ScoreComponent("explanation", 1.0 if isinstance(explanation, str) and explanation.strip() else 0.0, weights["explanation"]))

    if not explanation:
        violations.append(Violation("missing_explanation", "Solution should include an engineering explanation.", "warning"))

    return _report(task_id, weights, components, violations)


def _validate_format(
    voltages: Any,
    flows: Any,
    served_load: Any,
    violations: list[Violation],
) -> float:
    checks = 0
    passed = 0

    checks += 1
    if isinstance(voltages, dict) and all(isinstance(v, (int, float)) for v in voltages.values()):
        passed += 1
    else:
        violations.append(Violation("invalid_voltages", "solution.bus_voltages_pu must be an object of numeric values."))

    checks += 1
    if isinstance(flows, dict) and all(isinstance(v, (int, float)) for v in flows.values()):
        passed += 1
    else:
        violations.append(Violation("invalid_line_flows", "solution.line_flows_mva must be an object of numeric values."))

    checks += 1
    if isinstance(served_load, (int, float)):
        passed += 1
    else:
        violations.append(Violation("invalid_served_load", "solution.served_load_mw must be numeric."))

    return passed / checks


def _score_voltage(task: dict[str, Any], voltages: dict[str, float], violations: list[Violation]) -> float:
    buses = task.get("buses", [])
    bus_by_id = {bus["id"]: bus for bus in buses}
    tolerance = float(task.get("tolerances", {}).get("voltage_pu", 0.005))
    line_scores: list[float] = []

    for bus_id, bus in bus_by_id.items():
        if bus_id not in voltages:
            violations.append(Violation("missing_bus_voltage", f"Missing voltage for bus {bus_id}."))
            line_scores.append(0.0)
            continue
        voltage = float(voltages[bus_id])
        v_min = float(bus.get("v_min_pu", 0.0))
        v_max = float(bus.get("v_max_pu", 2.0))
        if not (v_min <= voltage <= v_max):
            violations.append(
                Violation(
                    "voltage_limit",
                    f"Voltage for bus {bus_id} is outside limits.",
                    details={"bus": bus_id, "value": voltage, "min": v_min, "max": v_max},
                )
            )
            line_scores.append(0.0)
        else:
            line_scores.append(1.0)

    for line in task.get("lines", []):
        from_bus = line["from"]
        to_bus = line["to"]
        if from_bus not in voltages or to_bus not in voltages:
            continue
        expected = _expected_to_voltage(task, line)
        actual = float(voltages[to_bus])
        error = abs(actual - expected)
        if error > tolerance:
            violations.append(
                Violation(
                    "voltage_mismatch",
                    f"Voltage for bus {to_bus} differs from approximate radial calculation.",
                    details={"bus": to_bus, "actual": actual, "expected": round(expected, 6), "tolerance": tolerance},
                )
            )
        line_scores.append(clamp01(1.0 - error / max(tolerance, 1e-9)))

    return sum(line_scores) / len(line_scores) if line_scores else 0.0


def _score_line_flow(task: dict[str, Any], flows: dict[str, float], violations: list[Violation]) -> float:
    tolerance = float(task.get("tolerances", {}).get("line_flow_mva", 0.02))
    scores: list[float] = []
    for line in task.get("lines", []):
        key = f"{line['from']}->{line['to']}"
        if key not in flows:
            violations.append(Violation("missing_line_flow", f"Missing line flow for {key}."))
            scores.append(0.0)
            continue
        expected = _expected_line_flow(task, line)
        actual = abs(float(flows[key]))
        limit = float(line["limit_mva"])
        if actual > limit:
            violations.append(
                Violation(
                    "line_overload",
                    f"Line {key} exceeds its MVA limit.",
                    details={"line": key, "actual": actual, "limit": limit},
                )
            )
        error = abs(actual - expected)
        if error > tolerance:
            violations.append(
                Violation(
                    "line_flow_mismatch",
                    f"Line flow for {key} differs from expected apparent power.",
                    details={"line": key, "actual": actual, "expected": round(expected, 6), "tolerance": tolerance},
                )
            )
        consistency = clamp01(1.0 - error / max(tolerance, 1e-9))
        limit_score = 1.0 if actual <= limit else 0.0
        scores.append(0.7 * consistency + 0.3 * limit_score)
    return sum(scores) / len(scores) if scores else 0.0


def _score_served_load(task: dict[str, Any], served_load_mw: float, violations: list[Violation]) -> float:
    required = sum(float(bus.get("p_load_mw", 0.0)) for bus in task.get("buses", []))
    tolerance = float(task.get("tolerances", {}).get("served_load_mw", 0.001))
    if required <= 0:
        return 1.0
    shortfall = max(0.0, required - served_load_mw)
    if shortfall > tolerance:
        violations.append(
            Violation(
                "load_not_served",
                "Served load is below required load.",
                details={"served_load_mw": served_load_mw, "required_load_mw": required},
            )
        )
    return clamp01(1.0 - shortfall / required)


def _expected_to_voltage(task: dict[str, Any], line: dict[str, Any]) -> float:
    from_voltage = _bus_voltage_setpoint(task, line["from"])
    downstream = _bus(task, line["to"])
    base_mva = float(task["base_mva"])
    p_pu = float(downstream.get("p_load_mw", 0.0)) / base_mva
    q_pu = float(downstream.get("q_load_mvar", 0.0)) / base_mva
    drop = float(line["r_pu"]) * p_pu + float(line["x_pu"]) * q_pu
    return from_voltage - drop


def _expected_line_flow(task: dict[str, Any], line: dict[str, Any]) -> float:
    downstream = _bus(task, line["to"])
    p = float(downstream.get("p_load_mw", 0.0))
    q = float(downstream.get("q_load_mvar", 0.0))
    return math.sqrt(p * p + q * q)


def _bus(task: dict[str, Any], bus_id: str) -> dict[str, Any]:
    for bus in task.get("buses", []):
        if bus.get("id") == bus_id:
            return bus
    raise KeyError(bus_id)


def _bus_voltage_setpoint(task: dict[str, Any], bus_id: str) -> float:
    bus = _bus(task, bus_id)
    return float(bus.get("voltage_pu", 1.0))


def _report(
    task_id: str,
    weights: dict[str, float],
    components: list[ScoreComponent],
    violations: list[Violation],
) -> EvaluationReport:
    score = weighted_score(components)
    hard_errors = [v for v in violations if v.severity == "error"]
    return EvaluationReport(
        task_id=task_id,
        benchmark="power_flow_benchmark",
        score=score,
        passed=score >= 0.8 and not hard_errors,
        components=components,
        violations=violations,
        metadata={"weights": weights},
    )

