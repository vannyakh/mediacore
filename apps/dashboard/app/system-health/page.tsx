import { API_BASE } from "@/lib/api";

type Health = { status: string; service: string; version: string };

export default async function SystemHealthPage() {
  let health: Health | null = null;
  let error: string | null = null;
  try {
    const res = await fetch(`${API_BASE}/health`, { cache: "no-store" });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    health = (await res.json()) as Health;
  } catch (e) {
    error = e instanceof Error ? e.message : "Unreachable";
  }

  return (
    <section>
      <h1>System Health</h1>
      <p className="lead">API liveness and dependency status.</p>
      <div className="panel">
        {error ? (
          <p className="muted">API unreachable: {error}</p>
        ) : (
          <table className="table">
            <tbody>
              <tr>
                <th>Status</th>
                <td>{health?.status}</td>
              </tr>
              <tr>
                <th>Service</th>
                <td>{health?.service}</td>
              </tr>
              <tr>
                <th>Version</th>
                <td>{health?.version}</td>
              </tr>
            </tbody>
          </table>
        )}
      </div>
    </section>
  );
}
