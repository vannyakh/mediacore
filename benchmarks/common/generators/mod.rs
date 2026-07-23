//! Synthetic datasets for micro-benchmarks (no network I/O).

pub fn sample_urls() -> Vec<&'static str> {
    vec![
        "https://cdn.example.com/demo.mp4",
        "https://cdn.example.com/path/to/clip.webm?token=abc",
        "file:///tmp/mediacore/sample.mp4",
        "mediacore://example/demo",
        "https://user:pass@media.example.org:8443/v1/asset.m3u8",
    ]
}

pub fn sample_metadata_json() -> String {
    r#"{
      "platform": "generic",
      "url": "https://cdn.example.com/demo.mp4",
      "title": "demo.mp4",
      "duration": 12.5,
      "formats": [
        {"id": "original", "quality": "original", "container": "mp4"}
      ]
    }"#
    .to_string()
}

pub fn sample_manifest_json() -> String {
    r#"{
      "type": "basic",
      "provider": "generic",
      "url": "https://cdn.example.com/demo.mp4",
      "format_ids": ["original"],
      "is_live": false
    }"#
    .to_string()
}
