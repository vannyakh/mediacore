<script setup lang="ts">
import { computed, nextTick, onMounted, ref, watch } from "vue";
import { useData } from "vitepress";
import mermaid from "mermaid";

const props = defineProps<{
  /** Mermaid source (preferred). */
  code?: string;
  /** Optional title shown above the diagram. */
  title?: string;
}>();

const slots = defineSlots<{
  default?: () => unknown;
}>();

const { isDark } = useData();
const host = ref<HTMLElement | null>(null);
const error = ref("");
const ready = ref(false);

const source = computed(() => {
  if (props.code?.trim()) return props.code.trim();
  // Slot text fallback is handled after mount via textContent
  return "";
});

let idSeq = 0;

async function render() {
  if (!host.value) return;
  error.value = "";
  const raw =
    source.value ||
    (host.value.querySelector("[data-mermaid-source]")?.textContent || "").trim();
  if (!raw) {
    error.value = "Empty mermaid source";
    return;
  }

  mermaid.initialize({
    startOnLoad: false,
    securityLevel: "strict",
    theme: isDark.value ? "dark" : "neutral",
    flowchart: { curve: "basis", htmlLabels: true },
  });

  const id = `mc-mermaid-${++idSeq}-${Date.now()}`;
  try {
    const { svg } = await mermaid.render(id, raw);
    const canvas = host.value.querySelector(".mc-mermaid-canvas");
    if (canvas) canvas.innerHTML = svg;
    ready.value = true;
  } catch (e) {
    error.value = e instanceof Error ? e.message : "Mermaid render failed";
    ready.value = false;
  }
}

onMounted(async () => {
  await nextTick();
  await render();
});

watch(isDark, () => {
  void render();
});
watch(source, () => {
  void render();
});
</script>

<template>
  <figure class="mc-mermaid-viewer" :class="{ ready }">
    <figcaption v-if="title" class="mc-mermaid-title">{{ title }}</figcaption>
    <div ref="host" class="mc-mermaid-frame">
      <div class="mc-mermaid-canvas" aria-hidden="false" />
      <pre v-if="!code" class="mc-mermaid-slot" data-mermaid-source hidden><slot /></pre>
    </div>
    <p v-if="error" class="mc-mermaid-error">{{ error }}</p>
  </figure>
</template>
