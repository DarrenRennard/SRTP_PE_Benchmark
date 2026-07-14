"""Deterministic baseline agent for the starter benchmark."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any


def solve(task: dict[str, Any]) -> dict[str, Any]:
    base_mva = float(task["base_mva"])
    bus_by_id = {bus["id"]: bus for bus in task["buses"]}

    voltages: dict[str, float] = {}
    flows: dict[str, float] = {}

    for bus in task["buses"]:
        if bus.get("type") == "slack":
            voltages[bus["id"]] = float(bus.get("voltage_pu", 1.0))

    for line in task["lines"]:
        from_bus = line["from"]
        to_bus = line["to"]
        load_bus = bus_by_id[to_bus]
        p_mw = float(load_bus.get("p_load_mw", 0.0))
        q_mvar = float(load_bus.get("q_load_mvar", 0.0))
        p_pu = p_mw / base_mva
        q_pu = q_mvar / base_mva
        drop = float(line["r_pu"]) * p_pu + float(line["x_pu"]) * q_pu
        voltages[to_bus] = round(voltages[from_bus] - drop, 6)
        flows[f"{from_bus}->{to_bus}"] = round(math.sqrt(p_mw * p_mw + q_mvar * q_mvar), 6)

    return {
        "agent": {
            "name": "deterministic-example-agent",
            "version": "0.1.0",
            "model": "none",
            "notes": "Computes the same approximate radial checks as the starter benchmark.",
        },
        "solution": {
            "bus_voltages_pu": voltages,
            "line_flows_mva": flows,
            "served_load_mw": round(sum(float(bus.get("p_load_mw", 0.0)) for bus in task["buses"]), 6),
            "explanation": (
                "The load bus voltage is estimated with a first-order radial voltage drop "
                "and the line flow is the apparent power of the downstream load."
            ),
        },
    }


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 2:
        print("Usage: python agents/example_agent.py TASK_JSON OUTPUT_JSON", file=sys.stderr)
        return 2

    task_path = Path(args[0])
    output_path = Path(args[1])
    with task_path.open("r", encoding="utf-8") as handle:
        task = json.load(handle)
    output = solve(task)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(output, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

