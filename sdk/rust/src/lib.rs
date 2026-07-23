//! MediaCore Rust SDK — unified client surface.
//!
//! ```ignore
//! let client = MediaCore::new("dev-api-key-change-me");
//! let meta = client.media().analyze("https://example.com/a.mp4").await?;
//! let job = client.media().download("https://example.com/a.mp4", "original").await?;
//! let jobs = client.jobs().list(50).await?;
//! let plugins = client.plugins().list().await?;
//! ```

use reqwest::Client;
use serde_json::Value;
use thiserror::Error;

#[derive(Debug, Error)]
pub enum Error {
    #[error("http: {0}")]
    Http(#[from] reqwest::Error),
    #[error("api {status}: {body}")]
    Api { status: u16, body: String },
}

pub type Result<T> = std::result::Result<T, Error>;

#[derive(Clone)]
pub struct MediaCore {
    api_key: String,
    base_url: String,
    http: Client,
}

impl MediaCore {
    pub fn new(api_key: impl Into<String>) -> Self {
        Self::with_base_url(api_key, "http://localhost:8000")
    }

    pub fn with_base_url(api_key: impl Into<String>, base_url: impl Into<String>) -> Self {
        Self {
            api_key: api_key.into(),
            base_url: base_url.into().trim_end_matches('/').to_string(),
            http: Client::new(),
        }
    }

    pub fn media(&self) -> MediaApi<'_> {
        MediaApi { client: self }
    }

    pub fn jobs(&self) -> JobsApi<'_> {
        JobsApi { client: self }
    }

    pub fn plugins(&self) -> PluginsApi<'_> {
        PluginsApi { client: self }
    }

    async fn request(&self, method: reqwest::Method, path: &str, body: Option<Value>) -> Result<Value> {
        let mut req = self
            .http
            .request(method, format!("{}{}", self.base_url, path))
            .header("X-API-Key", &self.api_key)
            .header("Content-Type", "application/json");
        if let Some(b) = body {
            req = req.json(&b);
        }
        let res = req.send().await?;
        let status = res.status().as_u16();
        let text = res.text().await?;
        if status >= 400 {
            return Err(Error::Api { status, body: text });
        }
        if text.is_empty() {
            return Ok(Value::Null);
        }
        Ok(serde_json::from_str(&text).unwrap_or(Value::String(text)))
    }
}

pub struct MediaApi<'a> {
    client: &'a MediaCore,
}

impl MediaApi<'_> {
    pub async fn analyze(&self, url: &str) -> Result<Value> {
        self.client
            .request(
                reqwest::Method::POST,
                "/v1/analyze",
                Some(serde_json::json!({ "url": url })),
            )
            .await
    }

    pub async fn download(&self, url: &str, format: &str) -> Result<Value> {
        let format = if format.is_empty() { "original" } else { format };
        self.client
            .request(
                reqwest::Method::POST,
                "/v1/download",
                Some(serde_json::json!({ "url": url, "format": format })),
            )
            .await
    }

    pub async fn convert(&self, path: &str, options: Value) -> Result<Value> {
        self.client
            .request(
                reqwest::Method::POST,
                "/v1/convert",
                Some(serde_json::json!({ "path": path, "options": options })),
            )
            .await
    }

    pub async fn thumbnail(&self, url: &str) -> Result<Value> {
        self.client
            .request(
                reqwest::Method::POST,
                "/v1/thumbnail",
                Some(serde_json::json!({ "url": url })),
            )
            .await
    }
}

pub struct JobsApi<'a> {
    client: &'a MediaCore,
}

impl JobsApi<'_> {
    pub async fn list(&self, limit: u32) -> Result<Value> {
        let limit = if limit == 0 { 50 } else { limit };
        self.client
            .request(
                reqwest::Method::GET,
                &format!("/v1/jobs?limit={limit}"),
                None,
            )
            .await
    }

    pub async fn get(&self, id: &str) -> Result<Value> {
        self.client
            .request(reqwest::Method::GET, &format!("/v1/jobs/{id}"), None)
            .await
    }
}

pub struct PluginsApi<'a> {
    client: &'a MediaCore,
}

impl PluginsApi<'_> {
    pub async fn list(&self) -> Result<Value> {
        self.client
            .request(reqwest::Method::GET, "/v1/plugins", None)
            .await
    }
}
