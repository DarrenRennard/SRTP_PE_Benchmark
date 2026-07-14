"""Command line interface for benchmark evaluation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from benchmarks.power_flow_benchmark.evaluator import evaluate
from evaluation_harness.io import read_json, write_json


def run_power_flow(args: argparse.Namespace) -> int:
    task = read_json(args.task)
    output = read_json(args.output)
    report = evaluate(task, output)
    payload = report.to_dict()

    if args.report:
        write_json(args.report, payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0 if report.passed else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Power electronics agent evaluation harness")
    subparsers = parser.add_subparsers(dest="command", required=True)

    power_flow = subparsers.add_parser("run-power-flow", help="Run the starter power flow benchmark")
    power_flow.add_argument("task", type=Path, help="Path to task JSON")
    power_flow.add_argument("output", type=Path, help="Path to agent output JSON")
    power_flow.add_argument("--report", type=Path, help="Optional path for report JSON")
    power_flow.set_defaults(func=run_power_flow)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

