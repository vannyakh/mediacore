import { defineConfig } from "vitepress";

export default defineConfig({
  title: "MediaCore",
  description:
    "The Open Source Media Infrastructure Platform — Extract • Process • Automate • Deliver",
  lang: "en-US",
  cleanUrls: true,
  lastUpdated: true,
  ignoreDeadLinks: [/^https?:\/\/localhost/],
  // Compatibility stubs for old flat paths (GitHub); hide from the site tree.
  srcExclude: [
    "api.md",
    "sdk.md",
    "plugins.md",
    "architecture.md",
    "vision.md",
    "testing.md",
    "storage.md",
    "providers.md",
    "roadmap.md",
  ],

  head: [
    ["meta", { name: "theme-color", content: "#0b1220" }],
    ["meta", { property: "og:title", content: "MediaCore Docs" }],
    [
      "meta",
      {
        property: "og:description",
        content: "Open source media infrastructure — APIs, SDKs, CLI, plugins",
      },
    ],
  ],

  themeConfig: {
    siteTitle: "MediaCore",
    outline: { level: [2, 3] },
    search: { provider: "local" },

    nav: [
      { text: "Guide", link: "/getting-started/" },
      { text: "API", link: "/api/" },
      { text: "SDK", link: "/sdk/" },
      { text: "Plugins", link: "/plugins/" },
      {
        text: "Project",
        items: [
          { text: "Architecture", link: "/architecture/" },
          { text: "Deployment", link: "/deployment/" },
          { text: "Benchmarks", link: "/benchmarks/" },
          { text: "Roadmap", link: "/getting-started/roadmap" },
          { text: "GitHub", link: "https://github.com/mediacore/mediacore" },
        ],
      },
    ],

    sidebar: {
      "/getting-started/": [
        {
          text: "Getting started",
          items: [
            { text: "Quick start", link: "/getting-started/" },
            { text: "Vision", link: "/getting-started/vision" },
            { text: "Testing", link: "/getting-started/testing" },
            { text: "Roadmap", link: "/getting-started/roadmap" },
          ],
        },
      ],
      "/architecture/": [
        {
          text: "Architecture",
          items: [
            { text: "Overview", link: "/architecture/" },
            { text: "Engine & events", link: "/architecture/overview" },
          ],
        },
      ],
      "/api/": [
        {
          text: "API",
          items: [{ text: "REST /v1", link: "/api/" }],
        },
      ],
      "/sdk/": [
        {
          text: "SDK",
          items: [{ text: "Clients", link: "/sdk/" }],
        },
      ],
      "/plugins/": [
        {
          text: "Plugins",
          items: [
            { text: "Plugin system", link: "/plugins/" },
            { text: "Storage", link: "/plugins/storage" },
            { text: "Providers", link: "/plugins/providers" },
          ],
        },
      ],
      "/deployment/": [
        {
          text: "Deployment",
          items: [{ text: "Docker & Helm", link: "/deployment/" }],
        },
      ],
      "/benchmarks/": [
        {
          text: "Benchmarks",
          items: [{ text: "Overview", link: "/benchmarks/" }],
        },
      ],
    },

    socialLinks: [
      { icon: "github", link: "https://github.com/mediacore/mediacore" },
    ],

    footer: {
      message: "Released under the Apache License 2.0",
      copyright: "Copyright © MediaCore Contributors",
    },

    editLink: {
      pattern: "https://github.com/mediacore/mediacore/edit/main/docs/:path",
      text: "Edit this page",
    },
  },
});
