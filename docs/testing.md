# MediaCore Testing

Testing is a first-class feature. Layers live under `tests/`; shared fakes and contracts live in `packages/testkit/`.

## Layout

```text
packages/testkit/     fake_provider, fake_storage, fake_queue, fake_http, contracts
tests/
  unit/               isolated components
  integration/        multi-component flows
  api/                REST /v1
  providers/          provider units + contracts
  plugins/            plugin certification
  storage/            storage backend contracts
  e2e/                full user workflows
  performance/        latency smoke
  benchmark/          pytest-benchmark
  stress/ load/ chaos/ security/ regression/
  fixtures/ snapshots/ data/
```

## Run locally

```bash
uv sync --extra dev

# PR-critical suite (default CI)
uv run pytest -m "not load and not stress and not chaos and not benchmark"

# All tests including heavy markers
uv run pytest

# Coverage
uv run pytest --cov=packages --cov=providers --cov=apps --cov-report=term-missing

# Benchmarks
uv run pytest -m benchmark --benchmark-only

# Load (requires API running)
uv run locust -f tests/load/locustfile.py --headless -u 10 -r 2 -t 30s --host http://127.0.0.1:8000
```

## Markers

| Marker | PR CI | Nightly |
|--------|-------|---------|
| unit, integration, api, provider, plugin, storage | yes | yes |
| e2e, performance, security, regression | yes | yes |
| benchmark, stress, chaos | no | yes |
| load | no | optional |

## Contracts

Every provider, plugin, and storage backend should pass the shared runners in `packages/testkit/contracts.py`. Contributors can validate plugins locally before submitting PRs.

## Regression policy

Every bug fix must add a permanent test under `tests/regression/`. The suite exists so the same failure never returns silently.

## Targets

| Category | Current gate | Mature target |
|----------|--------------|---------------|
| Overall coverage | ≥40% (ratchet up) | ≥95% core |
| Provider/plugin contracts | Built-ins | 100% ecosystem |
| Perf regression | Smoke latency | ≤5% vs main |
| Memory leaks | — | Zero known |

## Rust engine (future)

When `crates/mediacore-engine` lands, add Criterion benches (`cargo bench`) and document flamegraph/profiler workflows alongside the Python suite.
