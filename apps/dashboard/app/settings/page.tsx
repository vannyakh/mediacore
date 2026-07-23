import { API_BASE } from "@/lib/api";

const SETTINGS = [
  { key: "NEXT_PUBLIC_API_BASE", value: API_BASE, note: "Dashboard → API origin" },
  { key: "SEED_API_KEY", value: "(env)", note: "Bootstraps the first API key" },
  { key: "SYNC_DOWNLOAD", value: "(env)", note: "Run downloads in-process" },
  { key: "USE_SQLITE", value: "(env)", note: "Local SQLite instead of Postgres" },
  { key: "REDIS_URL", value: "(env)", note: "Dramatiq broker" },
  { key: "STORAGE_ROOT", value: "(env)", note: "Job artifact directory" },
] as const;

export default function SettingsPage() {
  return (
    <section>
      <h1>Settings</h1>
      <p className="lead">Environment and platform configuration.</p>
      <div className="panel">
        <table className="table">
          <thead>
            <tr>
              <th>Variable</th>
              <th>Value</th>
              <th>Notes</th>
            </tr>
          </thead>
          <tbody>
            {SETTINGS.map((s) => (
              <tr key={s.key}>
                <td>
                  <code>{s.key}</code>
                </td>
                <td>
                  <code>{s.value}</code>
                </td>
                <td className="muted">{s.note}</td>
              </tr>
            ))}
          </tbody>
        </table>
        <p className="muted" style={{ marginTop: "1rem" }}>
          Edit <code>.env</code> (see <code>.env.example</code>) and restart API / worker /
          dashboard.
        </p>
      </div>
    </section>
  );
}