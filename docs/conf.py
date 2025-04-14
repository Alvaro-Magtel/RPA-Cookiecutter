"""Sphinx configuration."""

project = "RPA AS"
author = "Alvaro Prieto Cano"
copyright = "2025, Alvaro Prieto Cano"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
