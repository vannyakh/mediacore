import { defineConfig } from "vitepress";
import { withMermaid } from "vitepress-plugin-mermaid";

const github = "https://github.com/vannyakh/mediacore";

export default withMermaid(
  defineConfig({
    title: "MediaCore",
    description: "Permitted media download CLI/API — Extract · Process · Deliver",
    lang: "en-US",
    cleanUrls: true,
    lastUpdated: true,
    ignoreDeadLinks: [/^https?:\/\/localhost/],
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
      ["link", { rel: "icon", type: "image/png", href: "/logo.png" }],
      ["meta", { name: "theme-color", content: "#0ea5e9" }],
      ["meta", { property: "og:type", content: "website" }],
      ["meta", { property: "og:title", content: "MediaCore Docs" }],
      [
        "meta",
        {
          property: "og:description",
          content: "Permitted media download CLI and API",
        },
      ],
      ["meta", { property: "og:image", content: "/logo.png" }],
      ["meta", { name: "twitter:card", content: "summary" }],
    ],

    mermaid: {
      theme: "neutral",
      flowchart: { curve: "basis", htmlLabels: true },
    },

    themeConfig: {
      logo: { src: "/logo.png", alt: "MediaCore" },
      siteTitle: "MediaCore",
      outline: { level: [2, 3] },
      search: { provider: "local" },

      nav: [
        { text: "Guide", link: "/getting-started/" },
        { text: "Platforms", link: "/platforms/" },
        { text: "Plugins", link: "/plugins/" },
        { text: "API", link: "/api/" },
        { text: "SDK", link: "/sdk/" },
        {
          text: "Project",
          items: [
            { text: "Architecture", link: "/architecture/" },
            { text: "Layout", link: "/architecture/layout" },
            { text: "Deployment", link: "/deployment/" },
            { text: "Roadmap", link: "/getting-started/roadmap" },
            { text: "GitHub", link: github },
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
        "/platforms/": [
          {
            text: "Platforms",
            items: [
              { text: "Available platforms", link: "/platforms/" },
              { text: "Register an extractor", link: "/platforms/register" },
            ],
          },
        ],
        "/architecture/": [
          {
            text: "Architecture",
            items: [
              { text: "Overview", link: "/architecture/" },
              { text: "Repository layout", link: "/architecture/layout" },
              { text: "Engine & events", link: "/architecture/overview" },
              { text: "vs yt-dlp layout", link: "/architecture/mediacore-vs-ytdlp" },
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
            items: [{ text: "Install", link: "/sdk/" }],
          },
        ],
        "/plugins/": [
          {
            text: "Plugins",
            items: [
              { text: "Plugin catalog", link: "/plugins/" },
              { text: "Register a plugin", link: "/plugins/register" },
              { text: "Storage", link: "/plugins/storage" },
              { text: "Providers vs plugins", link: "/plugins/providers" },
            ],
          },
        ],
        "/deployment/": [
          {
            text: "Deployment",
            items: [{ text: "Docker", link: "/deployment/" }],
          },
        ],
      },

      socialLinks: [{ icon: "github", link: github }],

      footer: {
        message:
          "Released under the Apache License 2.0 · Docs theme customized in <code>docs/.vitepress</code>",
        copyright: "Copyright © MediaCore Contributors · v0.1.0",
      },

      editLink: {
        pattern: `${github}/edit/master/docs/:path`,
        text: "Edit this page",
      },
    },
  }),
);
