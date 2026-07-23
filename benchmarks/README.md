# MediaCore Benchmarks

Standalone performance suite — modeled after Rust / Tokio / TiKV / Arrow style layouts.  
Measures **latency, memory, scalability, and regressions**, not only raw speed.

```text
benchmarks/
├── common/          fixtures, generators, metrics, profiler, reporter
├── core/            URL, metadata, manifest, cache, queue, pipeline, …
├── network/         HTTP, DNS, TLS, streaming, retry
├── storage/         filesystem, sqlite, postgres, redis, s3, …
├── media/           thumbnail, audio, ffmpeg, transcoding, …
├── providers/       provider API / parser / formats
├── plugins/         load / execute / lifecycle
├── sdk/             rust, javascript, python, go, dart
├── desktop/         startup, ipc, rendering, workflow
├── api/             analyze, download, websocket, grpc
├── worker/          jobs, queue, concurrency
├── stress/          cpu, memory, disk, network, workers
├── python/          Python smoke benches (current runtime)
├── reports/         dated HTML/JSON/Markdown outputs
└── scripts/         run / compare helpers
```

Companion toolkit: [`packages/mediacore_benchmark`](../packages/mediacore_benchmark/) (compare, export, regression detect).

---

## Quick start

```bash
# Python smoke (works today — no Rust toolchain required)
uv run python -m packages.mediacore_benchmark.runner
# or
uv run python benchmarks/scripts/run_smoke.py

# pytest-benchmark (CI nightly)
uv run pytest -m benchmark --benchmark-only --benchmark-json=benchmark.json

# Rust Criterion (requires cargo)
cargo bench -p mediacore-benchmarks
cargo bench -p mediacore-benchmarks --bench url_parser
```

Reports land in `benchmarks/reports/YYYY-MM-DD/` and Criterion HTML under `target/criterion/`.

---

## Categories

| Area | Examples |
|------|----------|
| **Core engine** | URL / manifest / metadata parse, JSON, pipeline, scheduler, events, queue, cache, plugin loader |
| **Runtime** | Worker startup, scheduling, concurrency, cancel / retry / resume / shutdown |
| **HTTP** | DNS, TLS, GET/POST, streaming, redirect, chunked, compression, HTTP/2–3 |
| **Storage** | sequential/random R/W, cache hit/miss, large/small files, parallel I/O |
| **Media** | thumbnail, audio, merge, subtitles, frames, watermark, convert, transcode |
| **Pipeline** | analyze → download → convert → subtitle → translate → thumbnail → export |
| **Queue** | push/pop, priority, delayed, scheduled, millions of jobs |
| **Plugin** | load/unload, init, execute, shutdown, communication |
| **API** | analyze/download/jobs, auth, rate limit, WebSocket, gRPC |
| **Stress** | 10–1000 workers, 10k jobs, 1M events, large metadata/manifest/cache |

---

## Metrics

Every bench should collect where applicable:

```text
Execution time · Latency · Avg · Median · P95 · P99 · P999
Memory / peak memory · CPU % · Disk R/W · Network throughput
Allocations · Binary size · Startup time
```

Memory: heap, stack, peak, fragmentation, leaks, allocation count.  
CPU: single/multi-thread, parallel runtime, scheduler, SIMD, hashing, compression.  
Network sizes: 1 MB → 10 GB, streaming, chunked, resume, parallel download.

---

## Profiling (Rust)

```bash
cargo bench -p mediacore-benchmarks
cargo flamegraph -p mediacore-benchmarks --bench url_parser
cargo llvm-lines -p mediacore-engine
cargo bloat -p mediacore-engine
```

Outputs: flame graph, call graph, CPU / memory / allocation profiles.

---

## Reports

```text
reports/2026-07-23/
  summary.json
  summary.md
  core.html          # from Criterion when enabled
  comparison.html
```

```bash
uv run python benchmarks/scripts/compare.py \
  --baseline benchmarks/reports/baseline/summary.json \
  --current benchmarks/reports/$(date +%F)/summary.json
```

---

## CI/CD

```text
PR → Build → Unit → Integration → Benchmark smoke → Regression check → Upload → Pages
```

- **PR:** Python smoke optional / lightweight  
- **Nightly:** full `pytest -m benchmark` + Criterion when Rust toolchain present  
- Artifacts: `benchmark.json`, `benchmarks/reports/**`

---

## Performance targets (v1.0)

| Component | Target |
|-----------|--------|
| CLI startup | < 50 ms |
| API startup | < 300 ms |
| URL parse | < 1 ms |
| Metadata parse | < 10 ms |
| JSON serialize | < 2 ms |
| Plugin load | < 20 ms |
| Worker startup | < 100 ms |
| Queue push / pop | > 200,000 ops/sec |
| Event dispatch | > 1,000,000 events/sec |
| Cache lookup | < 0.5 ms |
| HTTP client overhead | < 5 ms (excl. network) |

---

## Status

| Track | Status |
|-------|--------|
| Layout + common helpers | done |
| Criterion core microbenches | partial (`url_parser`, `metadata`, `manifest`, `cache`, `queue`, `events`) |
| Category stubs | scaffolded (placeholder Criterion harness) |
| Python smoke runner + compare | done |
| Full media/network/storage benches | planned |
| GitHub Pages history dashboard | planned |
