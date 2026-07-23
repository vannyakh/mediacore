//! MediaCore benchmark: filesystem
//!
//! Status: planned — scaffold for Criterion harness.
//! Categories and targets: see benchmarks/README.md

use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn bench_filesystem(c: &mut Criterion) {
    c.bench_function("filesystem_placeholder", |b| {
        b.iter(|| black_box(0u64).wrapping_add(1));
    });
}

criterion_group!(benches, bench_filesystem);
criterion_main!(benches);
