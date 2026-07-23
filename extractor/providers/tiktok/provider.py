from providers.base_stub import StubProvider


class TikTokProvider(StubProvider):
    name = "tiktok"
    host_suffixes = ("tiktok.com", "www.tiktok.com", "vm.tiktok.com")
