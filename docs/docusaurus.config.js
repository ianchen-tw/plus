module.exports = {
  title: "Plus",
  tagline: "API Server for students",
  url: "https://ianre657.github.io/plus/",
  baseUrl: "/plus/",
  favicon: "img/favicon.ico",
  organizationName: "ianre657", // Usually your GitHub org/user name.
  projectName: "plus", // Usually your repo name.
  themeConfig: {
    navbar: {
      title: "plus",
      logo: {
        alt: "plus logo",
        src: "img/nctuplus_logo_22.png",
      },
      items: [
        {
          to: "docs/intro",
          activeBasePath: "docs",
          label: "Docs",
          position: "left",
        },
        {
          href: "https://github.com/ianre657/plus",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Getting Started",
          items: [
            {
              label: "Installation",
              to: "docs/getting_started",
            },
          ],
        },
        {
          title: "Community",
          items: [
            // {
            //   label: 'Discord',
            //   href: 'https://discordapp.com/invite/docusaurus',
            // },
            {
              label: "Github Issue Tracker",
              href: "https://github.com/ianre657/plus/issues",
            },
          ],
        },
        {
          title: "More",
          items: [
            {
              label: "GitHub",
              href: "https://github.com/ianre657/plus",
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Ian Chen`,
    },
  },
  presets: [
    [
      "@docusaurus/preset-classic",
      {
        docs: {
          // It is recommended to set document id as docs home page (`docs/` path).
          homePageId: "docs/getting_started",
          sidebarPath: require.resolve("./sidebars.js"),
          // Please change this to your repo.
          editUrl: "https://github.com/ianre657/plus/edit/master/",
          // 'https://github.com/facebook/docusaurus/edit/master/website/',
        },
        // blog: {
        //   showReadingTime: true,
        //   // Please change this to your repo.
        //   editUrl:
        //     'https://github.com/facebook/docusaurus/edit/master/website/blog/',
        // },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      },
    ],
  ],
}
