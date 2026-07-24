<script setup lang="ts">
import { computed, onMounted, ref } from "vue";

type CatalogRow = {
  name: string;
  status: string;
  hosts: string[];
  description: string;
  logo?: string | null;
};

/** Prefer Simple Icons brand marks when the slug is known; else host favicon CDN. */
const SIMPLE_ICON_SLUGS: Record<string, string> = {
  youtube: "youtube",
  tiktok: "tiktok",
  instagram: "instagram",
  facebook: "facebook",
  twitter: "x",
  x: "x",
  twitch: "twitch",
  bilibili: "bilibili",
  pinterest: "pinterest",
  dailymotion: "dailymotion",
  soundcloud: "soundcloud",
  reddit: "reddit",
  rumble: "rumble",
  kick: "kick",
  linkedin: "linkedin",
  threads: "threads",
  snapchat: "snapchat",
  vimeo: "vimeo",
  netflix: "netflix",
  spotify: "spotify",
  discord: "discord",
  telegram: "telegram",
  whatsapp: "whatsapp",
  tumblr: "tumblr",
  flickr: "flickr",
  medium: "medium",
  github: "github",
  patreon: "patreon",
  bandcamp: "bandcamp",
  mixcloud: "mixcloud",
  streamable: "streamable",
  imgur: "imgur",
  archiveorg: "internetarchive",
  "internet archive": "internetarchive",
  applepodcasts: "applepodcasts",
  "abc.net.au": "abc",
  abc: "abc",
  bbc: "bbc",
  bilibili: "bilibili",
  bitchute: "bitchute",
  dropbox: "dropbox",
  google_drive: "googledrive",
  "google drive": "googledrive",
  ted: "ted",
  "wikimedia.org": "wikimedia",
  wikimedia: "wikimedia",
  apple: "apple",
  amazon: "amazon",
  google: "google",
  microsoft: "microsoft",
};

const WORKING: CatalogRow[] = [
  {
    name: "filesystem",
    status: "available",
    hosts: [],
    description: "Local files you already have (file://, absolute paths).",
    logo: "https://cdn.simpleicons.org/files/0ea5e9",
  },
  {
    name: "generic",
    status: "available",
    hosts: [],
    description: "Direct HTTP(S) media (.mp4/.m3u8/…).",
    logo: "https://cdn.simpleicons.org/http/0ea5e9",
  },
  {
    name: "example",
    status: "available",
    hosts: [],
    description: "Demo provider for tests/docs (mediacore://example/).",
    logo: "/logo.png",
  },
  {
    name: "youtube",
    status: "metadata_only",
    hosts: ["youtube.com", "youtu.be"],
    description: "Public oEmbed metadata only.",
    logo: "https://cdn.simpleicons.org/youtube",
  },
  {
    name: "tiktok",
    status: "metadata_only",
    hosts: ["tiktok.com", "vm.tiktok.com"],
    description: "Public oEmbed metadata only.",
    logo: "https://cdn.simpleicons.org/tiktok",
  },
  {
    name: "vimeo",
    status: "metadata_only",
    hosts: ["vimeo.com"],
    description: "Public oEmbed metadata only.",
    logo: "https://cdn.simpleicons.org/vimeo/1AB7EA",
  },
  {
    name: "dailymotion",
    status: "metadata_only",
    hosts: ["dailymotion.com", "dai.ly"],
    description: "Public oEmbed metadata only.",
    logo: "https://cdn.simpleicons.org/dailymotion",
  },
  {
    name: "soundcloud",
    status: "metadata_only",
    hosts: ["soundcloud.com"],
    description: "Public oEmbed metadata only.",
    logo: "https://cdn.simpleicons.org/soundcloud",
  },
  {
    name: "reddit",
    status: "metadata_only",
    hosts: ["reddit.com", "v.redd.it"],
    description: "Public oEmbed metadata only.",
    logo: "https://cdn.simpleicons.org/reddit",
  },
  {
    name: "ted",
    status: "metadata_only",
    hosts: ["ted.com"],
    description: "Public oEmbed metadata only.",
    logo: "https://cdn.simpleicons.org/ted",
  },
  {
    name: "wikimedia.org",
    status: "metadata_only",
    hosts: ["wikimedia.org", "commons.wikimedia.org"],
    description: "MediaWiki REST summary metadata.",
    logo: "https://cdn.simpleicons.org/wikimedia",
  },
  {
    name: "bandcamp",
    status: "metadata_only",
    hosts: ["bandcamp.com"],
    description: "Public oEmbed metadata only.",
    logo: "https://cdn.simpleicons.org/bandcamp",
  },
  {
    name: "mixcloud",
    status: "metadata_only",
    hosts: ["mixcloud.com"],
    description: "Public oEmbed metadata only.",
    logo: "https://cdn.simpleicons.org/mixcloud",
  },
  {
    name: "streamable",
    status: "metadata_only",
    hosts: ["streamable.com"],
    description: "Public oEmbed metadata only.",
  },
  {
    name: "imgur",
    status: "metadata_only",
    hosts: ["imgur.com", "i.imgur.com"],
    description: "Public oEmbed metadata only.",
    logo: "https://cdn.simpleicons.org/imgur",
  },
  {
    name: "archiveorg",
    status: "metadata_only",
    hosts: ["archive.org"],
    description: "Public oEmbed metadata only.",
    logo: "https://cdn.simpleicons.org/internetarchive",
  },
  {
    name: "flickr",
    status: "metadata_only",
    hosts: ["flickr.com"],
    description: "Public oEmbed metadata only.",
    logo: "https://cdn.simpleicons.org/flickr",
  },
  {
    name: "applepodcasts",
    status: "metadata_only",
    hosts: ["podcasts.apple.com"],
    description: "Public iTunes Lookup metadata only.",
    logo: "https://cdn.simpleicons.org/applepodcasts",
  },
  {
    name: "abc.net.au",
    status: "metadata_only",
    hosts: ["abc.net.au", "iview.abc.net.au"],
    description: "Public iView catalog metadata (show pages).",
    logo: "https://cdn.simpleicons.org/abc",
  },
  {
    name: "bbc",
    status: "metadata_only",
    hosts: ["bbc.co.uk", "bbc.com"],
    description: "Public programmes JSON metadata (/programmes/{pid}).",
    logo: "https://cdn.simpleicons.org/bbc",
  },
  {
    name: "bilibili",
    status: "metadata_only",
    hosts: ["bilibili.com", "b23.tv"],
    description: "Public web view API metadata (BV/av).",
    logo: "https://cdn.simpleicons.org/bilibili",
  },
  {
    name: "bitchute",
    status: "metadata_only",
    hosts: ["bitchute.com"],
    description: "Public beta video API metadata.",
    logo: "https://cdn.simpleicons.org/bitchute",
  },
  {
    name: "dropbox",
    status: "available",
    hosts: ["dropbox.com", "dl.dropboxusercontent.com"],
    description: "Shared file links via official dl=1 download parameter.",
    logo: "https://cdn.simpleicons.org/dropbox",
  },
  {
    name: "google_drive",
    status: "available",
    hosts: ["drive.google.com", "docs.google.com"],
    description: "Public file shares via uc?export=download.",
    logo: "https://cdn.simpleicons.org/googledrive",
  },
  {
    name: "media.ccc.de",
    status: "available",
    hosts: ["media.ccc.de"],
    description: "Public JSON API with direct recording downloads.",
    logo: "https://cdn.simpleicons.org/ccc",
  },
];

const rows = ref<CatalogRow[]>([]);
const loading = ref(true);
const error = ref("");
const query = ref("");
const statusFilter = ref<"all" | "available" | "not_configured" | "broken" | "hosts">("all");
const page = ref(1);
const pageSize = 50;
const brokenLogos = ref<Record<string, number>>({});

onMounted(async () => {
  try {
    const res = await fetch("/platforms.json");
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    const catalog: CatalogRow[] = data.providers || [];
    const seen = new Set(WORKING.map((w) => w.name.toLowerCase()));
    const rest = catalog.filter((r) => !seen.has(r.name.toLowerCase()));
    rows.value = [...WORKING, ...rest];
  } catch (e) {
    error.value = e instanceof Error ? e.message : "Failed to load catalog";
  } finally {
    loading.value = false;
  }
});

const filtered = computed(() => {
  const q = query.value.trim().toLowerCase();
  return rows.value.filter((r) => {
    if (statusFilter.value === "hosts" && !(r.hosts && r.hosts.length)) return false;
    if (statusFilter.value === "broken" && r.status !== "broken") return false;
    const workingStatuses = ["available", "active", "metadata", "metadata_only"];
    if (statusFilter.value === "available" && !workingStatuses.includes(r.status)) return false;
    if (statusFilter.value === "not_configured" && r.status === "broken") return false;
    if (statusFilter.value === "not_configured" && workingStatuses.includes(r.status)) return false;
    if (!q) return true;
    const hay = [r.name, r.description, ...(r.hosts || [])].join(" ").toLowerCase();
    return hay.includes(q);
  });
});

const pageCount = computed(() => Math.max(1, Math.ceil(filtered.value.length / pageSize)));

const pageRows = computed(() => {
  const start = (page.value - 1) * pageSize;
  return filtered.value.slice(start, start + pageSize);
});

function badgeClass(status: string): string {
  if (status === "available" || status === "active") return "available";
  if (status === "metadata" || status === "metadata_only") return "kind";
  if (status === "broken") return "broken";
  return "stub";
}

function displayStatus(status: string): string {
  if (status === "not_configured") return "stub";
  return status;
}

function onQuery() {
  page.value = 1;
}

function primaryHost(hosts: string[] | undefined): string | null {
  for (const raw of hosts || []) {
    let h = raw.trim().toLowerCase();
    if (h.startsWith("www.")) h = h.slice(4);
    if (h.includes(".") && !h.includes(" ")) return h;
  }
  return null;
}

function logoCandidates(name: string, hosts?: string[], preferred?: string | null): string[] {
  const out: string[] = [];
  const key = name.toLowerCase();
  const simple = SIMPLE_ICON_SLUGS[key];
  if (simple) out.push(`https://cdn.simpleicons.org/${simple}`);
  if (preferred) out.push(preferred);
  const host = primaryHost(hosts);
  if (host) {
    out.push(`https://www.google.com/s2/favicons?domain=${encodeURIComponent(host)}&sz=128`);
    out.push(`https://icons.duckduckgo.com/ip3/${encodeURIComponent(host)}.ico`);
  }
  const slug = key.replace(/[^a-z0-9]/g, "");
  if (slug) out.push(`https://cdn.simpleicons.org/${slug}`);
  return [...new Set(out)];
}

function logoSrc(name: string, hosts?: string[], preferred?: string | null): string | null {
  const list = logoCandidates(name, hosts, preferred);
  const failed = Number(brokenLogos.value[name] || 0);
  return list[failed] || null;
}

function onLogoError(name: string, hosts?: string[], preferred?: string | null) {
  const list = logoCandidates(name, hosts, preferred);
  const failed = Number(brokenLogos.value[name] || 0);
  if (failed + 1 < list.length) {
    brokenLogos.value = { ...brokenLogos.value, [name]: failed + 1 };
  } else {
    brokenLogos.value = { ...brokenLogos.value, [name]: list.length };
  }
}

function showLetter(name: string, hosts?: string[], preferred?: string | null): boolean {
  const list = logoCandidates(name, hosts, preferred);
  const failed = Number(brokenLogos.value[name] || 0);
  return failed >= list.length || list.length === 0;
}

function initial(name: string): string {
  return (name || "?").slice(0, 1).toUpperCase();
}
</script>

<template>
  <div class="mc-platforms">
    <p class="mc-lead" style="margin-bottom: 0.85rem">
      <template v-if="loading">Loading catalog…</template>
      <template v-else-if="error">Could not load <code>/platforms.json</code>: {{ error }}</template>
      <template v-else>
        {{ filtered.length.toLocaleString() }} platform{{ filtered.length === 1 ? "" : "s" }}
      </template>
    </p>

    <div class="mc-toolbar" v-if="!loading && !error">
      <input
        v-model="query"
        class="mc-search"
        type="search"
        placeholder="Search name, host, description…"
        @input="onQuery"
      />
      <select v-model="statusFilter" class="mc-select" @change="onQuery">
        <option value="all">All statuses</option>
        <option value="available">Working</option>
        <option value="not_configured">Stubs</option>
        <option value="broken">Broken</option>
        <option value="hosts">With hosts</option>
      </select>
    </div>

    <div class="mc-table-wrap" v-if="!loading && !error">
      <table class="mc-table">
        <thead>
          <tr>
            <th class="mc-col-logo"></th>
            <th>Name</th>
            <th>Status</th>
            <th>Hosts</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="r in pageRows" :key="r.name">
            <td class="mc-col-logo">
              <span class="mc-logo" aria-hidden="true">
                <img
                  v-if="!showLetter(r.name, r.hosts, r.logo)"
                  :src="logoSrc(r.name, r.hosts, r.logo) || undefined"
                  :alt="`${r.name} logo`"
                  loading="lazy"
                  referrerpolicy="no-referrer"
                  @error="onLogoError(r.name, r.hosts, r.logo)"
                />
                <span v-else class="mc-logo-fallback">{{ initial(r.name) }}</span>
              </span>
            </td>
            <td><code>{{ r.name }}</code></td>
            <td>
              <span class="mc-badge" :class="badgeClass(r.status)">{{
                displayStatus(r.status)
              }}</span>
            </td>
            <td class="mc-hosts">{{ (r.hosts || []).join(", ") || "—" }}</td>
            <td>{{ r.description || "—" }}</td>
          </tr>
          <tr v-if="pageRows.length === 0">
            <td colspan="5">No platforms match this filter.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="mc-pager" v-if="!loading && !error && filtered.length > pageSize">
      <button type="button" :disabled="page <= 1" @click="page--">Prev</button>
      <span>Page {{ page }} / {{ pageCount }}</span>
      <button type="button" :disabled="page >= pageCount" @click="page++">Next</button>
    </div>
  </div>
</template>
