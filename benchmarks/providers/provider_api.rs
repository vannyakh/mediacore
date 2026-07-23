//! MediaCore benchmark: provider_api
//!
//! Status: planned — scaffold for Criterion harness.
//! Categories and targets: see benchmarks/README.md

use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn bench_provider_api(c: &mut Criterion) {
    c.bench_function("provider_api_placeholder", |b| {
        b.iter(|| black_box(0u64).wrapping_add(1));
    });
}

criterion_group!(benches, bench_provider_api);
criterion_main!(benches);
