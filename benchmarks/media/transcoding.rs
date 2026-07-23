//! MediaCore benchmark: transcoding
//!
//! Status: planned — scaffold for Criterion harness.
//! Categories and targets: see benchmarks/README.md

use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn bench_transcoding(c: &mut Criterion) {
    c.bench_function("transcoding_placeholder", |b| {
        b.iter(|| black_box(0u64).wrapping_add(1));
    });
}

criterion_group!(benches, bench_transcoding);
criterion_main!(benches);
