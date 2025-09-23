# Ultra-clean configuration for Theory of Computation docs
project = 'Theory of Computation - Made Simple'
copyright = '2025, CS Education Team'
author = 'CS Faculty'

# Minimal extensions for clean experience
extensions = [
    'sphinx.ext.githubpages',
]

# Clean template structure
templates_path = []
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Furo theme with student-friendly settings
html_theme = 'furo'
html_static_path = ['_static']

# Ultra-clean CSS and minimal JS
html_css_files = ['clean.css']
html_js_files = ['student-friendly.js']

# Furo theme optimized for weak students
html_theme_options = {
    "light_css_variables": {
        # Extra large, readable fonts
        "font-size--normal": "20px",
        "font-size--small": "18px", 
        "line-height": "1.8",
        
        # Maximum comfort spacing
        "sidebar-width": "320px",
        "content-padding": "3rem",
        
        # Gentle, non-intimidating colors
        "color-brand-primary": "#4f46e5",
        "color-brand-content": "#6366f1", 
        "color-background-primary": "#ffffff",
        "color-background-secondary": "#f8fafc",
        
        # Clear contrast for readability
        "color-foreground-primary": "#1e293b",
        "color-foreground-secondary": "#475569",
    },
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "top_of_page_button": None,  # Remove clutter
}

html_title = "Theory of Computation - Made Simple"
html_short_title = "TOC Simple"

# Remove default Sphinx branding for clean look
html_show_sphinx = False
html_show_copyright = False
