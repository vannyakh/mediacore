//! Shared helpers for MediaCore Criterion benches and report tooling.

pub mod generators;
pub mod metrics;
pub mod utils;

pub use generators::{sample_manifest_json, sample_metadata_json, sample_urls};
pub use metrics::{BenchSample, LatencyStats};
pub use utils::percentile;
