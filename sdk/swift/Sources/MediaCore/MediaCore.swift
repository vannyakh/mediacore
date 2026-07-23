/// Future MediaCore Swift SDK stub.
///
/// client.media.analyze / download / convert / thumbnail
/// client.jobs.list / get
/// client.plugins.list
public struct MediaCore {
    public let apiKey: String
    public let baseURL: String

    public init(apiKey: String, baseURL: String = "http://localhost:8000") {
        self.apiKey = apiKey
        self.baseURL = baseURL
    }

    public func unimplemented() -> Never {
        fatalError("MediaCore Swift SDK is planned. See docs/sdk.md.")
    }
}
