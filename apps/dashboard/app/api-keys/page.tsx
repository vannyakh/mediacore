import { API_KEY } from "@/lib/api";

export default function ApiKeysPage() {
  const masked =
    API_KEY.length <= 8 ? "••••••••" : `${API_KEY.slice(0, 4)}…${API_KEY.slice(-4)}`;

  return (
    <section>
      <h1>API Keys</h1>
      <p className="lead">Manage API keys used by clients and SDKs.</p>
      <div className="grid" style={{ marginBottom: "1.25rem" }}>
        <div className="stat">
          <span className="muted">Dashboard key</span>
          <strong style={{ fontSize: "1rem" }}>
            <code>{masked}</code>
          </strong>
        </div>
        <div className="stat">
          <span className="muted">Header</span>
          <strong style={{ fontSize: "1rem" }}>
            <code>X-API-Key</code>
          </strong>
        </div>
      </div>
      <div className="panel">
        <p className="muted">
          Dev seed key comes from <code>SEED_API_KEY</code> /{" "}
          <code>NEXT_PUBLIC_API_KEY</code>. Full key admin UI is planned; rotate secrets via
          environment for now.
        </p>
      </div>
    </section>
  );
}
