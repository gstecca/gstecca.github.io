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

## How to Maintain and Update

### 1. Editing Content
To update your profile, experience, styling, or other text, modify these files:

*   **English Content**: Edit `content/en/_index.md`.
*   **Italian Content**: Edit `content/it/_index.md`.
*   **Site Configuration**: Edit `config.yaml` to change the site title, menu links, social icons, or your avatar image path.

### 2. Updating Profile Image
Replace the file `static/files/cv2025.jpg` with your new image, keeping the same filename, or update the `avatar` path in `config.yaml` to point to a new file in `static/files/`.

### 3. Updating Bibliography
When you have a new `scopus2025.bib` file:
1.  Place the new `.bib` file in `static/files/`.
2.  Run the update script:
    ```bash
    python3 scripts/update_bib.py
    ```
    This script reads the `.bib` file and automatically updates the publication lists in both `_index.md` files.

### 4. Previewing Locally
To see your changes before publishing:
```bash
hugo server
```
Open your browser to `http://localhost:1313`.

## Deployment to GitHub Pages

To publish changes to **https://gstecca.github.io**:

1.  **Rebuild the Site**:
    This command generates the static website files into the `docs/` folder, which GitHub Pages uses.
    ```bash
    hugo -d docs
    ```

2.  **Push Changes**:
     Commit and push the updated `docs/` folder (and any other changes) to GitHub.
    ```bash
    git add .
    git commit -m "Update site content and rebuild"
    git push
    ```

3.  **Verify**:
    Wait a minute for GitHub Pages to deploy, then visit [https://gstecca.github.io](https://gstecca.github.io).

## Requirements
- Hugo (Extended version recommended)
- Python 3 (for bibliography script)
