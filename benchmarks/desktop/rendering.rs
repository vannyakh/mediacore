//! MediaCore benchmark: rendering
//!
//! Status: planned — scaffold for Criterion harness.
//! Categories and targets: see benchmarks/README.md

use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn bench_rendering(c: &mut Criterion) {
    c.bench_function("rendering_placeholder", |b| {
        b.iter(|| black_box(0u64).wrapping_add(1));
    });
}

criterion_group!(benches, bench_rendering);
criterion_main!(benches);
