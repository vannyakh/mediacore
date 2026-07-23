from extractor.providers.base_stub import StubProvider


class FacebookProvider(StubProvider):
    name = "facebook"
    host_suffixes = ("facebook.com", "fb.watch", "fb.com", "m.facebook.com")
