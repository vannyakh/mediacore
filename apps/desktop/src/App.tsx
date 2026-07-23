import { useEffect, useState } from "react";

const API_BASE = "http://localhost:8000";
const API_KEY = "dev-api-key-change-me";

type MediaEvent = {
  type: string;
  payload: Record<string, unknown>;
  at: string;
};

export default function App() {
  const [events, setEvents] = useState<MediaEvent[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;

    async function refresh() {
      try {
        const res = await fetch(`${API_BASE}/v1/events?limit=20`, {
          headers: { "X-API-Key": API_KEY },
        });
        if (!res.ok) throw new Error(`API ${res.status}`);
        const body = (await res.json()) as { events: MediaEvent[] };
        if (!cancelled) {
          setEvents(body.events.slice().reverse());
          setError(null);
        }
      } catch (e) {
        if (!cancelled) setError(e instanceof Error ? e.message : "Failed to load events");
      }
    }

    void refresh();
    const id = window.setInterval(() => void refresh(), 4000);
    return () => {
      cancelled = true;
      window.clearInterval(id);
    };
  }, []);

  return (
    <main style={{ fontFamily: "IBM Plex Sans, sans-serif", padding: "2rem", maxWidth: 720 }}>
      <h1>MediaCore Desktop</h1>
      <p>
        Event stream consumer scaffold. Full Tauri shell (drag & drop, batch jobs) arrives in v0.4.
        Polls <code>GET /v1/events</code> — same contract as Dashboard and CLI.
      </p>
      {error ? <p style={{ color: "#b00020" }}>{error}</p> : null}
      <ul style={{ listStyle: "none", padding: 0 }}>
        {events.length === 0 ? (
          <li style={{ opacity: 0.6 }}>No recent events.</li>
        ) : (
          events.map((ev, idx) => (
            <li
              key={`${ev.at}-${ev.type}-${idx}`}
              style={{
                borderTop: "1px solid #ddd",
                padding: "0.6rem 0",
                fontSize: "0.9rem",
              }}
            >
              <strong>{ev.type}</strong>{" "}
              <span style={{ opacity: 0.6 }}>{ev.at}</span>
              <div style={{ fontFamily: "ui-monospace, monospace", fontSize: "0.8rem" }}>
                {JSON.stringify(ev.payload)}
              </div>
            </li>
          ))
        )}
      </ul>
    </main>
  );
}
