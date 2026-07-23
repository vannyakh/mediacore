"""Compare benchmark summaries and flag regressions."""

from __future__ import annotations

from typing import Any


def compare_summaries(
    baseline: dict[str, Any],
    current: dict[str, Any],
    *,
    metric: str = "mean_s",
) -> list[dict[str, Any]]:
    """Return per-bench deltas. Positive `delta_ratio` means slower."""
    base_benches = {b["name"]: b for b in baseline.get("benchmarks", [])}
    rows: list[dict[str, Any]] = []
    for item in current.get("benchmarks", []):
        name = item["name"]
        cur = float(item.get(metric) or item.get("stats", {}).get(metric) or 0.0)
        prev_item = base_benches.get(name)
        if prev_item is None:
            rows.append(
                {
                    "name": name,
                    "baseline": None,
                    "current": cur,
                    "delta_ratio": None,
                    "status": "new",
                }
            )
            continue
        prev = float(prev_item.get(metric) or prev_item.get("stats", {}).get(metric) or 0.0)
        ratio = None if prev <= 0 else (cur - prev) / prev
        rows.append(
            {
                "name": name,
                "baseline": prev,
                "current": cur,
                "delta_ratio": ratio,
                "status": "compared",
            }
        )
    return rows


def detect_regressions(
    comparisons: list[dict[str, Any]],
    *,
    threshold: float = 0.15,
) -> list[dict[str, Any]]:
    """Flag benches slower than `threshold` (default +15%)."""
    bad: list[dict[str, Any]] = []
    for row in comparisons:
        ratio = row.get("delta_ratio")
        if ratio is not None and ratio > threshold:
            bad.append({**row, "status": "regression"})
    return bad
