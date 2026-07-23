<script setup lang="ts">
type Stat = { label: string; value: string };

defineProps<{
  items: Stat[];
}>();
</script>

<template>
  <div class="mc-doc-stats">
    <div v-for="s in items" :key="s.label" class="mc-doc-stat">
      <span class="mc-doc-stat-value">{{ s.value }}</span>
      <span class="mc-doc-stat-label">{{ s.label }}</span>
    </div>
  </div>
</template>
