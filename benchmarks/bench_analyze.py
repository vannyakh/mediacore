"""Simple analyze latency micro-benchmark (mocked provider path)."""

from __future__ import annotations

import time
from unittest.mock import patch

from packages.core.models import FormatInfo, MediaMetadata
from packages.engine.engine import MediaCoreEngine


def main() -> None:
    engine = MediaCoreEngine()
    meta = MediaMetadata(
        platform="generic",
        url="https://cdn.example.com/demo.mp4",
        title="demo.mp4",
        formats=[FormatInfo(id="original", quality="original", container="mp4")],
    )
    n = 200
    start = time.perf_counter()
    with patch.object(engine.registry, "resolve") as resolve:
        provider = type(
            "P",
            (),
            {
                "get_metadata": lambda self, url: meta,
                "list_formats": lambda self, url: meta.formats,
            },
        )()
        resolve.return_value = provider
        for _ in range(n):
            engine.analyze("https://cdn.example.com/demo.mp4")
    elapsed = time.perf_counter() - start
    print(f"analyze x{n}: {elapsed:.3f}s ({n / elapsed:.1f} ops/s)")


if __name__ == "__main__":
    main()
