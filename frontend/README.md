# A Beginner's Guide to AI - Docusaurus Site

This folder contains the source code for the "A Beginner's Guide to AI" book website, built with Docusaurus.

## Development

To run the site locally, follow these steps:

1.  **Install dependencies:**
    ```bash
    npm install
    ```
2.  **Start the development server:**
    ```bash
    npm run start
    ```
    The site will be available at `http://localhost:3000`.

## Deployment to GitHub Pages

This site is configured for easy deployment to GitHub Pages.

### Manual Deployment

1.  **Create a GitHub Repository:** Create a new GitHub repository named `hackathon-project`.

2.  **Push Your Code:** Add the remote and push the `main` branch.
    ```bash
    git remote add origin https://github.com/yourusername/hackathon-project.git
    git branch -M main
    git push -u origin main
    ```

3.  **Run the Deploy Command:** This command will build the static site and push the `build` directory to the `gh-pages` branch of your repository.
    ```bash
    npm run deploy
    ```

4.  **Configure GitHub Pages:** In your repository's settings under "Pages", set the source to "Deploy from a branch" and select the `gh-pages` branch with the `/ (root)` folder. Your site should be live at `https://yourusername.github.io/hackathon-project/`.

### Automated Deployment with GitHub Actions

This repository includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) that automates the deployment process. The workflow will trigger on every push to the `main` branch, building and deploying your site automatically.

**Note:** For the GitHub Action to work, you may need to go to your repository's **Settings > Actions > General** and ensure that **Workflow permissions** are set to **Read and write permissions**.