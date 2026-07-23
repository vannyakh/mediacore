export type AnalyzeResult = {
  platform: string;
  title: string;
  formats: Array<{ id: string; quality: string; container: string }>;
  manifest?: Record<string, unknown>;
};

export class MediaCore {
  constructor(
    private apiKey: string,
    private baseUrl = "http://localhost:8000",
  ) {}

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
      this.request("/v1/download", {
        method: "POST",
        body: JSON.stringify({ url, format }),
      }),
    convert: (path: string, options: Record<string, unknown> = {}) =>
      this.request("/v1/convert", {
        method: "POST",
        body: JSON.stringify({ path, options }),
      }),
    thumbnail: (url: string) =>
      this.request("/v1/thumbnail", {
        method: "POST",
        body: JSON.stringify({ url }),
      }),
  };

  jobs = {
    get: (id: string) => this.request(`/v1/jobs/${id}`),
    list: async () => [] as unknown[],
  };

  plugins = {
    list: () => this.request("/v1/plugins"),
  };
}
