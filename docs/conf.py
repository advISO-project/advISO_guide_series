# Configuration file for the Sphinx documentation builder.
from datetime import date

#
# ============================================================================
# GUIDE SETTINGS — edit these to configure your guide
# ============================================================================

## Guide name and metadata
guide_name = 'advISO Guide Series'
author = 'advISO Team'
copyright = f'{author} & contributors'
release = '0.1'
version = '0.1.0'

## Set under_development to True to display the "under development" banner.
under_development = True

## Guide subtitle that appears on the logo (e.g. "Validation Guide", "SOP Guide").
guide_subtitle = 'Guide Series'

## Sidebar background colour (hex).
sidebar_color = '#1F3347'

## GitHub repository URL.
github_repo = 'https://github.com/advISO-project/advISO_guide_series'

## Path to the sidebar logo image.
html_logo = '_static/adviso_guide_series_logo_transparent.png'


# ============================================================================
# Everything below here is Sphinx plumbing — you shouldn't need to change it.
# ============================================================================

project = guide_name

exclude_patterns = [
    '_build',
]

# -- Extensions --------------------------------------------------------------

extensions = [
    'myst_parser',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx_design',
    'sphinx_tabs.tabs',
]

# -- MyST (Markdown) configuration ------------------------------------------

myst_enable_extensions = [
    'colon_fence',
    'substitution',
]

today_fmt = "%Y-%m-%d"

myst_substitutions = {
    'guide_name': guide_name,
    'guide_subtitle': guide_subtitle,
    'sidebar_color': sidebar_color,

    'release': release,
    'version': version,
    'github_repo': github_repo,
    'github_issues_link': f'[GitHub repository]({github_repo}/issues)',
    'today_date': date.today().strftime(today_fmt),
}

# -- RST configuration (for .rst content pages) -----------------------------

numfig = True

rst_epilog = f"""

.. |release| replace:: {release}
.. |version| replace:: {version}
"""

# -- Intersphinx -------------------------------------------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

# -- HTML output -------------------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
templates_path = ['_templates']

html_css_files = [
    'custom.css',
    'extra.css',
]

html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'collapse_navigation': True,
    'navigation_depth': 3,
}

# -- EPUB output -------------------------------------------------------------

epub_show_urls = 'footnote'

# -- Custom config values ----------------------------------------------------

def setup(app):
    app.add_config_value('under_development', False, 'env')
