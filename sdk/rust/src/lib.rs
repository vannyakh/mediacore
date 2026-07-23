//! Stub crate for the apidownloader Rust SDK.

pub struct VideoExtractor {
    pub api_key: String,
    pub base_url: String,
}

impl VideoExtractor {
    pub fn new(api_key: impl Into<String>) -> Self {
        Self {
            api_key: api_key.into(),
            base_url: "http://localhost:8000".into(),
        }
    }
}
