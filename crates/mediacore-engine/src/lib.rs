//! MediaCore Engine (Rust) — scaffold for the future core runtime.
//!
//! The Python packages under `packages/` are the v0.1 foundation.
//! This crate will own plugin loading, pipelines, and job orchestration.

pub trait Provider {
    fn name(&self) -> &str;
    fn supports(&self, url: &str) -> bool;
}

pub struct Engine;

impl Engine {
    pub fn new() -> Self {
        Self
    }
}

impl Default for Engine {
    fn default() -> Self {
        Self::new()
    }
}
