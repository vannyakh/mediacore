<script setup lang="ts">
type Step = { title: string; body?: string };

defineProps<{
  items: Step[];
}>();
</script>

<template>
  <ol class="mc-doc-steps">
    <li v-for="(step, i) in items" :key="i" class="mc-doc-step">
      <span class="mc-doc-step-n">{{ i + 1 }}</span>
      <div>
        <strong>{{ step.title }}</strong>
        <p v-if="step.body">{{ step.body }}</p>
      </div>
    </li>
  </ol>
</template>
