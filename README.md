# Giuseppe Stecca - Curriculum Vitae Website

This repository contains the source code for Giuseppe Stecca's personal CV website, built with [Hugo](https://gohugo.io/) and the [Hugo-Paper](https://github.com/nanxiaobei/hugo-paper) theme.

## Project Structure

- **`config.yaml`**: Main configuration file (title, menu, social links).
- **`content/`**: Contains the page content.
    - `en/_index.md`: English homepage.
    - `it/_index.md`: Italian homepage.
- **`static/files/`**: Contains static assets like your profile image (`cv2025.jpg`) and bibliography file (`scopus2025.bib`).
- **`scripts/update_bib.py`**: Python script to automate bibliography updates.
- **`themes/paper/`**: The visual theme (added as a git submodule).

## How to Maintain Steps

### 1. Editing Content
To update your profile, experience, styling, or other text:
- Edit **`content/en/_index.md`** for English.
- Edit **`content/it/_index.md`** for Italian.
- These files are standard Markdown. You can add new sections using `## Section Title`.

### 2. Updating Bibliography
When you have a new `scopus2025.bib` file:
1.  Place the new `.bib` file in `static/files/`.
2.  Run the update script:
    ```bash
    wsl python3 scripts/update_bib.py
    ```
    This script reads the `.bib` file and updates the list of publications in both `_index.md` files automatically.

### 3. Previewing Locally
To see your changes before publishing:
```bash
wsl hugo server
```
Open your browser to `http://localhost:1313`.

## Deployment to GitHub Pages

To publish this site to **https://gstecca.github.io**:

1.  **Create a Repository**: Create a new public repository named `cv` on your GitHub account (`gstecca`).
2.  **Push Code**:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin https://github.com/gstecca.github.io.git
    git push -u origin main
    ```


```markdown
3.  **Build and Deploy**:
    1.  Build the site:
        ```bash
        wsl hugo --destination docs
        ```
    2.  Push the `docs` folder to GitHub (ensure other files are excluded via `.gitignore` if you wish to keep the source private):
        ```bash
        git add docs/
        git commit -m "Update site"
        git push
        ```
    3.  In the GitHub repository settings, set the **GitHub Pages** source to the `/docs` folder of the `main` branch.
```
2.  Push everything to GitHub.
```markdown
    ```bash
    git add .
    git commit -m "Update site"
    git push
    ```
3.  Set GitHub Pages source to the `/docs` folder of the `main` branch.
```

## Requirements
- Hugo (Extended version recommended)
- Python 3 (for bibliography script)
