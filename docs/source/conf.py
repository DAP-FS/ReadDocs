# Configuration file for the Sphinx documentation builder.

project = 'Regular Expressions in Theory of Computation'
copyright = '2025, TOC Interactive Guide'
author = 'TOC Interactive Guide'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.mathjax',
    'sphinx_togglebutton',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinxcontrib.tikz',  # Added for TikZ diagrams
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output ------------------------------------------------
html_theme = 'furo'
html_title = "Regular Expressions in TOC"
html_theme_options = {
    "sidebar_hide_name": True,
    "light_css_variables": {
        "color-brand-primary": "#336699",
        "color-brand-content": "#336699",
        "color-admonition-background": "#fafafa",
    },
    "dark_css_variables": {
        "color-brand-primary": "#4A9EF7",
        "color-brand-content": "#4A9EF7",
        "color-admonition-background": "#2d2d2d",
    },
    "navigation_with_keys": True,
    "top_of_page_button": "edit",
}

html_static_path = ['_static']
html_logo = None
html_favicon = None

# -- Extension configuration -------------------------------------------------
todo_include_todos = True
togglebutton_hint_text_show = "Click to show hint"
togglebutton_hint_text_hide = "Click to hide hint"

# TikZ configuration
tikz_proc_suite = 'pdf2svg'  # Use pdf2svg for SVG output
tikz_transparent = True
tikz_tikzlibraries = 'arrows,automata,positioning,shapes'
tikz_latex_preamble = r'''
\definecolor{finalstatecolor}{RGB}{144,238,144}
\usetikzlibrary{arrows,automata,positioning,shapes}
'''

# Furo theme specific CSS customizations
html_css_files = [
    'custom.css',
]
