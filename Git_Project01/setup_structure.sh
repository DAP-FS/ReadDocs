#!/usr/bin/env bash
# Create Sphinx furo docs project structure (empty files only)

mkdir -p project-root/docs/_static
mkdir -p project-root/docs/_templates
mkdir -p project-root/docs/chapters
mkdir -p project-root/.github/workflows

# docs files
touch project-root/docs/conf.py
touch project-root/docs/index.rst
touch project-root/docs/requirements.txt
touch project-root/docs/_static/custom.css
touch project-root/docs/_static/custom.js
touch project-root/docs/_templates/custom-button.html
touch project-root/docs/chapters/getting-started.rst
touch project-root/docs/chapters/chapter1.rst
touch project-root/docs/chapters/chapter2.rst
touch project-root/docs/chapters/chapter3.rst
touch project-root/docs/chapters/glossary.rst
touch project-root/docs/chapters/instructor-notes.rst

# GitHub workflow
touch project-root/.github/workflows/gh-pages.yml

# root-level files
touch project-root/.nojekyll
touch project-root/README.md
touch project-root/Makefile

