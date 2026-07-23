<script setup lang="ts">
defineProps<{
  eyebrow?: string;
  title: string;
  lead?: string;
}>();
</script>

<template>
  <header class="mc-doc-hero">
    <p v-if="eyebrow" class="mc-doc-eyebrow">{{ eyebrow }}</p>
    <h1 class="mc-doc-title">{{ title }}</h1>
    <p v-if="lead" class="mc-doc-lead">{{ lead }}</p>
    <slot />
  </header>
</template>
