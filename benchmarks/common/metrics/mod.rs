//! Metric types collected by MediaCore benchmarks.

use serde::{Deserialize, Serialize};

use crate::utils::percentile;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct LatencyStats {
    pub count: usize,
    pub mean_ns: f64,
    pub median_ns: f64,
    pub p95_ns: f64,
    pub p99_ns: f64,
    pub p999_ns: f64,
    pub min_ns: f64,
    pub max_ns: f64,
}

impl LatencyStats {
    pub fn from_sorted_ns(mut samples: Vec<f64>) -> Self {
        samples.sort_by(|a, b| a.partial_cmp(b).unwrap_or(std::cmp::Ordering::Equal));
        let count = samples.len();
        let mean = if count == 0 {
            0.0
        } else {
            samples.iter().sum::<f64>() / count as f64
        };
        Self {
            count,
            mean_ns: mean,
            median_ns: percentile(&samples, 0.50),
            p95_ns: percentile(&samples, 0.95),
            p99_ns: percentile(&samples, 0.99),
            p999_ns: percentile(&samples, 0.999),
            min_ns: samples.first().copied().unwrap_or(0.0),
            max_ns: samples.last().copied().unwrap_or(0.0),
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct BenchSample {
    pub name: String,
    pub category: String,
    pub latency: LatencyStats,
    pub ops_per_sec: f64,
    pub peak_memory_bytes: Option<u64>,
    pub allocations: Option<u64>,
}
