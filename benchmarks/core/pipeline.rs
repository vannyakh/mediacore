//! MediaCore benchmark: pipeline
//!
//! Status: planned — scaffold for Criterion harness.
//! Categories and targets: see benchmarks/README.md

use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn bench_pipeline(c: &mut Criterion) {
    c.bench_function("pipeline_placeholder", |b| {
        b.iter(|| black_box(0u64).wrapping_add(1));
    });
}

criterion_group!(benches, bench_pipeline);
criterion_main!(benches);
