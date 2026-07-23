//! Event dispatch micro-benchmark (in-process fan-out).

use criterion::{black_box, criterion_group, criterion_main, Criterion};

#[derive(Clone)]
struct Event {
    kind: &'static str,
    job_id: u64,
}

fn dispatch(events: &[Event], handlers: &[fn(&Event)]) {
    for e in events {
        for h in handlers {
            h(e);
        }
    }
}

fn noop(_e: &Event) {}

fn bench_events(c: &mut Criterion) {
    let events: Vec<Event> = (0..1000)
        .map(|i| Event {
            kind: "Progress",
            job_id: i,
        })
        .collect();
    let handlers: Vec<fn(&Event)> = vec![noop, noop, noop];
    c.bench_function("core/event_dispatch_1k", |b| {
        b.iter(|| dispatch(black_box(&events), black_box(&handlers)));
    });
}

criterion_group!(benches, bench_events);
criterion_main!(benches);
