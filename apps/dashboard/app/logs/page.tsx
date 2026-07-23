export default function LogsPage() {
  return (
    <section>
      <h1>Logs</h1>
      <p className="lead">Request and audit trail for sensitive actions.</p>
      <div className="panel">
        <p className="muted">
          API request logging runs via middleware. An <code>audit_logs</code> browser for
          key creates, job deletes, and admin actions is planned next.
        </p>
      </div>
    </section>
  );
}
