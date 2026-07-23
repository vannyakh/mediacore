const API_BASE = process.env.NEXT_PUBLIC_API_BASE || "http://localhost:8000";
const API_KEY = process.env.NEXT_PUBLIC_API_KEY || "dev-api-key-change-me";

export async function apiGet<T>(path: string): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { "X-API-Key": API_KEY },
    cache: "no-store",
  });
  if (!res.ok) {
    throw new Error(`API ${res.status}: ${await res.text()}`);
  }
  return res.json() as Promise<T>;
}

export async function apiGetText(path: string, auth = false): Promise<string> {
  const headers: HeadersInit = auth ? { "X-API-Key": API_KEY } : {};
  const res = await fetch(`${API_BASE}${path}`, { headers, cache: "no-store" });
  if (!res.ok) {
    throw new Error(`API ${res.status}: ${await res.text()}`);
  }
  return res.text();
}

export type Job = {
  id: string;
  status: string;
  type: string;
  url: string;
  platform?: string | null;
  format_id?: string | null;
  error?: string | null;
  result_url?: string | null;
  created_at?: string | null;
  completed_at?: string | null;
};

export type SystemInfo = {
  name: string;
  version: string;
  environment: string;
  providers: number;
  plugins: number;
  ffmpeg: boolean;
  events_retained: number;
};

export type MediaEvent = {
  type: string;
  payload: Record<string, unknown>;
  at: string;
};

export { API_BASE, API_KEY };
