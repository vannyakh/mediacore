from pathlib import Path
from unittest.mock import patch

import pytest

from packages.testkit.contracts import run_provider_contract
from providers.abc_net_au.provider import AbcNetAuProvider
from providers.applepodcasts.provider import ApplepodcastsProvider
from providers.archiveorg.provider import ArchiveorgProvider
from providers.bandcamp.provider import BandcampProvider
from providers.bbc.provider import BbcProvider
from providers.bilibili.provider import BilibiliProvider
from providers.bitchute.provider import BitchuteProvider
from providers.dailymotion.provider import DailymotionProvider
from providers.example.provider import ExampleProvider
from providers.filesystem.provider import FilesystemProvider
from providers.flickr.provider import FlickrProvider
from providers.generic.provider import GenericHTTPProvider
from providers.imgur.provider import ImgurProvider
from providers.mixcloud.provider import MixcloudProvider
from providers.reddit.provider import RedditProvider
from providers.soundcloud.provider import SoundcloudProvider
from providers.streamable.provider import StreamableProvider
from providers.ted.provider import TedProvider
from providers.tiktok.provider import TiktokProvider
from providers.vimeo.provider import VimeoProvider
from providers.wikimedia.provider import WikimediaProvider
from providers.youtube.provider import YoutubeProvider

pytestmark = pytest.mark.provider


def test_generic_contract(tmp_path: Path):
    provider = GenericHTTPProvider()
    url = "https://cdn.example.com/demo.mp4"
    with (
        patch("providers.direct_media.head_content_type", return_value="video/mp4"),
        patch("providers.direct_media.download_file", return_value=(4, "video/mp4")),
    ):
        run_provider_contract(provider, url, tmp_path / "out.mp4", expect_download=True)


def test_filesystem_contract(tmp_path: Path):
    src = tmp_path / "local.mp4"
    src.write_bytes(b"local-bytes")
    provider = FilesystemProvider()
    run_provider_contract(provider, src.as_uri(), tmp_path / "copied.mp4", expect_download=True)


def test_example_contract_metadata_only(tmp_path: Path):
    provider = ExampleProvider()
    run_provider_contract(
        provider,
        "mediacore://example/demo",
        tmp_path / "out.mp4",
        expect_download=False,
    )


def _run_oembed_contract(provider, url: str, dest: Path, fake: dict | None = None):
    payload = fake or {
        "title": "Public Clip",
        "duration": 10,
        "thumbnail_url": "https://example.com/t.jpg",
        "author_name": "Author",
        "provider_url": "https://example.com/",
        "html": "<iframe></iframe>",
    }
    with patch("providers.oembed.httpx.Client") as client_cls:
        client = client_cls.return_value.__enter__.return_value
        response = client.get.return_value
        response.status_code = 200
        response.raise_for_status.return_value = None
        response.json.return_value = payload
        run_provider_contract(provider, url, dest, expect_download=False)


def test_youtube_contract_metadata_only(tmp_path: Path):
    _run_oembed_contract(
        YoutubeProvider(),
        "https://www.youtube.com/watch?v=jNQXAC9IVRw",
        tmp_path / "out.mp4",
        fake={
            "title": "Me at the zoo",
            "author_name": "jawed",
            "thumbnail_url": "https://example.com/t.jpg",
            "provider_url": "https://www.youtube.com/",
            "html": "<iframe></iframe>",
            "type": "video",
        },
    )


def test_tiktok_contract_metadata_only(tmp_path: Path):
    _run_oembed_contract(
        TiktokProvider(),
        "https://www.tiktok.com/@scout2015/video/6718335390845095173",
        tmp_path / "out.mp4",
        fake={
            "title": "Sample TikTok",
            "author_name": "scout2015",
            "author_url": "https://www.tiktok.com/@scout2015",
            "thumbnail_url": "https://example.com/t.jpg",
            "provider_url": "https://www.tiktok.com",
            "html": "<blockquote></blockquote>",
            "type": "video",
        },
    )


def test_vimeo_contract_metadata_only(tmp_path: Path):
    _run_oembed_contract(
        VimeoProvider(),
        "https://vimeo.com/123456789",
        tmp_path / "out.mp4",
    )


def test_dailymotion_contract_metadata_only(tmp_path: Path):
    _run_oembed_contract(
        DailymotionProvider(),
        "https://www.dailymotion.com/video/x123abc",
        tmp_path / "out.mp4",
    )


def test_soundcloud_contract_metadata_only(tmp_path: Path):
    _run_oembed_contract(
        SoundcloudProvider(),
        "https://soundcloud.com/artist/track",
        tmp_path / "out.mp4",
    )


def test_reddit_contract_metadata_only(tmp_path: Path):
    _run_oembed_contract(
        RedditProvider(),
        "https://www.reddit.com/r/videos/comments/abc/title/",
        tmp_path / "out.mp4",
    )


def test_ted_contract_metadata_only(tmp_path: Path):
    _run_oembed_contract(
        TedProvider(),
        "https://www.ted.com/talks/example_talk",
        tmp_path / "out.mp4",
    )


def test_wikimedia_contract_metadata_only(tmp_path: Path):
    provider = WikimediaProvider()
    fake = {
        "title": "Example.jpg",
        "displaytitle": "Example.jpg",
        "extract": "A sample file on Commons.",
        "thumbnail": {"source": "https://upload.wikimedia.org/t.jpg"},
        "type": "standard",
        "lang": "en",
    }
    with patch("providers.wikimedia.provider.httpx.Client") as client_cls:
        client = client_cls.return_value.__enter__.return_value
        response = client.get.return_value
        response.status_code = 200
        response.raise_for_status.return_value = None
        response.json.return_value = fake
        run_provider_contract(
            provider,
            "https://commons.wikimedia.org/wiki/File:Example.jpg",
            tmp_path / "out.mp4",
            expect_download=False,
        )


def test_bandcamp_contract_metadata_only(tmp_path: Path):
    _run_oembed_contract(
        BandcampProvider(),
        "https://artist.bandcamp.com/track/example",
        tmp_path / "out.mp4",
    )


def test_mixcloud_contract_metadata_only(tmp_path: Path):
    _run_oembed_contract(
        MixcloudProvider(),
        "https://www.mixcloud.com/artist/show/",
        tmp_path / "out.mp4",
    )


def test_streamable_contract_metadata_only(tmp_path: Path):
    _run_oembed_contract(
        StreamableProvider(),
        "https://streamable.com/abcd",
        tmp_path / "out.mp4",
    )


def test_imgur_contract_metadata_only(tmp_path: Path):
    _run_oembed_contract(
        ImgurProvider(),
        "https://imgur.com/gallery/abc",
        tmp_path / "out.mp4",
    )


def test_archiveorg_contract_metadata_only(tmp_path: Path):
    _run_oembed_contract(
        ArchiveorgProvider(),
        "https://archive.org/details/example",
        tmp_path / "out.mp4",
    )


def test_flickr_contract_metadata_only(tmp_path: Path):
    _run_oembed_contract(
        FlickrProvider(),
        "https://www.flickr.com/photos/flickr/4459660154",
        tmp_path / "out.mp4",
        fake={
            "title": "Sample photo",
            "thumbnail_url": "https://example.com/t.jpg",
            "author_name": "Author",
            "provider_url": "https://www.flickr.com/",
            "type": "photo",
            "url": "https://example.com/photo.jpg",
        },
    )


def test_applepodcasts_contract_metadata_only(tmp_path: Path):
    provider = ApplepodcastsProvider()
    fake = {
        "resultCount": 1,
        "results": [
            {
                "kind": "podcast",
                "trackName": "The Daily",
                "artistName": "The New York Times",
                "collectionName": "The Daily",
                "artworkUrl600": "https://example.com/art.jpg",
                "description": "News podcast",
                "collectionId": 1200361736,
                "trackId": 1200361736,
                "feedUrl": "https://example.com/feed.xml",
            }
        ],
    }
    with patch("providers.applepodcasts.provider.httpx.Client") as client_cls:
        client = client_cls.return_value.__enter__.return_value
        response = client.get.return_value
        response.status_code = 200
        response.raise_for_status.return_value = None
        response.json.return_value = fake
        run_provider_contract(
            provider,
            "https://podcasts.apple.com/us/podcast/the-daily/id1200361736",
            tmp_path / "out.mp4",
            expect_download=False,
        )


def test_abc_net_au_contract_metadata_only(tmp_path: Path):
    provider = AbcNetAuProvider()
    fake = {
        "id": 123450,
        "slug": "abc-news",
        "type": "series",
        "title": "ABC News",
        "displayTitle": "ABC News",
        "description": "News series",
        "thumbnail": "https://example.com/t.jpg",
        "shareUrl": "https://iview.abc.net.au/show/abc-news",
        "requiresLogin": False,
    }
    with patch("providers.abc_net_au.provider.httpx.Client") as client_cls:
        client = client_cls.return_value.__enter__.return_value
        response = client.get.return_value
        response.status_code = 200
        response.raise_for_status.return_value = None
        response.json.return_value = fake
        run_provider_contract(
            provider,
            "https://iview.abc.net.au/show/abc-news",
            tmp_path / "out.mp4",
            expect_download=False,
        )


def test_bbc_contract_metadata_only(tmp_path: Path):
    provider = BbcProvider()
    fake = {
        "programme": {
            "pid": "b006q2x0",
            "type": "brand",
            "title": "Doctor Who",
            "short_synopsis": "Adventures in Space and Time.",
            "image": {"pid": "p0gpxrx6"},
            "ownership": {"service": {"title": "BBC One"}},
        }
    }
    with patch("providers.bbc.provider.httpx.Client") as client_cls:
        client = client_cls.return_value.__enter__.return_value
        response = client.get.return_value
        response.status_code = 200
        response.raise_for_status.return_value = None
        response.json.return_value = fake
        run_provider_contract(
            provider,
            "https://www.bbc.co.uk/programmes/b006q2x0",
            tmp_path / "out.mp4",
            expect_download=False,
        )


def test_bilibili_contract_metadata_only(tmp_path: Path):
    provider = BilibiliProvider()
    fake = {
        "code": 0,
        "message": "OK",
        "data": {
            "bvid": "BV1xx411c7mD",
            "aid": 2,
            "title": "Sample",
            "desc": "Description",
            "pic": "https://example.com/p.jpg",
            "duration": 120,
            "owner": {"name": "Uploader"},
            "cid": 1,
        },
    }
    with patch("providers.bilibili.provider.httpx.Client") as client_cls:
        client = client_cls.return_value.__enter__.return_value
        response = client.get.return_value
        response.status_code = 200
        response.raise_for_status.return_value = None
        response.json.return_value = fake
        run_provider_contract(
            provider,
            "https://www.bilibili.com/video/BV1xx411c7mD",
            tmp_path / "out.mp4",
            expect_download=False,
        )


def test_bitchute_contract_metadata_only(tmp_path: Path):
    provider = BitchuteProvider()
    fake = {
        "video_id": "2s6B3nZjAk7R",
        "video_name": "Sample video",
        "description": "A description",
        "duration": "1:30",
        "thumbnail_url": "https://example.com/t.jpg",
        "channel": {"channel_name": "Channel"},
        "view_count": 10,
        "date_published": "2018-11-13T17:31:27Z",
    }
    with patch("providers.bitchute.provider.httpx.Client") as client_cls:
        client = client_cls.return_value.__enter__.return_value
        response = client.post.return_value
        response.status_code = 200
        response.raise_for_status.return_value = None
        response.json.return_value = fake
        run_provider_contract(
            provider,
            "https://www.bitchute.com/video/2s6B3nZjAk7R/",
            tmp_path / "out.mp4",
            expect_download=False,
        )


def test_oembed_providers_override_catalog_modules():
    from packages.registry.providers import reset_registry

    registry = reset_registry()
    for name in (
        "youtube",
        "tiktok",
        "dailymotion",
        "soundcloud",
        "reddit",
        "ted",
        "wikimedia.org",
        "vimeo",
        "bandcamp",
        "mixcloud",
        "streamable",
        "imgur",
        "archiveorg",
        "flickr",
        "applepodcasts",
        "abc.net.au",
        "bbc",
        "bilibili",
        "bitchute",
    ):
        provider = registry.get(name)
        assert provider is not None
        assert getattr(provider, "status", None) == "metadata_only"
        assert getattr(provider, "source", None) != "catalog"
