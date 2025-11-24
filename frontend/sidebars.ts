import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: 'category',
      label: "A Beginner's Guide to AI",
      link: {
        type: 'generated-index',
        title: "A Beginner's Guide to AI",
        description: "Your journey into the world of Artificial Intelligence starts here. This book covers the fundamentals, history, applications, and future of AI.",
        slug: '/',
      },
      collapsible: false,
      items: [
        'introduction-to-ai',
        'history-of-ai',
        'applications-of-ai',
        'future-of-ai',
      ],
    },
  ],
};

export default sidebars;