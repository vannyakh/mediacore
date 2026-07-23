export class MediaCore {
  constructor(apiKey, baseUrl = "http://localhost:8000") {
    this.apiKey = apiKey;
    this.baseUrl = baseUrl.replace(/\/$/, "");
  }

  async #request(path, options = {}) {
    const res = await fetch(`${this.baseUrl}${path}`, {
      ...options,
      headers: {
        "Content-Type": "application/json",
        "X-API-Key": this.apiKey,
        ...(options.headers || {}),
      },
    });
    if (!res.ok) throw new Error(`API ${res.status}: ${await res.text()}`);
    return res.json();
  }

  media = {
    analyze: (url) =>
      this.#request("/v1/analyze", { method: "POST", body: JSON.stringify({ url }) }),
    download: (url, format = "original") =>
      this.#request("/v1/download", {
        method: "POST",
        body: JSON.stringify({ url, format }),
      }),
    convert: (path, options = {}) =>
      this.#request("/v1/convert", {
        method: "POST",
        body: JSON.stringify({ path, options }),
      }),
    thumbnail: (url) =>
      this.#request("/v1/thumbnail", {
        method: "POST",
        body: JSON.stringify({ url }),
      }),
  };

  jobs = {
    get: (id) => this.#request(`/v1/jobs/${id}`),
    list: async () => [],
  };

  plugins = {
    list: () => this.#request("/v1/plugins"),
  };
}

export const VideoExtractor = MediaCore;
