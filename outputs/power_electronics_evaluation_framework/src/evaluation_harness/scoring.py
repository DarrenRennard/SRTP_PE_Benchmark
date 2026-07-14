"""Scoring helpers."""

from __future__ import annotations

from .models import ScoreComponent


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def weighted_score(components: list[ScoreComponent]) -> float:
    total_weight = sum(component.weight for component in components)
    if total_weight <= 0:
        return 0.0
    total = sum(clamp01(component.score) * component.weight for component in components)
    return round(total / total_weight, 6)

