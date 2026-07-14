"""Shared data models for benchmark reports."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(frozen=True)
class Violation:
    """A benchmark rule violation."""

    code: str
    message: str
    severity: str = "error"
    details: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ScoreComponent:
    """One normalized score component."""

    name: str
    score: float
    weight: float
    notes: str = ""


@dataclass(frozen=True)
class EvaluationReport:
    """Serializable benchmark report."""

    task_id: str
    benchmark: str
    score: float
    passed: bool
    components: list[ScoreComponent]
    violations: list[Violation]
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

