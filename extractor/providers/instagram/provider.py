from extractor.providers.base_stub import StubProvider


class InstagramProvider(StubProvider):
    name = "instagram"
    host_suffixes = ("instagram.com", "www.instagram.com")
