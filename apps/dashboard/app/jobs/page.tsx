export default function JobsPage() {
  return (
    <section>
      <h1>Jobs</h1>
      <p className="lead">Inspect analyze and download job status.</p>
      <div className="panel">
        <p className="muted">
          Lookup a job via <code>GET /api/v1/jobs/&#123;id&#125;</code>. A list endpoint can be added next.
        </p>
      </div>
    </section>
  );
}
