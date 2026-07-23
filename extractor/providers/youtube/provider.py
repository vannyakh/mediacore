from providers.base_stub import StubProvider


class YouTubeProvider(StubProvider):
    name = "youtube"
    host_suffixes = (
        "youtube.com",
        "youtu.be",
        "youtube-nocookie.com",
        "m.youtube.com",
    )
