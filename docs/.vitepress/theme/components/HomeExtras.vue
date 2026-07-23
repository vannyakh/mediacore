<script setup lang="ts">
import TechStack from "./TechStack.vue";
</script>

<template>
  <TechStack />
  <section class="mc-section">
    <h2>Extend MediaCore</h2>
    <p class="mc-lead">Register extractors and plugins without forking the core.</p>
    <div class="mc-grid">
      <a class="mc-card" href="/platforms/">
        <h3>Platforms</h3>
        <p>Browse available / stub extractors and the full catalog API.</p>
      </a>
      <a class="mc-card" href="/platforms/register">
        <h3>Register an extractor</h3>
        <p>Implement Provider and register it in the registry.</p>
      </a>
      <a class="mc-card" href="/plugins/">
        <h3>Plugins</h3>
        <p>Storage, FFmpeg, webhooks, AI — optional capabilities.</p>
      </a>
      <a class="mc-card" href="/plugins/register">
        <h3>Register a plugin</h3>
        <p>Add plugins/*/plugin.py with PLUGIN + create() / on_event.</p>
      </a>
    </div>
  </section>
</template>

<style scoped>
a.mc-card {
  text-decoration: none;
  color: inherit;
  transition: border-color 0.15s ease, transform 0.15s ease;
}
a.mc-card:hover {
  border-color: var(--vp-c-brand-1);
  transform: translateY(-2px);
}
</style>
