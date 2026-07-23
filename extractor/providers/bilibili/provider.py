from extractor.providers.base_stub import StubProvider


class BilibiliProvider(StubProvider):
    name = "bilibili"
    host_suffixes = ("bilibili.com", "www.bilibili.com", "b23.tv")
