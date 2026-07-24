"""Curated host maps for major platforms (URL detection).

Merged into ``providers/data/providers_index.json`` by
``scripts/generate_providers.py``. Stubs detect platforms; metadata/download
require permitted/official access.
"""

from __future__ import annotations

# name -> hosts + extractor id aliases
MAJOR_PLATFORMS: dict[str, dict] = {
    "youtube": {
        "hosts": (
            "youtube.com",
            "youtu.be",
            "youtube-nocookie.com",
            "m.youtube.com",
            "music.youtube.com",
            "www.youtube.com",
        ),
        "ie_names": ("youtube", "Youtube", "YoutubeTab", "YoutubeClip"),
    },
    "tiktok": {
        "hosts": (
            "tiktok.com",
            "www.tiktok.com",
            "vm.tiktok.com",
            "m.tiktok.com",
            "vt.tiktok.com",
        ),
        "ie_names": ("TikTok", "tiktok"),
    },
    "instagram": {
        "hosts": ("instagram.com", "www.instagram.com"),
        "ie_names": ("Instagram", "instagram:story", "instagram:tag", "instagram:user"),
    },
    "facebook": {
        "hosts": (
            "facebook.com",
            "www.facebook.com",
            "fb.watch",
            "m.facebook.com",
            "fb.com",
            "web.facebook.com",
        ),
        "ie_names": ("Facebook", "facebook", "facebook:ads", "facebook:reel"),
    },
    "twitter": {
        "hosts": ("twitter.com", "www.twitter.com", "x.com", "www.x.com", "mobile.twitter.com"),
        "ie_names": ("twitter", "Twitter"),
    },
    "twitch": {
        "hosts": ("twitch.tv", "www.twitch.tv", "m.twitch.tv", "clips.twitch.tv", "go.twitch.tv"),
        "ie_names": ("Twitch", "TwitchVod", "TwitchClips"),
    },
    "applepodcasts": {
        "hosts": ("podcasts.apple.com", "itunes.apple.com"),
        "ie_names": ("ApplePodcasts", "apple:podcasts"),
    },
    "flickr": {
        "hosts": ("flickr.com", "www.flickr.com", "secure.flickr.com"),
        "ie_names": ("Flickr",),
    },
    "slideshare": {
        "hosts": ("slideshare.net", "www.slideshare.net"),
        "ie_names": ("Slideshare",),
    },
    "tumblr": {
        "hosts": ("tumblr.com", "www.tumblr.com"),
        "ie_names": ("Tumblr",),
    },
    "bilibili": {
        "hosts": (
            "bilibili.com",
            "www.bilibili.com",
            "b23.tv",
            "space.bilibili.com",
            "player.bilibili.com",
            "live.bilibili.com",
            "bilibili.tv",
            "www.bilibili.tv",
        ),
        "ie_names": ("BiliBili", "Bilibili", "bilibili"),
    },
    "aol.com": {
        "hosts": ("aol.com", "www.aol.com", "aol.ca", "aol.co.uk", "aol.de", "aol.jp"),
        "ie_names": ("aol.com",),
    },
    "arte.sky.it": {
        "hosts": ("arte.sky.it",),
        "ie_names": ("arte.sky.it",),
    },
    "pinterest": {
        "hosts": ("pinterest.com", "www.pinterest.com", "pin.it"),
        "ie_names": ("Pinterest",),
    },
    "dailymotion": {
        "hosts": ("dailymotion.com", "www.dailymotion.com", "dai.ly"),
        "ie_names": ("Dailymotion",),
    },
    "soundcloud": {
        "hosts": ("soundcloud.com", "www.soundcloud.com", "m.soundcloud.com"),
        "ie_names": ("Soundcloud",),
    },
    "reddit": {
        "hosts": ("reddit.com", "www.reddit.com", "old.reddit.com", "v.redd.it", "i.redd.it"),
        "ie_names": ("Reddit",),
    },
    "rumble": {
        "hosts": ("rumble.com", "www.rumble.com"),
        "ie_names": ("Rumble",),
    },
    "kick": {
        "hosts": ("kick.com", "www.kick.com"),
        "ie_names": ("Kick",),
    },
    "linkedin": {
        "hosts": ("linkedin.com", "www.linkedin.com"),
        "ie_names": ("linkedin", "LinkedIn"),
    },
    "threads": {
        "hosts": ("threads.net", "www.threads.net"),
        "ie_names": ("Threads",),
    },
    "snapchat": {
        "hosts": ("snapchat.com", "www.snapchat.com", "story.snapchat.com"),
        "ie_names": ("Snapchat",),
    },
    "bandcamp": {
        "hosts": ("bandcamp.com",),
        "ie_names": ("Bandcamp",),
    },
    "mixcloud": {
        "hosts": ("mixcloud.com", "www.mixcloud.com"),
        "ie_names": ("Mixcloud",),
    },
    "archiveorg": {
        "hosts": ("archive.org", "www.archive.org"),
        "ie_names": ("archive.org", "ArchiveOrg"),
    },
    # Movie / trailer platforms — PlatformModule hosts for URL detection +
    # direct-media download; page/watch URLs stay not_configured until a
    # permitted/official API is wired (no scrapers).
    "imdb": {
        "hosts": ("imdb.com", "www.imdb.com", "m.imdb.com"),
        "ie_names": ("imdb", "imdb:list"),
    },
    "moviepilot": {
        "hosts": ("moviepilot.de", "www.moviepilot.de"),
        "ie_names": ("moviepilot",),
    },
    "rottentomatoes": {
        "hosts": ("rottentomatoes.com", "www.rottentomatoes.com"),
        "ie_names": ("RottenTomatoes",),
    },
    "niconico": {
        "hosts": ("nicovideo.jp", "www.nicovideo.jp", "nico.ms"),
        "ie_names": ("Niconico",),
    },
    "youku": {
        "hosts": ("youku.com", "v.youku.com", "www.youku.com"),
        "ie_names": ("youku",),
    },
    "iqiyi": {
        "hosts": ("iqiyi.com", "www.iqiyi.com"),
        "ie_names": ("iqiyi",),
    },
    "streamable": {
        "hosts": ("streamable.com", "www.streamable.com"),
        "ie_names": ("Streamable",),
    },
    "imgur": {
        "hosts": ("imgur.com", "i.imgur.com", "www.imgur.com"),
        "ie_names": ("Imgur",),
    },
    "ted": {
        "hosts": ("ted.com", "www.ted.com"),
        "ie_names": ("TED",),
    },
    "bbc": {
        "hosts": ("bbc.co.uk", "www.bbc.co.uk", "bbc.com", "www.bbc.com"),
        "ie_names": (
            "bbc",
            "BBC",
            "bbc.co.uk",
            "bbc.co.uk:article",
            "bbc.co.uk:iplayer:episodes",
            "bbc.co.uk:iplayer:group",
            "bbc.co.uk:playlist",
        ),
    },
    "cnn": {
        "hosts": (
            "cnn.com",
            "www.cnn.com",
            "edition.cnn.com",
            "money.cnn.com",
            "cnnespanol.cnn.com",
        ),
        "ie_names": ("CNN", "cnn"),
    },
    "cielotv.it": {
        "hosts": ("cielotv.it", "www.cielotv.it"),
        "ie_names": ("cielotv.it",),
    },
    "croatian.film": {
        "hosts": ("croatian.film", "www.croatian.film"),
        "ie_names": ("croatian.film",),
    },
    "cu.ntv.co.jp": {
        "hosts": ("cu.ntv.co.jp",),
        "ie_names": ("cu.ntv.co.jp",),
    },
    "espn": {
        "hosts": ("espn.com", "www.espn.com"),
        "ie_names": ("ESPN",),
    },
    "faz.net": {
        "hosts": ("faz.net", "www.faz.net"),
        "ie_names": ("faz.net", "FAZ"),
    },
    "freespeech.org": {
        "hosts": ("freespeech.org", "www.freespeech.org"),
        "ie_names": ("freespeech.org",),
    },
    "nba": {
        "hosts": ("nba.com", "www.nba.com"),
        "ie_names": ("NBA",),
    },
    "crunchyroll": {
        "hosts": ("crunchyroll.com", "www.crunchyroll.com"),
        "ie_names": ("Crunchyroll", "crunchyroll"),
    },
    "funimation": {
        "hosts": ("funimation.com", "www.funimation.com"),
        "ie_names": ("Funimation",),
    },
    "afreecatv": {
        # Rebranded to Soop; keep legacy afreecatv hosts (redirect) + sooplive.
        "hosts": (
            "afreecatv.com",
            "www.afreecatv.com",
            "vod.afreecatv.com",
            "sooplive.com",
            "www.sooplive.com",
            "vod.sooplive.com",
            "play.sooplive.com",
        ),
        "ie_names": ("afreecatv", "soop", "soop:live", "soop:user", "soop:catchstory"),
    },
    "24tv.ua": {
        "hosts": ("24tv.ua", "www.24tv.ua"),
        "ie_names": ("24tv.ua",),
    },
    "56.com": {
        "hosts": ("56.com", "www.56.com", "player.56.com"),
        "ie_names": ("56.com",),
    },
    "9now.com.au": {
        "hosts": ("9now.com.au", "www.9now.com.au"),
        "ie_names": ("9now.com.au",),
    },
    "abc.net.au": {
        "hosts": ("abc.net.au", "www.abc.net.au", "iview.abc.net.au"),
        "ie_names": ("abc.net.au", "abc.net.au:iview", "abc.net.au:iview:showseries"),
    },
    "bitchute": {
        "hosts": ("bitchute.com", "www.bitchute.com", "old.bitchute.com"),
        "ie_names": ("BitChute", "bitchute"),
    },
    "blogger.com": {
        "hosts": ("blogger.com", "www.blogger.com"),
        "ie_names": ("blogger.com",),
    },
    "canalc2.tv": {
        "hosts": ("canalc2.tv", "www.canalc2.tv", "archives-canalc2.u-strasbg.fr"),
        "ie_names": ("canalc2.tv",),
    },
    "cbc.ca": {
        "hosts": ("cbc.ca", "www.cbc.ca", "gem.cbc.ca"),
        "ie_names": (
            "cbc.ca",
            "cbc.ca:player",
            "cbc.ca:player:playlist",
            "cbc.ca:listen",
            "gem.cbc.ca",
            "gem.cbc.ca:playlist",
            "gem.cbc.ca:live",
        ),
    },
    "odysee": {
        "hosts": ("odysee.com", "www.odysee.com"),
        "ie_names": ("Odysee", "lbry"),
    },
    "peertube": {
        "hosts": (),  # federated — many domains; catalog-only until configured
        "ie_names": ("PeerTube",),
    },
    "vk": {
        "hosts": ("vk.com", "vk.ru", "vkvideo.ru"),
        "ie_names": ("VK",),
    },
    "okru": {
        "hosts": ("ok.ru", "www.ok.ru"),
        "ie_names": ("Odnoklassniki",),
    },
    "rutube": {
        "hosts": ("rutube.ru", "www.rutube.ru"),
        "ie_names": ("Rutube",),
    },
    "weibo": {
        "hosts": ("weibo.com", "www.weibo.com", "video.weibo.com"),
        "ie_names": ("Weibo",),
    },
    "xiaohongshu": {
        "hosts": ("xiaohongshu.com", "www.xiaohongshu.com", "xhslink.com"),
        "ie_names": ("XiaoHongShu",),
    },
    "douyin": {
        "hosts": ("douyin.com", "www.douyin.com", "v.douyin.com"),
        "ie_names": ("Douyin",),
    },
    "kuaishou": {
        "hosts": ("kuaishou.com", "www.kuaishou.com", "v.kuaishou.com"),
        "ie_names": ("Kuaishou",),
    },
    "pornhub": {
        "hosts": ("pornhub.com", "www.pornhub.com"),
        "ie_names": ("PornHub",),
    },
    "xvideos": {
        "hosts": ("xvideos.com", "www.xvideos.com"),
        "ie_names": ("XVideos",),
    },
    "xhamster": {
        "hosts": ("xhamster.com", "www.xhamster.com"),
        "ie_names": ("XHamster",),
    },
    "ninegag": {
        "hosts": ("9gag.com", "www.9gag.com"),
        "ie_names": ("9gag",),
    },
    "imgur_album": {
        "hosts": (),
        "ie_names": ("imgur:album",),
    },
    "google_drive": {
        "hosts": ("drive.google.com", "docs.google.com"),
        "ie_names": ("GoogleDrive",),
    },
    "daum.net": {
        "hosts": ("daum.net", "www.daum.net", "tv.kakao.com", "kakaotv.daum.net"),
        "ie_names": ("daum.net", "Daum", "Kakao"),
    },
    "dzen.ru": {
        "hosts": ("dzen.ru", "www.dzen.ru", "zen.yandex.ru"),
        "ie_names": ("dzen.ru", "Dzen", "ZenYandex"),
    },
    "dropbox": {
        "hosts": (
            "dropbox.com",
            "www.dropbox.com",
            "dl.dropbox.com",
            "dl.dropboxusercontent.com",
        ),
        "ie_names": ("Dropbox",),
    },
    "mega": {
        "hosts": ("mega.nz", "mega.co.nz"),
        "ie_names": ("MEGA",),
    },
    "zoom": {
        "hosts": ("zoom.us", "www.zoom.us"),
        "ie_names": ("Zoom",),
    },
    "loom": {
        "hosts": ("loom.com", "www.loom.com"),
        "ie_names": ("Loom",),
    },
    "media.ccc.de": {
        "hosts": ("media.ccc.de", "api.media.ccc.de"),
        "ie_names": ("media.ccc.de", "CCC"),
    },
    "wistia": {
        "hosts": ("wistia.com", "www.wistia.com", "fast.wistia.net"),
        "ie_names": ("Wistia",),
    },
    "brightcove": {
        "hosts": ("brightcove.com", "players.brightcove.net"),
        "ie_names": ("Brightcove",),
    },
    "hgtv.com": {
        "hosts": ("hgtv.com", "www.hgtv.com"),
        "ie_names": ("hgtv.com",),
    },
    "ign.com": {
        "hosts": ("ign.com", "www.ign.com"),
        "ie_names": ("ign.com", "IGN"),
    },
    "iq.com": {
        "hosts": ("iq.com", "www.iq.com"),
        "ie_names": ("iq.com",),
    },
    "jwplatform": {
        "hosts": ("jwplatform.com", "cdn.jwplayer.com"),
        "ie_names": ("JWPlatform",),
    },
    "vimeo_platform": {
        # covered by dedicated VimeoProvider; listed for catalog parity
        "hosts": (),
        "ie_names": ("vimeo", "Vimeo"),
    },
}
