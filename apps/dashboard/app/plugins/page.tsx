import { apiGet } from "@/lib/api";

type Plugin = {
  name: string;
  version: string;
  kind: string;
  description: string;
  status: string;
  capabilities: string[];
};

export default async function PluginsPage() {
  let plugins: Plugin[] = [];
  let error: string | null = null;
  try {
    plugins = await apiGet<Plugin[]>("/v1/plugins");
  } catch (e) {
    error = e instanceof Error ? e.message : "Failed to load plugins";
  }

  return (
    <section>
      <h1>Plugins</h1>
      <p className="lead">MediaCore stays small — capabilities come from plugins.</p>
      {error ? <p className="muted">{error}</p> : null}
      <div className="panel">
        <table className="table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Kind</th>
              <th>Status</th>
              <th>Capabilities</th>
            </tr>
          </thead>
          <tbody>
            {plugins.map((p) => (
              <tr key={p.name}>
                <td>{p.name}</td>
                <td>{p.kind}</td>
                <td>{p.status}</td>
                <td>{(p.capabilities || []).join(", ")}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
