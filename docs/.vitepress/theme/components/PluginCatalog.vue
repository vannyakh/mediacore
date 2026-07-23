<script setup lang="ts">
import { computed, onMounted, ref } from "vue";

type PluginRow = {
  name: string;
  short_name: string;
  kind: string;
  status: string;
  description: string;
  capabilities: string[];
  logo?: string | null;
};

const rows = ref<PluginRow[]>([]);
const total = ref(0);
const byKind = ref<Record<string, number>>({});
const loading = ref(true);
const error = ref("");
const query = ref("");
const kindFilter = ref("all");
const statusFilter = ref<"all" | "available" | "stub">("all");
const brokenLogos = ref<Record<string, boolean>>({});

onMounted(async () => {
  try {
    const res = await fetch("/plugins.json");
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    rows.value = data.plugins || [];
    total.value = data.count ?? rows.value.length;
    byKind.value = data.by_kind || {};
  } catch (e) {
    error.value = e instanceof Error ? e.message : "Failed to load plugins";
  } finally {
    loading.value = false;
  }
});

const kinds = computed(() => Object.keys(byKind.value).sort());

const filtered = computed(() => {
  const q = query.value.trim().toLowerCase();
  return rows.value.filter((p) => {
    if (kindFilter.value !== "all" && p.kind !== kindFilter.value) return false;
    if (statusFilter.value !== "all" && p.status !== statusFilter.value) return false;
    if (!q) return true;
    const hay = [p.name, p.short_name, p.kind, p.description, ...(p.capabilities || [])]
      .join(" ")
      .toLowerCase();
    return hay.includes(q);
  });
});

function onLogoError(name: string) {
  brokenLogos.value = { ...brokenLogos.value, [name]: true };
}

function initial(name: string): string {
  const short = name.replace(/^mediacore-plugin-/, "");
  return (short || "?").slice(0, 1).toUpperCase();
}
</script>

<template>
  <div class="mc-plugins">
    <p class="mc-lead" style="margin-bottom: 0.85rem">
      <template v-if="loading">Loading plugins…</template>
      <template v-else-if="error">Could not load <code>/plugins.json</code>: {{ error }}</template>
      <template v-else>
        {{ total }} plugins across {{ kinds.length }} kinds.
      </template>
    </p>

    <div class="mc-toolbar" v-if="!loading && !error">
      <input
        v-model="query"
        class="mc-search"
        type="search"
        placeholder="Search name, kind, capability…"
      />
      <select v-model="kindFilter" class="mc-select">
        <option value="all">All kinds</option>
        <option v-for="k in kinds" :key="k" :value="k">{{ k }} ({{ byKind[k] }})</option>
      </select>
      <select v-model="statusFilter" class="mc-select">
        <option value="all">All statuses</option>
        <option value="available">Available</option>
        <option value="stub">Stub</option>
      </select>
    </div>

    <div class="mc-grid" v-if="!loading && !error">
      <article v-for="p in filtered" :key="p.name" class="mc-card mc-card-brand">
        <div class="mc-brand-row">
          <span class="mc-logo" aria-hidden="true">
            <img
              v-if="p.logo && !brokenLogos[p.name]"
              :src="p.logo"
              :alt="`${p.short_name} logo`"
              loading="lazy"
              referrerpolicy="no-referrer"
              @error="onLogoError(p.name)"
            />
            <span v-else class="mc-logo-fallback">{{ initial(p.name) }}</span>
          </span>
          <h3>{{ p.name }}</h3>
        </div>
        <p>{{ p.description || "MediaCore plugin" }}</p>
        <div class="mc-meta">
          <span class="mc-badge kind">{{ p.kind }}</span>
          <span class="mc-badge" :class="p.status === 'available' ? 'available' : 'stub'">{{
            p.status
          }}</span>
          <span v-for="cap in p.capabilities.slice(0, 3)" :key="cap" class="mc-badge kind">{{
            cap
          }}</span>
        </div>
      </article>
      <p v-if="filtered.length === 0" class="mc-lead">No plugins match this filter.</p>
    </div>
  </div>
</template>
