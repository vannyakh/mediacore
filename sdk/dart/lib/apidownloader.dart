class VideoExtractor {
  VideoExtractor(this.apiKey, {this.baseUrl = 'http://localhost:8000'});

  final String apiKey;
  final String baseUrl;
}
