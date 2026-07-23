import DefaultTheme from "vitepress/theme";
import type { Theme } from "vitepress";
import "./custom.css";
import TechStack from "./components/TechStack.vue";
import PluginCatalog from "./components/PluginCatalog.vue";
import PlatformCatalog from "./components/PlatformCatalog.vue";
import SdkCatalog from "./components/SdkCatalog.vue";
import HomeExtras from "./components/HomeExtras.vue";
import DocHero from "./components/DocHero.vue";
import DocLinks from "./components/DocLinks.vue";
import DocStats from "./components/DocStats.vue";
import DocSteps from "./components/DocSteps.vue";
import ArchitectureLayers from "./components/ArchitectureLayers.vue";
import MermaidViewer from "./components/MermaidViewer.vue";

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component("TechStack", TechStack);
    app.component("PluginCatalog", PluginCatalog);
    app.component("PlatformCatalog", PlatformCatalog);
    app.component("SdkCatalog", SdkCatalog);
    app.component("HomeExtras", HomeExtras);
    app.component("DocHero", DocHero);
    app.component("DocLinks", DocLinks);
    app.component("DocStats", DocStats);
    app.component("DocSteps", DocSteps);
    app.component("ArchitectureLayers", ArchitectureLayers);
    app.component("MermaidViewer", MermaidViewer);
  },
} satisfies Theme;
