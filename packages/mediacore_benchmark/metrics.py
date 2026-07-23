"""Latency / throughput aggregation for MediaCore benchmarks."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from statistics import mean, median
from typing import Any


def _percentile(sorted_vals: list[float], p: float) -> float:
    if not sorted_vals:
        return 0.0
    if len(sorted_vals) == 1:
        return sorted_vals[0]
    idx = round(max(0.0, min(1.0, p)) * (len(sorted_vals) - 1))
    return sorted_vals[min(idx, len(sorted_vals) - 1)]


@dataclass(slots=True)
class LatencyStats:
    count: int
    mean_s: float
    median_s: float
    p95_s: float
    p99_s: float
    p999_s: float
    min_s: float
    max_s: float
    ops_per_sec: float

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def summarize_latencies(samples_s: list[float]) -> LatencyStats:
    ordered = sorted(samples_s)
    n = len(ordered)
    avg = mean(ordered) if n else 0.0
    ops = (1.0 / avg) if avg > 0 else 0.0
    return LatencyStats(
        count=n,
        mean_s=avg,
        median_s=median(ordered) if n else 0.0,
        p95_s=_percentile(ordered, 0.95),
        p99_s=_percentile(ordered, 0.99),
        p999_s=_percentile(ordered, 0.999),
        min_s=ordered[0] if n else 0.0,
        max_s=ordered[-1] if n else 0.0,
        ops_per_sec=ops,
    )
