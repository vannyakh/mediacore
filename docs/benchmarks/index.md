# Benchmarks

MediaCore ships a **standalone benchmark module** (similar to Rust, Tokio, TiKV, Arrow) that measures latency, memory, scalability, and regressions over time.

Full layout and targets: [`benchmarks/README.md`](https://github.com/mediacore/mediacore/blob/main/benchmarks/README.md).

## Run

```bash
# Python smoke (current runtime)
uv run python -m packages.mediacore_benchmark.runner

# pytest-benchmark
uv run pytest -m benchmark --benchmark-only

# Rust Criterion
cargo bench -p mediacore-benchmarks
```

## Toolkit

`packages/mediacore_benchmark` provides:

- Run smoke suites and write dated reports under `benchmarks/reports/`
- Compare runs and detect regressions (`benchmarks/scripts/compare.py`)
- Export JSON and Markdown summaries

## CI

| Gate | Suite |
|------|--------|
| PR | Optional Python smoke |
| Nightly | pytest-benchmark + smoke reports (+ Criterion when Rust available) |

## v1.0 targets (highlights)

| Component | Target |
|-----------|--------|
| URL parse | < 1 ms |
| Metadata parse | < 10 ms |
| Queue push/pop | > 200k ops/s |
| Event dispatch | > 1M events/s |
| Cache lookup | < 0.5 ms |
