"""MediaCore benchmark toolkit — run, compare, and export performance reports."""

from packages.mediacore_benchmark.compare import compare_summaries, detect_regressions
from packages.mediacore_benchmark.metrics import LatencyStats, summarize_latencies
from packages.mediacore_benchmark.reporter import export_json, export_markdown

__all__ = [
    "LatencyStats",
    "compare_summaries",
    "detect_regressions",
    "export_json",
    "export_markdown",
    "summarize_latencies",
]
