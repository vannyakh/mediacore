import { apiGet, type Job } from "@/lib/api";

const QUEUES = [
  { name: "analyze", description: "Metadata / analyze jobs" },
  { name: "download", description: "Media download jobs" },
  { name: "process", description: "Audio, video, convert, clip, subtitles" },
  { name: "cleanup", description: "Expired file cleanup" },
] as const;

export default async function QueuePage() {
  let jobs: Job[] = [];
  let error: string | null = null;
  try {
    jobs = await apiGet<Job[]>("/v1/jobs?limit=100");
  } catch (e) {
    error = e instanceof Error ? e.message : "Failed to load queue snapshot";
  }

  const pending = jobs.filter((j) =>
    ["pending", "queued", "running"].includes(j.status.toLowerCase()),
  );
  const byType = pending.reduce<Record<string, number>>((acc, job) => {
    const key = job.type || "unknown";
    acc[key] = (acc[key] || 0) + 1;
    return acc;
  }, {});

  return (
    <section>
      <h1>Queue</h1>
      <p className="lead">Dramatiq queues backing analyze, download, process, and cleanup.</p>
      {error ? <p className="muted">{error}</p> : null}
      <div className="grid" style={{ marginBottom: "1.25rem" }}>
        <div className="stat">
          <span className="muted">In-flight jobs</span>
          <strong>{error ? "—" : pending.length}</strong>
        </div>
        <div className="stat">
          <span className="muted">Recent sample</span>
          <strong>{error ? "—" : jobs.length}</strong>
        </div>
      </div>
      <div className="panel">
        <table className="table">
          <thead>
            <tr>
              <th>Queue</th>
              <th>Description</th>
              <th>Active (by job type)</th>
            </tr>
          </thead>
          <tbody>
            {QUEUES.map((q) => (
              <tr key={q.name}>
                <td>
                  <code>{q.name}</code>
                </td>
                <td>{q.description}</td>
                <td>{byType[q.name] ?? 0}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
