<script setup lang="ts">
const layers = [
  {
    label: "Applications",
    items: [
      { name: "SDK", icon: "https://cdn.simpleicons.org/typescript/3178C6" },
      { name: "CLI", icon: "https://cdn.simpleicons.org/gnubash/4EAA25" },
      { name: "Dashboard", icon: "https://cdn.simpleicons.org/nextdotjs/000000" },
      { name: "Desktop", icon: "https://cdn.simpleicons.org/tauri/24C8DB" },
    ],
  },
  {
    label: "API",
    items: [{ name: "REST /v1", icon: "https://cdn.simpleicons.org/fastapi/009688" }],
  },
  {
    label: "Runtime",
    items: [
      { name: "Pipeline", icon: "https://cdn.simpleicons.org/python/3776AB" },
      { name: "Worker", icon: "https://cdn.simpleicons.org/redis/DC382D" },
      { name: "Scheduler", icon: "https://cdn.simpleicons.org/prometheus/E6522C" },
    ],
  },
  {
    label: "Plugins",
    items: [
      { name: "Providers", icon: "https://cdn.simpleicons.org/package/0ea5e9" },
      { name: "Storage", icon: "https://cdn.simpleicons.org/files/0ea5e9" },
      { name: "FFmpeg", icon: "https://cdn.simpleicons.org/ffmpeg/007808" },
      { name: "AI", icon: "https://cdn.simpleicons.org/openai/412991" },
    ],
  },
];
</script>

<template>
  <div class="mc-doc-stack" aria-label="MediaCore architecture layers">
    <div v-for="layer in layers" :key="layer.label" class="mc-arch-layer">
      <span class="mc-arch-label">{{ layer.label }}</span>
      <div class="mc-doc-stack-row">
        <span v-for="item in layer.items" :key="item.name" class="mc-doc-chip">
          <img :src="item.icon" :alt="item.name" loading="lazy" referrerpolicy="no-referrer" />
          {{ item.name }}
        </span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.mc-arch-layer {
  display: grid;
  gap: 0.45rem;
  padding: 0.85rem 0.9rem;
  border-radius: 14px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
}

.mc-arch-label {
  font-size: 0.72rem;
  font-weight: 750;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--vp-c-text-2);
  text-align: center;
}
</style>
