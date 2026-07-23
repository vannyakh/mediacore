export default function DashboardPage() {
  return (
    <section>
      <h1>Dashboard</h1>
      <p className="lead">Overview of extraction jobs, usage, and worker health.</p>
      <div className="grid">
        <div className="stat">
          <span className="muted">Jobs (24h)</span>
          <strong>—</strong>
        </div>
        <div className="stat">
          <span className="muted">Success rate</span>
          <strong>—</strong>
        </div>
        <div className="stat">
          <span className="muted">Active workers</span>
          <strong>—</strong>
        </div>
        <div className="stat">
          <span className="muted">API keys</span>
          <strong>—</strong>
        </div>
      </div>
    </section>
  );
}
