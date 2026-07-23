/**
 * MediaCore TypeScript SDK — same surface as JS / Python / Go / Rust / Dart / C#.
 */

export type AnalyzeResult = {
  platform: string;
  title: string;
  url?: string;
  formats: Array<{ id: string; quality: string; container: string }>;
  manifest?: Record<string, unknown>;
};

export type JobCreateResult = {
  job_id: string;
  status: string;
  type: string;
};

export type JobResult = {
  id: string;
  status: string;
  type: string;
  url: string;
  platform?: string | null;
  format_id?: string | null;
  error?: string | null;
  result_url?: string | null;
};

export type PluginResult = {
  name: string;
  version: string;
  kind: string;
  description: string;
  status: string;
  capabilities?: string[];
};

export class MediaCore {
  constructor(
    private apiKey: string,
    private baseUrl = "http://localhost:8000",
  ) {
    this.baseUrl = baseUrl.replace(/\/$/, "");
  }

  private async request<T>(path: string, init?: RequestInit): Promise<T> {
    const res = await fetch(`${this.baseUrl}${path}`, {
      ...init,
      headers: {
        "Content-Type": "application/json",
        "X-API-Key": this.apiKey,
        ...(init?.headers || {}),
      },
    });
    if (!res.ok) throw new Error(`API ${res.status}: ${await res.text()}`);
    return res.json() as Promise<T>;
  }

  media = {
    analyze: (url: string) =>
      this.request<AnalyzeResult>("/v1/analyze", {
        method: "POST",
        body: JSON.stringify({ url }),
      }),
    download: (url: string, format = "original") =>
      this.request<JobCreateResult>("/v1/download", {
        method: "POST",
        body: JSON.stringify({ url, format }),
      }),
    convert: (path: string, options: Record<string, unknown> = {}) =>
      this.request<JobCreateResult>("/v1/convert", {
        method: "POST",
        body: JSON.stringify({ path, options }),
      }),
    thumbnail: (url: string) =>
      this.request<JobCreateResult>("/v1/thumbnail", {
        method: "POST",
        body: JSON.stringify({ url }),
      }),
  };

  jobs = {
    list: (limit = 50) =>
      this.request<JobResult[]>(`/v1/jobs?limit=${encodeURIComponent(String(limit))}`),
    get: (id: string) => this.request<JobResult>(`/v1/jobs/${id}`),
  };

  plugins = {
    list: () => this.request<PluginResult[]>("/v1/plugins"),
  };
}

export default MediaCore;
