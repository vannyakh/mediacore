from extractor.providers.base_stub import StubProvider


class PinterestProvider(StubProvider):
    name = "pinterest"
    host_suffixes = ("pinterest.com", "www.pinterest.com", "pin.it")
