import { apiGetText, API_BASE } from "@/lib/api";

type MetricRow = { name: string; labels: string; value: string };

function parsePrometheus(text: string): MetricRow[] {
  const rows: MetricRow[] = [];
  for (const line of text.split("\n")) {
    if (!line || line.startsWith("#")) continue;
    const match = line.match(/^([a-zA-Z_:][a-zA-Z0-9_:]*)(\{[^}]*\})?\s+(.+)$/);
    if (!match) continue;
    const [, name, labels = "", value] = match;
    if (!name.startsWith("mediacore_")) continue;
    rows.push({ name, labels, value });
  }
  return rows.slice(0, 80);
}

export default async function MetricsPage() {
  let rows: MetricRow[] = [];
  let error: string | null = null;
  try {
    const text = await apiGetText("/metrics");
    rows = parsePrometheus(text);
  } catch (e) {
    error = e instanceof Error ? e.message : "Failed to load metrics";
  }

  return (
    <section>
      <h1>Metrics</h1>
      <p className="lead">
        Prometheus scrape endpoint at <code>{API_BASE}/metrics</code>.
      </p>
      {error ? <p className="muted">{error}</p> : null}
      <div className="panel">
        {rows.length === 0 && !error ? (
          <p className="muted">No mediacore_* samples yet. Hit the API to generate traffic.</p>
        ) : (
          <table className="table">
            <thead>
              <tr>
                <th>Metric</th>
                <th>Labels</th>
                <th>Value</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((row, i) => (
                <tr key={`${row.name}-${i}`}>
                  <td>
                    <code>{row.name}</code>
                  </td>
                  <td className="muted">{row.labels || "—"}</td>
                  <td>{row.value}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </section>
  );
}
