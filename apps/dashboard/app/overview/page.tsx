import { apiGet, API_BASE } from "@/lib/api";

type System = {
  name: string;
  version: string;
  providers: number;
  plugins: number;
  ffmpeg: boolean;
};

export default async function OverviewPage() {
  let system: System | null = null;
  let error: string | null = null;
  try {
    system = await apiGet<System>("/v1/system");
  } catch (e) {
    error = e instanceof Error ? e.message : "Failed to load system";
  }

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
      </div>
    </section>
  );
}
