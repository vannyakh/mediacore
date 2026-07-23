const WORKERS = [
  { actor: "analyze_job", queue: "analyze", role: "URL analyze / metadata" },
  { actor: "download_job", queue: "download", role: "Media download" },
  { actor: "process_job", queue: "process", role: "Transform (audio/video/clip/…)" },
  { actor: "cleanup_job", queue: "cleanup", role: "Expire and remove artifacts" },
] as const;

export default function WorkersPage() {
  return (
    <section>
      <h1>Workers</h1>
      <p className="lead">Dramatiq workers processing MediaCore queues.</p>
      <div className="panel">
        <table className="table">
          <thead>
            <tr>
              <th>Actor</th>
              <th>Queue</th>
              <th>Role</th>
            </tr>
          </thead>
          <tbody>
            {WORKERS.map((w) => (
              <tr key={w.actor}>
                <td>
                  <code>{w.actor}</code>
                </td>
                <td>
                  <code>{w.queue}</code>
                </td>
                <td>{w.role}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <p className="muted" style={{ marginTop: "1rem" }}>
          Run with <code>uv run python -m apps.worker</code>. Set{" "}
          <code>SYNC_DOWNLOAD=true</code> or <code>DRAMATIQ_STUB=true</code> for local
          in-process execution without Redis.
        </p>
      </div>
    </section>
  );
}
