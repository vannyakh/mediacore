import { apiGet, API_BASE, type SystemInfo } from "@/lib/api";

export default async function StoragePage() {
  let system: SystemInfo | null = null;
  let error: string | null = null;
  try {
    system = await apiGet<SystemInfo>("/v1/system");
  } catch (e) {
    error = e instanceof Error ? e.message : "Failed to load system";
  }

  return (
    <section>
      <h1>Storage</h1>
      <p className="lead">Local and plugin-backed file storage for job outputs.</p>
      {error ? <p className="muted">{error}</p> : null}
      <div className="grid" style={{ marginBottom: "1.25rem" }}>
        <div className="stat">
          <span className="muted">Public files mount</span>
          <strong>
            <code>/files</code>
          </strong>
        </div>
        <div className="stat">
          <span className="muted">API base</span>
          <strong style={{ fontSize: "1rem" }}>{API_BASE}</strong>
        </div>
        <div className="stat">
          <span className="muted">FFmpeg</span>
          <strong>{system ? (system.ffmpeg ? "available" : "missing") : "—"}</strong>
        </div>
      </div>
      <div className="panel">
        <p className="muted">
          Default root is <code>STORAGE_ROOT</code> (./data/files). Completed jobs expose
          artifacts via <code>{API_BASE}/files/…</code>. Storage plugins (e.g. storage-local)
          extend backends without changing core.
        </p>
      </div>
    </section>
  );
}
