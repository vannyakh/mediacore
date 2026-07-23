//! Manifest JSON parse micro-benchmark.

use criterion::{black_box, criterion_group, criterion_main, Criterion};
use mediacore_bench_common::sample_manifest_json;
use serde_json::Value;

fn bench_manifest(c: &mut Criterion) {
    let payload = sample_manifest_json();
    c.bench_function("core/manifest_json_parse", |b| {
        b.iter(|| {
            let v: Value = serde_json::from_str(black_box(&payload)).expect("json");
            black_box(v);
        });
    });
}

criterion_group!(benches, bench_manifest);
criterion_main!(benches);
