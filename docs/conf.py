"""Sphinx configuration."""
project = "Notify"
author = "Garrett M. Shipley"
copyright = "2022, Garrett M. Shipley"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
