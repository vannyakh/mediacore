<script setup lang="ts">
import { onMounted, ref } from "vue";

type SdkRow = {
  id: string;
  name: string;
  logo?: string;
};

const rows = ref<SdkRow[]>([]);
const loading = ref(true);
const error = ref("");
const brokenLogos = ref<Record<string, boolean>>({});

onMounted(async () => {
  try {
    const res = await fetch("/sdks.json");
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    rows.value = data.sdks || [];
  } catch (e) {
    error.value = e instanceof Error ? e.message : "Failed to load SDKs";
  } finally {
    loading.value = false;
  }
});

function onLogoError(id: string) {
  brokenLogos.value = { ...brokenLogos.value, [id]: true };
}

function initial(name: string): string {
  return (name || "?").slice(0, 1).toUpperCase();
}
</script>

<template>
  <div class="mc-sdks">
    <p v-if="loading" class="mc-lead">Loading SDKs…</p>
    <p v-else-if="error" class="mc-lead">Could not load <code>/sdks.json</code>: {{ error }}</p>
    <div v-else class="mc-sdk-grid">
      <a v-for="s in rows" :key="s.id" class="mc-sdk-tile" :href="`/sdk/${s.id}`">
        <span class="mc-sdk-logo" aria-hidden="true">
          <img
            v-if="s.logo && !brokenLogos[s.id]"
            :src="s.logo"
            :alt="`${s.name} logo`"
            loading="lazy"
            referrerpolicy="no-referrer"
            @error="onLogoError(s.id)"
          />
          <span v-else class="mc-logo-fallback">{{ initial(s.name) }}</span>
        </span>
        <span class="mc-sdk-name">{{ s.name }}</span>
      </a>
    </div>
  </div>
</template>
