# MediaCore Rust SDK

```rust
use mediacore_sdk::MediaCore;

#[tokio::main]
async fn main() -> mediacore_sdk::Result<()> {
    let client = MediaCore::new("dev-api-key-change-me");
    let meta = client.media().analyze("https://example.com/video.mp4").await?;
    let _job = client.media().download("https://example.com/video.mp4", "original").await?;
    let _jobs = client.jobs().list(50).await?;
    let _plugins = client.plugins().list().await?;
    println!("{meta}");
    Ok(())
}
```

See [docs/sdk/](../../docs/sdk/).
