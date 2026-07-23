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
        "hosts": ("tiktok.com", "www.tiktok.com", "vm.tiktok.com", "m.tiktok.com"),
        "ie_names": ("TikTok", "tiktok"),
    },
    "instagram": {
        "hosts": ("instagram.com", "www.instagram.com"),
        "ie_names": ("Instagram",),
    },
    "facebook": {
        "hosts": ("facebook.com", "www.facebook.com", "fb.watch", "m.facebook.com", "fb.com"),
        "ie_names": ("Facebook",),
    },
    "twitter": {
        "hosts": ("twitter.com", "www.twitter.com", "x.com", "www.x.com", "mobile.twitter.com"),
        "ie_names": ("twitter", "Twitter"),
    },
    "twitch": {
        "hosts": ("twitch.tv", "www.twitch.tv", "m.twitch.tv", "clips.twitch.tv"),
        "ie_names": ("Twitch", "TwitchVod", "TwitchClips"),
    },
    "bilibili": {
        "hosts": ("bilibili.com", "www.bilibili.com", "b23.tv", "space.bilibili.com"),
        "ie_names": ("BiliBili", "Bilibili"),
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
        "ie_names": ("bbc", "BBC"),
    },
    "cnn": {
        "hosts": ("cnn.com", "www.cnn.com"),
        "ie_names": ("CNN",),
    },
    "espn": {
        "hosts": ("espn.com", "www.espn.com"),
        "ie_names": ("ESPN",),
    },
    "nba": {
        "hosts": ("nba.com", "www.nba.com"),
        "ie_names": ("NBA",),
    },
    "crunchyroll": {
        "hosts": ("crunchyroll.com", "www.crunchyroll.com"),
        "ie_names": ("Crunchyroll",),
    },
    "funimation": {
        "hosts": ("funimation.com", "www.funimation.com"),
        "ie_names": ("Funimation",),
    },
    "afreecatv": {
        "hosts": ("afreecatv.com", "www.afreecatv.com", "vod.afreecatv.com"),
        "ie_names": ("afreecatv",),
    },
    "bitchute": {
        "hosts": ("bitchute.com", "www.bitchute.com"),
        "ie_names": ("BitChute",),
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
    "dropbox": {
        "hosts": ("dropbox.com", "www.dropbox.com", "dl.dropboxusercontent.com"),
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
    "wistia": {
        "hosts": ("wistia.com", "www.wistia.com", "fast.wistia.net"),
        "ie_names": ("Wistia",),
    },
    "brightcove": {
        "hosts": ("brightcove.com", "players.brightcove.net"),
        "ie_names": ("Brightcove",),
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
