import 'dart:convert';

import 'package:http/http.dart' as http;

/// MediaCore Dart SDK — unified client surface.
///
/// client.media.analyze / download / convert / thumbnail
/// client.jobs.list / get
/// client.plugins.list
class MediaCore {
  MediaCore(this.apiKey, {this.baseUrl = 'http://localhost:8000', http.Client? httpClient})
      : _http = httpClient ?? http.Client() {
    media = MediaApi(this);
    jobs = JobsApi(this);
    plugins = PluginsApi(this);
  }

  final String apiKey;
  final String baseUrl;
  final http.Client _http;

  late final MediaApi media;
  late final JobsApi jobs;
  late final PluginsApi plugins;

  Future<dynamic> request(String method, String path, {Object? body}) async {
    final uri = Uri.parse('${baseUrl.replaceAll(RegExp(r'/$'), '')}$path');
    final headers = {
      'Content-Type': 'application/json',
      'X-API-Key': apiKey,
    };
    late http.Response res;
    switch (method) {
      case 'GET':
        res = await _http.get(uri, headers: headers);
      case 'POST':
        res = await _http.post(uri, headers: headers, body: body == null ? null : jsonEncode(body));
      default:
        throw ArgumentError('Unsupported method $method');
    }
    if (res.statusCode >= 400) {
      throw StateError('API ${res.statusCode}: ${res.body}');
    }
    if (res.body.isEmpty) return null;
    return jsonDecode(res.body);
  }

  void close() => _http.close();
}

class MediaApi {
  MediaApi(this._client);
  final MediaCore _client;

  Future<Map<String, dynamic>> analyze(String url) async {
    final out = await _client.request('POST', '/v1/analyze', body: {'url': url});
    return Map<String, dynamic>.from(out as Map);
  }

  Future<Map<String, dynamic>> download(String url, [String format = 'original']) async {
    final out = await _client.request('POST', '/v1/download', body: {'url': url, 'format': format});
    return Map<String, dynamic>.from(out as Map);
  }

  Future<Map<String, dynamic>> convert(String path, [Map<String, dynamic> options = const {}]) async {
    final out = await _client.request('POST', '/v1/convert', body: {'path': path, 'options': options});
    return Map<String, dynamic>.from(out as Map);
  }

  Future<Map<String, dynamic>> thumbnail(String url) async {
    final out = await _client.request('POST', '/v1/thumbnail', body: {'url': url});
    return Map<String, dynamic>.from(out as Map);
  }
}

class JobsApi {
  JobsApi(this._client);
  final MediaCore _client;

  Future<List<dynamic>> list([int limit = 50]) async {
    final out = await _client.request('GET', '/v1/jobs?limit=$limit');
    return List<dynamic>.from(out as List);
  }

  Future<Map<String, dynamic>> get(String id) async {
    final out = await _client.request('GET', '/v1/jobs/$id');
    return Map<String, dynamic>.from(out as Map);
  }
}

class PluginsApi {
  PluginsApi(this._client);
  final MediaCore _client;

  Future<List<dynamic>> list() async {
    final out = await _client.request('GET', '/v1/plugins');
    return List<dynamic>.from(out as List);
  }
}
