<script setup lang="ts">
const stack = [
  { name: "Python", slug: "python", color: "3776AB", href: "https://www.python.org/" },
  { name: "FastAPI", slug: "fastapi", color: "009688", href: "https://fastapi.tiangolo.com/" },
  { name: "Vue", slug: "vuedotjs", color: "4FC08D", href: "https://vuejs.org/" },
  { name: "VitePress", slug: "vitepress", color: "5C73E7", href: "https://vitepress.dev/" },
  { name: "TypeScript", slug: "typescript", color: "3178C6", href: "https://www.typescriptlang.org/" },
  { name: "Rust", slug: "rust", color: "000000", href: "https://www.rust-lang.org/" },
  { name: "Go", slug: "go", color: "00ADD8", href: "https://go.dev/" },
  { name: "Docker", slug: "docker", color: "2496ED", href: "https://www.docker.com/" },
  { name: "Redis", slug: "redis", color: "DC382D", href: "https://redis.io/" },
  { name: "PostgreSQL", slug: "postgresql", color: "4169E1", href: "https://www.postgresql.org/" },
  { name: "FFmpeg", slug: "ffmpeg", color: "007808", href: "https://ffmpeg.org/" },
  { name: "Prometheus", slug: "prometheus", color: "E6522C", href: "https://prometheus.io/" },
];

function iconUrl(slug: string, color: string) {
  return `https://cdn.simpleicons.org/${slug}/${color}`;
}
</script>

<template>
  <section class="mc-section">
    <h2>Tech stack</h2>
    <div class="mc-tech">
      <a v-for="item in stack" :key="item.name" :href="item.href" target="_blank" rel="noreferrer">
        <img :src="iconUrl(item.slug, item.color)" :alt="item.name" loading="lazy" />
        <span>{{ item.name }}</span>
      </a>
    </div>
  </section>
</template>
