//! URL parsing micro-benchmark.

use criterion::{black_box, criterion_group, criterion_main, Criterion};
use mediacore_bench_common::sample_urls;
use url::Url;

fn parse_url(raw: &str) -> bool {
    Url::parse(raw).is_ok()
}

fn bench_url_parser(c: &mut Criterion) {
    let urls = sample_urls();
    c.bench_function("core/url_parse", |b| {
        b.iter(|| {
            for u in &urls {
                black_box(parse_url(u));
            }
        });
    });
}

criterion_group!(benches, bench_url_parser);
criterion_main!(benches);
