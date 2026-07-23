"""Python smoke runner for MediaCore core micro-benchmarks."""

from __future__ import annotations

import time
from pathlib import Path
from typing import Callable
from unittest.mock import patch

from packages.core.models import FormatInfo, MediaMetadata
from packages.core.parser import hostname, is_direct_media_url
from packages.core.validator import validate_url
from packages.engine.engine import MediaCoreEngine
from packages.mediacore_benchmark.metrics import summarize_latencies
from packages.mediacore_benchmark.reporter import export_json, export_markdown, new_summary


def _time_calls(fn: Callable[[], None], n: int) -> list[float]:
    samples: list[float] = []
    for _ in range(n):
        start = time.perf_counter()
        fn()
        samples.append(time.perf_counter() - start)
    return samples


def run_python_smoke(*, iterations: int = 200) -> dict:
    url = "https://cdn.example.com/demo.mp4"
    meta = MediaMetadata(
        platform="generic",
        url=url,
        title="demo.mp4",
        formats=[FormatInfo(id="original", quality="original", container="mp4")],
        manifest={"type": "basic", "provider": "generic"},
    )
    engine = MediaCoreEngine()
    provider = type(
        "P",
        (),
        {
            "metadata": lambda self, u: meta,
            "formats": lambda self, u: meta.formats,
            "manifest": lambda self, u: meta.manifest,
            "get_metadata": lambda self, u: meta,
            "list_formats": lambda self, u: meta.formats,
        },
    )()

    benches: list[dict] = []

    def add(name: str, fn: Callable[[], None]) -> None:
        stats = summarize_latencies(_time_calls(fn, iterations))
        row = {"name": name, "category": "core", **stats.to_dict()}
        benches.append(row)

    add("python/url_validate", lambda: validate_url(url))
    add("python/hostname", lambda: hostname(url))
    add("python/is_direct_media", lambda: is_direct_media_url(url))
    add("python/metadata_to_dict", meta.to_dict)

    with patch.object(engine.registry, "resolve", return_value=provider):
        add("python/analyze", lambda: engine.analyze(url))

    return new_summary(suite="python-smoke", benchmarks=benches)


def main() -> None:
    summary = run_python_smoke()
    out_dir = Path("benchmarks/reports") / time.strftime("%Y-%m-%d")
    export_json(summary, out_dir / "summary.json")
    export_markdown(summary, out_dir / "summary.md")
    print(f"wrote {out_dir / 'summary.json'}")
    for b in summary["benchmarks"]:
        print(
            f"  {b['name']}: {b['mean_s']*1000:.3f} ms mean, "
            f"{b['ops_per_sec']:.0f} ops/s"
        )


if __name__ == "__main__":
    main()
