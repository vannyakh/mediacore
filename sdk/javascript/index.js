/**
 * MediaCore JavaScript SDK — unified client surface.
 *
 * client.media.analyze / download / convert / thumbnail
 * client.jobs.list / get
 * client.plugins.list
 */

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
    thumbnail: (url) =>
      this.#request("/v1/thumbnail", {
        method: "POST",
        body: JSON.stringify({ url }),
      }),
  };

  jobs = {
    list: (limit = 50) => this.#request(`/v1/jobs?limit=${encodeURIComponent(limit)}`),
    get: (id) => this.#request(`/v1/jobs/${id}`),
  };

  plugins = {
    list: () => this.#request("/v1/plugins"),
  };
}

export default MediaCore;
