"""Export benchmark summaries to JSON / Markdown."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def export_json(summary: dict[str, Any], path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    return path


def export_markdown(summary: dict[str, Any], path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# MediaCore Benchmark Report",
        "",
        f"- Generated: {summary.get('generated_at', '')}",
        f"- Suite: {summary.get('suite', 'python-smoke')}",
        "",
        "| Benchmark | Mean (ms) | P95 (ms) | Ops/s |",
        "|-----------|----------:|---------:|------:|",
    ]
    for b in summary.get("benchmarks", []):
        mean_ms = float(b.get("mean_s", 0.0)) * 1000
        p95_ms = float(b.get("p95_s", 0.0)) * 1000
        ops = float(b.get("ops_per_sec", 0.0))
        lines.append(f"| {b.get('name')} | {mean_ms:.3f} | {p95_ms:.3f} | {ops:.1f} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def new_summary(*, suite: str, benchmarks: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "suite": suite,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "benchmarks": benchmarks,
    }
