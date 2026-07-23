<script setup lang="ts">
type LinkItem = {
  title: string;
  href: string;
  hint?: string;
  icon?: string;
};

defineProps<{
  items: LinkItem[];
  compact?: boolean;
}>();
</script>

<template>
  <div class="mc-doc-links" :class="{ compact }">
    <a v-for="item in items" :key="item.href" class="mc-doc-link" :href="item.href">
      <img
        v-if="item.icon"
        class="mc-doc-link-icon"
        :src="item.icon"
        :alt="item.title"
        loading="lazy"
        referrerpolicy="no-referrer"
      />
      <span class="mc-doc-link-text">
        <strong>{{ item.title }}</strong>
        <small v-if="item.hint">{{ item.hint }}</small>
      </span>
    </a>
  </div>
</template>
