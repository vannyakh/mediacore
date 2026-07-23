import { apiGet } from "@/lib/api";

type Provider = { name: string; status: string };

export default async function ProvidersPage() {
  let providers: Provider[] = [];
  let error: string | null = null;
  try {
    providers = await apiGet<Provider[]>("/v1/providers");
  } catch (e) {
    error = e instanceof Error ? e.message : "Failed to load providers";
  }

  return (
    <section>
      <h1>Providers</h1>
      <p className="lead">Registered media providers (core stays provider-agnostic).</p>
      {error ? <p className="muted">{error}</p> : null}
      <div className="panel">
        <table className="table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {providers.map((p) => (
              <tr key={p.name}>
                <td>{p.name}</td>
                <td>{p.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
