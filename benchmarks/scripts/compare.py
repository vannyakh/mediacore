#!/usr/bin/env python3
"""Compare two MediaCore benchmark summary JSON files."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from packages.mediacore_benchmark.compare import (  # noqa: E402
    compare_summaries,
    detect_regressions,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--current", type=Path, required=True)
    parser.add_argument("--threshold", type=float, default=0.15)
    args = parser.parse_args()

    baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
    current = json.loads(args.current.read_text(encoding="utf-8"))
    rows = compare_summaries(baseline, current)
    regressions = detect_regressions(rows, threshold=args.threshold)

    for row in rows:
        ratio = row["delta_ratio"]
        pct = "n/a" if ratio is None else f"{ratio * 100:+.1f}%"
        print(f"{row['name']}: {pct} ({row['status']})")

    if regressions:
        print(f"\n{len(regressions)} regression(s) over {args.threshold:.0%}:", file=sys.stderr)
        for r in regressions:
            print(f"  - {r['name']}: {r['delta_ratio'] * 100:+.1f}%", file=sys.stderr)
        return 1
    print("\nNo regressions detected.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
