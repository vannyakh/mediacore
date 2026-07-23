//! In-memory queue push/pop micro-benchmark.

use std::collections::VecDeque;

use criterion::{black_box, criterion_group, criterion_main, Criterion};

fn bench_queue(c: &mut Criterion) {
    c.bench_function("core/queue_push_pop", |b| {
        b.iter(|| {
            let mut q = VecDeque::with_capacity(256);
            for i in 0..256u32 {
                q.push_back(black_box(i));
            }
            while let Some(v) = q.pop_front() {
                black_box(v);
            }
        });
    });
}

criterion_group!(benches, bench_queue);
criterion_main!(benches);
