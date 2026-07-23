"""Platform provider helpers."""

__all__ = ["build_all_providers"]


def __getattr__(name: str):
    if name == "build_all_providers":
        from providers.platforms.factory import build_all_providers

        return build_all_providers
    raise AttributeError(name)
