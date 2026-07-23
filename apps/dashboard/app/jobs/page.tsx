import { apiGet, type Job } from "@/lib/api";

function fmt(ts?: string | null): string {
  if (!ts) return "—";
  try {
    return new Date(ts).toLocaleString();
  } catch {
    return ts;
  }
}

export default async function JobsPage() {
  let jobs: Job[] = [];
  let error: string | null = null;
  try {
    jobs = await apiGet<Job[]>("/v1/jobs?limit=50");
  } catch (e) {
    error = e instanceof Error ? e.message : "Failed to load jobs";
  }

  return (
    <section>
      <h1>Jobs</h1>
      <p className="lead">Analyze, download, and processing job history.</p>
      {error ? <p className="muted">{error}</p> : null}
      <div className="panel">
        {jobs.length === 0 && !error ? (
          <p className="muted">No jobs yet. Create one via POST /v1/download or /v1/analyze.</p>
        ) : (
          <table className="table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Type</th>
                <th>Status</th>
                <th>Platform</th>
                <th>URL</th>
                <th>Created</th>
              </tr>
            </thead>
            <tbody>
              {jobs.map((job) => (
                <tr key={job.id}>
                  <td>
                    <code>{job.id.slice(0, 8)}</code>
                  </td>
                  <td>{job.type}</td>
                  <td>{job.status}</td>
                  <td>{job.platform || "—"}</td>
                  <td title={job.url}>
                    {job.url.length > 48 ? `${job.url.slice(0, 48)}…` : job.url}
                  </td>
                  <td>{fmt(job.created_at)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </section>
  );
}
