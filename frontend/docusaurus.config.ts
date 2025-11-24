import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: "A Beginner's Guide to AI",
  tagline: 'Your journey into the world of Artificial Intelligence starts here.',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://CodeVoyager007.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/hackathon-practice/',

  // GitHub pages deployment config.
  organizationName: 'CodeVoyager007', // Usually your GitHub org/user name.
  projectName: 'hackathon-practice', // Usually your repo name.
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Please change this to your repo.
          editUrl:
            'https://github.com/CodeVoyager007/hackathon-book/tree/main/frontend/',
          routeBasePath: '/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: "A Beginner's Guide to AI",
      logo: {
        alt: 'AI Book Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Chapters',
        },
        {
          href: 'https://github.com/CodeVoyager007/hackathon-book',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Chapters',
          items: [
            {
              label: '1. Introduction to AI',
              to: '/introduction-to-ai',
            },
            {
              label: '2. History of AI',
              to: '/history-of-ai',
            },
            {
                label: '3. Applications of AI',
                to: '/applications-of-ai',
            },
            {
                label: '4. Future of AI',
                to: '/future-of-ai',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Stack Overflow',
              href: 'https://stackoverflow.com/questions/tagged/docusaurus',
            },
            {
              label: 'Discord',
              href: 'https://discordapp.com/invite/docusaurus',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/docusaurus',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/CodeVoyager007/hackathon-book',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} A Beginner's Guide to AI. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,

  plugins: [
    [
      '@docusaurus/plugin-client-redirects',
      {
        from: '/docs/intro',
        to: '/',
      },
    ],
    ['@cmfcmf/docusaurus-search-local', {}]
  ],

  typescript: {
    // Recommended in Docusaurus docs
    // Fork a new process for type checking
    forkTsChecker: true,
    // We can also enable incremental builds
    useIncrementalCompilation: true,
  },
};

export default config;