import { apiGet } from "@/lib/api";

type Provider = {
  name: string;
  status: string;
  source?: string | null;
  capabilities?: string[];
};

type CatalogSummary = {
  source?: string | null;
  extractors: number;
  base_platforms: number;
  providers_indexed: number;
  providers_with_hosts: number;
  broken: number;
  note: string;
};

export default async function ProvidersPage() {
  let providers: Provider[] = [];
  let catalog: CatalogSummary | null = null;
  let error: string | null = null;
  try {
    [providers, catalog] = await Promise.all([
      apiGet<Provider[]>("/v1/providers"),
      apiGet<CatalogSummary>("/v1/providers/catalog"),
    ]);
  } catch (e) {
    error = e instanceof Error ? e.message : "Failed to load providers";
  }

  return (
    <section>
      <h1>Providers</h1>
      <p className="lead">Registered media providers (core stays provider-agnostic).</p>
      {error ? <p className="muted">{error}</p> : null}
      {catalog ? (
        <div className="grid" style={{ marginBottom: "1.25rem" }}>
          <div className="stat">
            <span className="muted">Catalog extractors</span>
            <strong>{catalog.extractors}</strong>
          </div>
          <div className="stat">
            <span className="muted">Indexed providers</span>
            <strong>{catalog.providers_indexed}</strong>
          </div>
          <div className="stat">
            <span className="muted">With hosts</span>
            <strong>{catalog.providers_with_hosts}</strong>
          </div>
          <div className="stat">
            <span className="muted">Broken</span>
            <strong>{catalog.broken}</strong>
          </div>
        </div>
      ) : null}
      <div className="panel">
        <table className="table">
          <thead>
            <tr>
              <th>Name</th>
              <th>Status</th>
              <th>Source</th>
              <th>Capabilities</th>
            </tr>
          </thead>
          <tbody>
            {providers.map((p) => (
              <tr key={p.name}>
                <td>{p.name}</td>
                <td>{p.status}</td>
                <td>{p.source || "—"}</td>
                <td>{(p.capabilities || []).join(", ") || "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
