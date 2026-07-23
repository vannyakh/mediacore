using System.Net.Http.Headers;
using System.Net.Http.Json;

namespace MediaCore.Sdk;

public class MediaCoreClient
{
    private readonly HttpClient _http;

    public MediaCoreClient(string apiKey, string baseUrl = "http://localhost:8000")
    {
        _http = new HttpClient { BaseAddress = new Uri(baseUrl.TrimEnd('/') + "/") };
        _http.DefaultRequestHeaders.Add("X-API-Key", apiKey);
        _http.DefaultRequestHeaders.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
        Media = new MediaApi(_http);
        Plugins = new PluginsApi(_http);
        Jobs = new JobsApi(_http);
    }

    public MediaApi Media { get; }
    public PluginsApi Plugins { get; }
    public JobsApi Jobs { get; }
}

public class MediaApi
{
    private readonly HttpClient _http;
    public MediaApi(HttpClient http) => _http = http;

    public Task<object?> AnalyzeAsync(string url) =>
        _http.PostAsJsonAsync("v1/analyze", new { url })
            .ContinueWith(async t => await t.Result.Content.ReadFromJsonAsync<object>())
            .Unwrap();
}

public class PluginsApi
{
    private readonly HttpClient _http;
    public PluginsApi(HttpClient http) => _http = http;

    public Task<object?> ListAsync() =>
        _http.GetFromJsonAsync<object>("v1/plugins");
}

public class JobsApi
{
    private readonly HttpClient _http;
    public JobsApi(HttpClient http) => _http = http;

    public Task<object?> GetAsync(string id) =>
        _http.GetFromJsonAsync<object>($"v1/jobs/{id}");
}
