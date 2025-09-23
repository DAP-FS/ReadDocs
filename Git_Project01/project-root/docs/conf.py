# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'Educational Documentation'
copyright = '2025, Educational Team'
author = 'Educational Team'
release = '1.0'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# HTML output options
html_theme = 'furo'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
html_js_files = [
    'custom.js',
]

# Furo theme options - optimized for accessibility and readability
html_theme_options = {
    "light_css_variables": {
        "font-size--normal": "18px",  # Larger default font
        "font-size--small": "16px",
        "font-size--small--2": "14px",
        "line-height": "1.6",  # Better line spacing
        "sidebar-width": "280px",  # Wider sidebar
        "color-brand-primary": "#2563eb",
        "color-brand-content": "#1d4ed8",
        "color-admonition-title--note": "#0ea5e9",
        "color-admonition-title--tip": "#10b981",
        "color-admonition-title--important": "#f59e0b",
        "color-admonition-title--caution": "#ef4444",
    },
    "dark_css_variables": {
        "font-size--normal": "18px",
        "font-size--small": "16px", 
        "font-size--small--2": "14px",
        "line-height": "1.6",
        "sidebar-width": "280px",
        "color-brand-primary": "#60a5fa",
        "color-brand-content": "#93c5fd",
    },
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "top_of_page_button": "edit",
    "source_repository": "https://github.com/yourusername/your-repo",
    "source_branch": "main",
    "source_directory": "docs/",
}

html_title = "Educational Documentation"
html_short_title = "EduDocs"

# Todo extension options
todo_include_todos = True

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
