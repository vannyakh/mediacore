package io.mediacore

/**
 * Future MediaCore Kotlin SDK stub.
 *
 * client.media.analyze / download / convert / thumbnail
 * client.jobs.list / get
 * client.plugins.list
 */
class MediaCore(
    val apiKey: String,
    val baseUrl: String = "http://localhost:8000",
) {
    fun unimplemented(): Nothing =
        error("MediaCore Kotlin SDK is planned. See docs/sdk.md.")
}
