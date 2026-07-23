import { apiGet, API_BASE, type Job, type SystemInfo } from "@/lib/api";

function countByStatus(jobs: Job[]): Record<string, number> {
  return jobs.reduce<Record<string, number>>((acc, job) => {
    acc[job.status] = (acc[job.status] || 0) + 1;
    return acc;
  }, {});
}

export default async function OverviewPage() {
  let system: SystemInfo | null = null;
  let jobs: Job[] = [];
  let error: string | null = null;

  try {
    [system, jobs] = await Promise.all([
      apiGet<SystemInfo>("/v1/system"),
      apiGet<Job[]>("/v1/jobs?limit=50"),
    ]);
  } catch (e) {
    error = e instanceof Error ? e.message : "Failed to load overview";
  }

  const byStatus = countByStatus(jobs);
  const completed = byStatus.completed ?? 0;
  const failed = byStatus.failed ?? 0;
  const active =
    (byStatus.pending ?? 0) + (byStatus.queued ?? 0) + (byStatus.running ?? 0);

  return (
    <section>
      <h1>Overview</h1>
      <p className="lead">
        MediaCore — media extraction, processing, and automation platform.
      </p>
      {error ? <p className="muted">{error} (API: {API_BASE})</p> : null}
      <div className="grid">
        <div className="stat">
          <span className="muted">Version</span>
          <strong>{system?.version ?? "—"}</strong>
        </div>
        <div className="stat">
          <span className="muted">Environment</span>
          <strong>{system?.environment ?? "—"}</strong>
        </div>
        <div className="stat">
          <span className="muted">Providers</span>
          <strong>{system?.providers ?? "—"}</strong>
        </div>
        <div className="stat">
          <span className="muted">Plugins</span>
          <strong>{system?.plugins ?? "—"}</strong>
        </div>
        <div className="stat">
          <span className="muted">FFmpeg</span>
          <strong>{system ? (system.ffmpeg ? "yes" : "no") : "—"}</strong>
        </div>
        <div className="stat">
          <span className="muted">Events retained</span>
          <strong>{system?.events_retained ?? "—"}</strong>
        </div>
        <div className="stat">
          <span className="muted">Recent jobs</span>
          <strong>{jobs.length || "—"}</strong>
        </div>
        <div className="stat">
          <span className="muted">Active / done / failed</span>
          <strong>
            {system || jobs.length
              ? `${active} / ${completed} / ${failed}`
              : "—"}
          </strong>
        </div>
      </div>
    </section>
  );
}
