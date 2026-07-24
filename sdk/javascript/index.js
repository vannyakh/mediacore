/**
 * MediaCore JavaScript SDK — thin client for the permitted download API.
 *
 * Install (from repo): npm install ./sdk/javascript
 */

const TERMINAL = new Set(["completed", "failed", "cancelled"]);

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
    if (res.status === 204) return null;
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
  };

  jobs = {
    list: (limit = 50) => this.#request(`/v1/jobs?limit=${encodeURIComponent(limit)}`),
    get: (id) => this.#request(`/v1/jobs/${id}`),
    wait: async (id, { timeout = 120000, interval = 500 } = {}) => {
      const deadline = Date.now() + timeout;
      let last = null;
      while (Date.now() < deadline) {
        last = await this.jobs.get(id);
        if (TERMINAL.has(String(last?.status || ""))) return last;
        await new Promise((r) => setTimeout(r, interval));
      }
      throw new Error(`job ${id} did not finish within ${timeout}ms`);
    },
  };

  providers = {
    list: () => this.#request("/v1/providers"),
  };

  plugins = {
    list: () => this.#request("/v1/plugins"),
  };
}

export default MediaCore;
