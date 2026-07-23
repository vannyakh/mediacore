//! MediaCore benchmark: streaming
//!
//! Status: planned — scaffold for Criterion harness.
//! Categories and targets: see benchmarks/README.md

use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn bench_streaming(c: &mut Criterion) {
    c.bench_function("streaming_placeholder", |b| {
        b.iter(|| black_box(0u64).wrapping_add(1));
    });
}

criterion_group!(benches, bench_streaming);
criterion_main!(benches);
