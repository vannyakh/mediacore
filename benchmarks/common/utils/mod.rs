//! Small utilities shared across benches.

/// Percentile of a **sorted** slice (`p` in `0.0..=1.0`).
pub fn percentile(sorted: &[f64], p: f64) -> f64 {
    if sorted.is_empty() {
        return 0.0;
    }
    if sorted.len() == 1 {
        return sorted[0];
    }
    let clamped = p.clamp(0.0, 1.0);
    let idx = (clamped * (sorted.len() as f64 - 1.0)).round() as usize;
    sorted[idx.min(sorted.len() - 1)]
}
