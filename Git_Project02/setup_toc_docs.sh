#!/usr/bin/env bash
# setup_toc_docs.sh
# Create toc-docs directory and file structure

# Root directory
mkdir -p toc-docs

# Docs subdirectories
mkdir -p toc-docs/docs/_static
mkdir -p toc-docs/docs/content
mkdir -p toc-docs/.github/workflows

# Files inside docs/
touch toc-docs/docs/conf.py
touch toc-docs/docs/index.rst
touch toc-docs/docs/requirements.txt

# Static files
touch toc-docs/docs/_static/clean.css
touch toc-docs/docs/_static/student-friendly.js

# Content .rst files
touch toc-docs/docs/content/basics.rst
touch toc-docs/docs/content/automata.rst
touch toc-docs/docs/content/languages.rst
touch toc-docs/docs/content/complexity.rst
touch toc-docs/docs/content/exercises.rst

# GitHub workflow
touch toc-docs/.github/workflows/deploy.yml

# Root-level files
touch toc-docs/README.md
touch toc-docs/Makefile

