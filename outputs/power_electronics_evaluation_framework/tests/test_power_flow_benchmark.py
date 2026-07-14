from __future__ import annotations

import json
import unittest
from pathlib import Path

from benchmarks.power_flow_benchmark.evaluator import evaluate


ROOT = Path(__file__).resolve().parents[1]


class PowerFlowBenchmarkTests(unittest.TestCase):
    def test_sample_output_passes(self) -> None:
        task = _load(ROOT / "benchmarks/power_flow_benchmark/tasks/example_radial_bus.json")
        output = _load(ROOT / "benchmarks/power_flow_benchmark/sample_outputs/example_agent_output.json")

        report = evaluate(task, output)

        self.assertTrue(report.passed)
        self.assertGreaterEqual(report.score, 0.99)
        self.assertEqual([], [v for v in report.violations if v.severity == "error"])

    def test_bad_voltage_fails(self) -> None:
        task = _load(ROOT / "benchmarks/power_flow_benchmark/tasks/example_radial_bus.json")
        output = _load(ROOT / "benchmarks/power_flow_benchmark/sample_outputs/example_agent_output.json")
        output["solution"]["bus_voltages_pu"]["load_1"] = 0.90

        report = evaluate(task, output)

        self.assertFalse(report.passed)
        self.assertTrue(any(v.code == "voltage_limit" for v in report.violations))


def _load(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


if __name__ == "__main__":
    unittest.main()

