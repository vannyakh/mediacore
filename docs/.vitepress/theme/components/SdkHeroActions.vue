<script setup lang="ts">
const actions = [
  { label: "Install JS", href: "#quick-start", primary: true },
  { label: "Languages", href: "#languages" },
  { label: "Source", href: "/architecture/overview" },
  { label: "REST API", href: "/api/" },
];
</script>

<template>
  <div class="mc-sdk-actions">
    <a
      v-for="a in actions"
      :key="a.label"
      class="mc-sdk-action"
      :class="{ primary: a.primary }"
      :href="a.href"
    >
      {{ a.label }}
    </a>
  </div>
</template>
