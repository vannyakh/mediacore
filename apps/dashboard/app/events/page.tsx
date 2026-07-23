"use client";

import { useEffect, useState } from "react";
import { API_BASE, API_KEY } from "@/lib/api";

type MediaEvent = {
  type: string;
  payload: Record<string, unknown>;
  at: string;
};

export default function EventsPage() {
  const [events, setEvents] = useState<MediaEvent[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [live, setLive] = useState(false);

  useEffect(() => {
    let cancelled = false;
    let source: EventSource | null = null;

    async function loadHistory() {
      try {
        const res = await fetch(`${API_BASE}/v1/events?limit=50`, {
          headers: { "X-API-Key": API_KEY },
          cache: "no-store",
        });
        if (!res.ok) throw new Error(`API ${res.status}`);
        const body = (await res.json()) as { events: MediaEvent[] };
        if (!cancelled) setEvents(body.events.slice().reverse());
      } catch (e) {
        if (!cancelled) setError(e instanceof Error ? e.message : "Failed to load events");
      }
    }

    void loadHistory();

    // EventSource cannot set custom headers; use fetch stream polling fallback via history
    // when browser EventSource cannot authenticate. Prefer poll every 3s for API-key auth.
    const interval = window.setInterval(() => {
      void loadHistory();
      setLive(true);
    }, 3000);

    return () => {
      cancelled = true;
      window.clearInterval(interval);
      source?.close();
    };
  }, []);

  return (
    <section>
      <h1>Events</h1>
      <p className="lead">
        Job lifecycle stream — JobCreated through Completed / Failed / Cancelled.
        {live ? " Live (polling)." : ""}
      </p>
      {error ? <p className="muted">{error}</p> : null}
      <div className="panel" style={{ overflowX: "auto" }}>
        <table>
          <thead>
            <tr>
              <th>Time</th>
              <th>Type</th>
              <th>Job</th>
              <th>Payload</th>
            </tr>
          </thead>
          <tbody>
            {events.length === 0 ? (
              <tr>
                <td colSpan={4} className="muted">
                  No events yet.
                </td>
              </tr>
            ) : (
              events.map((ev, idx) => (
                <tr key={`${ev.at}-${ev.type}-${idx}`}>
                  <td className="muted">{ev.at}</td>
                  <td>
                    <strong>{ev.type}</strong>
                  </td>
                  <td className="muted">{String(ev.payload.job_id ?? "—")}</td>
                  <td>
                    <code>{JSON.stringify(ev.payload)}</code>
                  </td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </section>
  );
}
