//! In-memory cache lookup micro-benchmark.

use std::collections::HashMap;

use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn bench_cache(c: &mut Criterion) {
    let mut map = HashMap::with_capacity(1024);
    for i in 0..1024u32 {
        map.insert(format!("k{i}"), i);
    }
    c.bench_function("core/cache_lookup", |b| {
        b.iter(|| {
            for i in 0..64u32 {
                black_box(map.get(black_box(&format!("k{i}"))));
            }
        });
    });
}

criterion_group!(benches, bench_cache);
criterion_main!(benches);
