<script setup lang="ts">
import { computed, nextTick, onBeforeUnmount, onMounted, ref, watch } from "vue";
import { DataSet } from "vis-data";
import { Network } from "vis-network";
import {
  KIND_COLORS,
  edges as allEdges,
  nodes as allNodes,
  type GraphEdge,
  type GraphKind,
  type GraphNode,
} from "../data/dependency-graph";

const container = ref<HTMLElement | null>(null);
let network: Network | null = null;
let resizeObserver: ResizeObserver | null = null;

const hideOptional = ref(false);
const hideInfra = ref(false);
const hideSdk = ref(false);
const selectedId = ref<string | null>(null);
const minimized = ref(false);
const showLegend = ref(false);

const legend: { kind: GraphKind; label: string }[] = [
  { kind: "core", label: "Core" },
  { kind: "app", label: "Apps" },
  { kind: "provider", label: "Providers" },
  { kind: "plugin", label: "Plugins" },
  { kind: "sdk", label: "SDKs" },
  { kind: "infra", label: "Infra" },
];

function filterGraph() {
  let nodes: GraphNode[] = [...allNodes];
  let edges: GraphEdge[] = [...allEdges];

  if (hideInfra.value) {
    const drop = new Set(nodes.filter((n) => n.kind === "infra").map((n) => n.id));
    nodes = nodes.filter((n) => !drop.has(n.id));
    edges = edges.filter((e) => !drop.has(e.from) && !drop.has(e.to));
  }
  if (hideSdk.value) {
    const drop = new Set(nodes.filter((n) => n.kind === "sdk").map((n) => n.id));
    nodes = nodes.filter((n) => !drop.has(n.id));
    edges = edges.filter((e) => !drop.has(e.from) && !drop.has(e.to));
  }
  if (hideOptional.value) {
    edges = edges.filter((e) => e.kind !== "optional");
  }

  const ids = new Set(nodes.map((n) => n.id));
  edges = edges.filter((e) => ids.has(e.from) && ids.has(e.to));
  return { nodes, edges };
}

const stats = computed(() => {
  const g = filterGraph();
  return { nodes: g.nodes.length, edges: g.edges.length };
});

function edgeColor(kind: GraphEdge["kind"]) {
  if (kind === "optional") return "#a855f7";
  if (kind === "dev") return "#64748b";
  return "#f472b6";
}

function isDark() {
  return document.documentElement.classList.contains("dark");
}

function labelColor() {
  return isDark() ? "#e2e8f0" : "#0f172a";
}

function canvasSize() {
  if (!container.value) return null;
  const w = container.value.clientWidth;
  const h = container.value.clientHeight;
  if (w < 2 || h < 2) return null;
  return { w, h };
}

function syncSize() {
  if (!network) return;
  const size = canvasSize();
  if (!size) return;
  network.setSize(`${size.w}px`, `${size.h}px`);
  network.redraw();
}

function fit(animate = true) {
  if (!network) return;
  syncSize();
  // Do not cap maxZoomLevel — a tight layout needs zoom-in to fill the canvas.
  // Capping left a tiny center blob and mismatched drag hit-targets.
  network.fit({
    animation: animate
      ? { duration: 280, easingFunction: "easeInOutQuad" }
      : false,
  });
}

function onWindowResize() {
  syncSize();
  fit(false);
}

function build() {
  if (!container.value) return;
  network?.destroy();
  network = null;

  const { nodes, edges } = filterGraph();
  const fontColor = labelColor();
  const visNodes = new DataSet(
    nodes.map((n) => ({
      id: n.id,
      label: n.label,
      group: n.kind,
      color: {
        background: KIND_COLORS[n.kind],
        border: KIND_COLORS[n.kind],
        highlight: { background: "#f97316", border: "#ea580c" },
      },
      font: { color: fontColor, size: 14, face: "ui-sans-serif, system-ui" },
      shape: "dot",
      size: n.id === "mediacore" ? 32 : 20,
      borderWidth: 2,
      // Allow free dragging once physics settles.
      physics: true,
    })),
  );
  const visEdges = new DataSet(
    edges.map((e, i) => ({
      id: i,
      from: e.from,
      to: e.to,
      arrows: { to: { enabled: true, scaleFactor: 0.7 } },
      color: { color: edgeColor(e.kind), highlight: "#fb923c", opacity: 0.85 },
      width: e.kind === "prod" ? 1.8 : 1.2,
      dashes: e.kind === "optional",
      smooth: true,
    })),
  );

  const el = container.value;
  network = new Network(
    el,
    { nodes: visNodes, edges: visEdges },
    {
      autoResize: false,
      interaction: {
        hover: true,
        tooltipDelay: 80,
        navigationButtons: false,
        keyboard: { enabled: true, bindToWindow: false },
        zoomView: true,
        dragView: true,
        dragNodes: true,
        selectable: true,
        multiselect: false,
      },
      physics: {
        enabled: true,
        solver: "forceAtlas2Based",
        forceAtlas2Based: {
          gravitationalConstant: -55,
          centralGravity: 0.005,
          springLength: 160,
          springConstant: 0.06,
          damping: 0.45,
          avoidOverlap: 1,
        },
        stabilization: { enabled: true, iterations: 200, fit: false },
      },
      nodes: {
        shadow: false,
        scaling: { min: 16, max: 36 },
      },
      edges: {
        selectionWidth: 2,
        hoverWidth: 1.5,
      },
    },
  );

  syncSize();

  network.on("selectNode", (params) => {
    selectedId.value = (params.nodes[0] as string) || null;
  });
  network.on("deselectNode", () => {
    selectedId.value = null;
  });

  // After layout settles: stop physics so node drag feels solid, then fill canvas.
  network.once("stabilizationIterationsDone", () => {
    network?.setOptions({ physics: { enabled: false } });
    requestAnimationFrame(() => {
      syncSize();
      fit(false);
    });
  });

  network.on("dragStart", () => {
    network?.setOptions({ physics: { enabled: false } });
  });
}

async function toggleMinimized() {
  minimized.value = !minimized.value;
  await nextTick();
  requestAnimationFrame(() => {
    syncSize();
    fit(true);
  });
}

onMounted(async () => {
  await nextTick();
  // Wait a frame so flex/layout has real pixel size before vis-network init.
  requestAnimationFrame(() => {
    build();
    if (container.value && typeof ResizeObserver !== "undefined") {
      let lastW = 0;
      let lastH = 0;
      resizeObserver = new ResizeObserver(() => {
        const size = canvasSize();
        if (!size) return;
        if (size.w === lastW && size.h === lastH) return;
        lastW = size.w;
        lastH = size.h;
        syncSize();
        fit(false);
      });
      resizeObserver.observe(container.value);
    }
  });
  window.addEventListener("resize", onWindowResize);
});

onBeforeUnmount(() => {
  window.removeEventListener("resize", onWindowResize);
  resizeObserver?.disconnect();
  resizeObserver = null;
  network?.destroy();
  network = null;
});

watch([hideOptional, hideInfra, hideSdk], async () => {
  await nextTick();
  requestAnimationFrame(() => build());
});
</script>

<template>
  <div class="mc-graph" :class="{ 'is-minimized': minimized }">
    <div class="mc-graph__toolbar">
      <div class="mc-graph__title">
        <strong>MediaCore relationships</strong>
        <span>{{ stats.nodes }} nodes · {{ stats.edges }} edges</span>
        <span v-if="selectedId" class="mc-graph__selected">
          · <code>{{ selectedId }}</code>
        </span>
      </div>
      <div class="mc-graph__actions">
        <button type="button" class="mc-chip" @click="fit">Fit</button>
        <button
          type="button"
          class="mc-chip"
          :aria-pressed="!minimized"
          @click="toggleMinimized"
        >
          {{ minimized ? "Show options" : "Minimize" }}
        </button>
      </div>
    </div>

    <div
      ref="container"
      class="mc-graph__canvas"
      role="img"
      aria-label="MediaCore dependency graph"
    />

    <footer v-show="!minimized" class="mc-graph__dock">
      <div class="mc-graph__dock-row">
        <div class="mc-graph__filters">
          <label class="mc-pill">
            <input v-model="hideOptional" type="checkbox" />
            Hide optional
          </label>
          <label class="mc-pill">
            <input v-model="hideInfra" type="checkbox" />
            Hide infra
          </label>
          <label class="mc-pill">
            <input v-model="hideSdk" type="checkbox" />
            Hide SDKs
          </label>
        </div>

        <button
          type="button"
          class="mc-chip ghost"
          :aria-expanded="showLegend"
          @click="showLegend = !showLegend"
        >
          {{ showLegend ? "Hide legend" : "Legend" }}
        </button>
      </div>

      <div v-if="showLegend" class="mc-graph__legend">
        <span v-for="item in legend" :key="item.kind" class="mc-legend-item">
          <i class="dot" :style="{ background: KIND_COLORS[item.kind] }" />
          {{ item.label }}
        </span>
        <span class="mc-legend-item">
          <i class="line prod" />
          Prod
        </span>
        <span class="mc-legend-item">
          <i class="line optional" />
          Optional
        </span>
      </div>

      <p class="mc-graph__hint">Drag · scroll to zoom · click a node</p>
    </footer>
  </div>
</template>

<style scoped>
.mc-graph {
  position: relative;
  display: flex;
  flex-direction: column;
  height: min(72vh, 720px);
  min-height: 520px;
  margin: 0.5rem 0 1.25rem;
  /* no card — blend into VitePress page background */
  border: 0;
  border-radius: 0;
  background: transparent;
  color: var(--vp-c-text-1);
  overflow: visible;
}

.mc-graph.is-minimized {
  height: min(78vh, 760px);
}

.mc-graph__toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  padding: 0 0 0.65rem;
  background: transparent;
}

.mc-graph__title {
  display: flex;
  flex-wrap: wrap;
  align-items: baseline;
  gap: 0.4rem 0.55rem;
  min-width: 0;
}

.mc-graph__title strong {
  font-size: 0.95rem;
  font-weight: 700;
  letter-spacing: -0.01em;
  color: var(--vp-c-text-1);
}

.mc-graph__title > span {
  font-size: 0.78rem;
  color: var(--vp-c-text-2);
}

.mc-graph__selected code {
  color: var(--vp-c-brand-1);
  font-size: 0.78rem;
}

.mc-graph__actions {
  display: flex;
  gap: 0.4rem;
  flex: 0 0 auto;
}

.mc-graph__canvas {
  flex: 1 1 auto;
  width: 100%;
  min-height: 420px;
  height: 100%;
  touch-action: none;
  cursor: grab;
  background: transparent;
  /* Ensure vis-network gets a real box to measure */
  position: relative;
  overflow: hidden;
}

.mc-graph__canvas:active {
  cursor: grabbing;
}

/* Fill the content box; do NOT force canvas CSS size — that breaks drag hit-testing */
.mc-graph__canvas :deep(.vis-network) {
  width: 100%;
  height: 100%;
  outline: none;
}

.mc-graph__dock {
  margin-top: 0.35rem;
  padding: 0.55rem 0 0;
  border-top: 1px solid var(--vp-c-divider);
  background: transparent;
}

.mc-graph__dock-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.mc-graph__filters {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
}

.mc-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.26rem 0.6rem;
  border-radius: 999px;
  border: 1px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
  font-size: 0.78rem;
  color: var(--vp-c-text-1);
  cursor: pointer;
  user-select: none;
}

.mc-pill input {
  accent-color: var(--vp-c-brand-1);
}

.mc-chip {
  border: 1px solid var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
  border-radius: 999px;
  padding: 0.26rem 0.7rem;
  font-size: 0.78rem;
  font-weight: 600;
  cursor: pointer;
}

.mc-chip:hover {
  filter: brightness(1.05);
}

.mc-chip.ghost {
  border-color: var(--vp-c-divider);
  background: transparent;
  color: var(--vp-c-text-2);
}

.mc-chip.ghost:hover {
  background: var(--vp-c-bg-soft);
  color: var(--vp-c-text-1);
}

.mc-graph__legend {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem 0.85rem;
  margin-top: 0.55rem;
  padding-top: 0.5rem;
  border-top: 1px solid var(--vp-c-divider);
}

.mc-legend-item {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.74rem;
  color: var(--vp-c-text-2);
}

.dot {
  width: 8px;
  height: 8px;
  border-radius: 999px;
  display: inline-block;
}

.line {
  width: 16px;
  height: 0;
  border-top: 2px solid #f472b6;
  display: inline-block;
}

.line.optional {
  border-top-style: dashed;
  border-top-color: #a855f7;
}

.mc-graph__hint {
  margin: 0.4rem 0 0;
  font-size: 0.7rem;
  color: var(--vp-c-text-3);
}

@media (max-width: 700px) {
  .mc-graph__toolbar {
    align-items: flex-start;
    flex-direction: column;
  }
  .mc-graph__dock-row {
    flex-direction: column;
    align-items: stretch;
  }
}
</style>
