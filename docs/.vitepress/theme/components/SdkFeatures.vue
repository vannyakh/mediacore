<script setup lang="ts">
const features = [
  {
    title: "One REST surface",
    body: "Same media / jobs / plugins methods across every language client.",
  },
  {
    title: "Local-first install",
    body: "Add clients from the monorepo path today. Registry publish comes later.",
  },
  {
    title: "API-key auth",
    body: "All clients send X-API-Key against your MediaCore /v1 endpoint.",
  },
  {
    title: "Ready + stubs",
    body: "Ship with JS, TS, Python, Go, Rust, Dart, C#. Java / Swift / Kotlin scaffolds next.",
  },
];
</script>

<template>
  <div class="mc-sdk-features">
    <article v-for="f in features" :key="f.title" class="mc-sdk-feature">
      <h3>{{ f.title }}</h3>
      <p>{{ f.body }}</p>
    </article>
  </div>
</template>
