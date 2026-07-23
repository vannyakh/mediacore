using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Text.Json;

namespace MediaCore.Sdk;

/// <summary>
/// MediaCore C# SDK — unified client surface.
/// client.Media.Analyze / Download / Convert / Thumbnail
/// client.Jobs.List / Get
/// client.Plugins.List
/// </summary>
public class MediaCore
{
    private readonly HttpClient _http;

    public MediaCore(string apiKey, string baseUrl = "http://localhost:8000")
    {
        _http = new HttpClient { BaseAddress = new Uri(baseUrl.TrimEnd('/') + "/") };
        _http.DefaultRequestHeaders.Add("X-API-Key", apiKey);
        _http.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
        Media = new MediaApi(_http);
        Jobs = new JobsApi(_http);
        Plugins = new PluginsApi(_http);
    }

    public MediaApi Media { get; }
    public JobsApi Jobs { get; }
    public PluginsApi Plugins { get; }
}

// Back-compat alias
public class MediaCoreClient : MediaCore
{
    public MediaCoreClient(string apiKey, string baseUrl = "http://localhost:8000")
        : base(apiKey, baseUrl) { }
}

public class MediaApi
{
    private readonly HttpClient _http;
    public MediaApi(HttpClient http) => _http = http;

    public async Task<JsonElement> AnalyzeAsync(string url, CancellationToken ct = default)
    {
        var res = await _http.PostAsJsonAsync("v1/analyze", new { url }, ct);
        await EnsureSuccess(res);
        return await res.Content.ReadFromJsonAsync<JsonElement>(cancellationToken: ct);
    }

    public async Task<JsonElement> DownloadAsync(string url, string format = "original", CancellationToken ct = default)
    {
        var res = await _http.PostAsJsonAsync("v1/download", new { url, format }, ct);
        await EnsureSuccess(res);
        return await res.Content.ReadFromJsonAsync<JsonElement>(cancellationToken: ct);
    }

    public async Task<JsonElement> ConvertAsync(string path, object? options = null, CancellationToken ct = default)
    {
        var res = await _http.PostAsJsonAsync("v1/convert", new { path, options = options ?? new { } }, ct);
        await EnsureSuccess(res);
        return await res.Content.ReadFromJsonAsync<JsonElement>(cancellationToken: ct);
    }

    public async Task<JsonElement> ThumbnailAsync(string url, CancellationToken ct = default)
    {
        var res = await _http.PostAsJsonAsync("v1/thumbnail", new { url }, ct);
        await EnsureSuccess(res);
        return await res.Content.ReadFromJsonAsync<JsonElement>(cancellationToken: ct);
    }

    private static async Task EnsureSuccess(HttpResponseMessage res)
    {
        if (!res.IsSuccessStatusCode)
        {
            var body = await res.Content.ReadAsStringAsync();
            throw new HttpRequestException($"API {(int)res.StatusCode}: {body}");
        }
    }
}

public class JobsApi
{
    private readonly HttpClient _http;
    public JobsApi(HttpClient http) => _http = http;

    public async Task<JsonElement> ListAsync(int limit = 50, CancellationToken ct = default)
    {
        var res = await _http.GetAsync($"v1/jobs?limit={limit}", ct);
        if (!res.IsSuccessStatusCode)
        {
            var body = await res.Content.ReadAsStringAsync(ct);
            throw new HttpRequestException($"API {(int)res.StatusCode}: {body}");
        }
        return await res.Content.ReadFromJsonAsync<JsonElement>(cancellationToken: ct);
    }

    public async Task<JsonElement> GetAsync(string id, CancellationToken ct = default)
    {
        var res = await _http.GetAsync($"v1/jobs/{id}", ct);
        if (!res.IsSuccessStatusCode)
        {
            var body = await res.Content.ReadAsStringAsync(ct);
            throw new HttpRequestException($"API {(int)res.StatusCode}: {body}");
        }
        return await res.Content.ReadFromJsonAsync<JsonElement>(cancellationToken: ct);
    }
}

public class PluginsApi
{
    private readonly HttpClient _http;
    public PluginsApi(HttpClient http) => _http = http;

    public async Task<JsonElement> ListAsync(CancellationToken ct = default)
    {
        var res = await _http.GetAsync("v1/plugins", ct);
        if (!res.IsSuccessStatusCode)
        {
            var body = await res.Content.ReadAsStringAsync(ct);
            throw new HttpRequestException($"API {(int)res.StatusCode}: {body}");
        }
        return await res.Content.ReadFromJsonAsync<JsonElement>(cancellationToken: ct);
    }
}
