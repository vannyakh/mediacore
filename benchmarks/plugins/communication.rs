//! MediaCore benchmark: communication
//!
//! Status: planned — scaffold for Criterion harness.
//! Categories and targets: see benchmarks/README.md

use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn bench_communication(c: &mut Criterion) {
    c.bench_function("communication_placeholder", |b| {
        b.iter(|| black_box(0u64).wrapping_add(1));
    });
}

criterion_group!(benches, bench_communication);
criterion_main!(benches);
