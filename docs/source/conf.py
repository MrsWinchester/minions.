# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from __future__ import annotations
import os
import sys
from pathlib import Path

# ── Make the repo root (where manage.py lives) importable
ROOT = Path(__file__).resolve().parents[2]   # source -> docs -> REPO_ROOT
sys.path.insert(0, str(ROOT))

# ── Configure Django so autodoc can import your project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "minions_site.settings")

# 1) Try to load .env (safe if missing)
try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
except Exception:
    pass  # ok if python-dotenv isn't installed

# 2) Now set up Django for autodoc
try:
    import django  # type: ignore
    django.setup()
except Exception as e:
    print(f"[sphinx/conf.py] Django setup skipped/failed: {e}")

# (optional) avoid hard dependency during docs build
autodoc_mock_imports = ["dotenv"]
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = "minions_site"
copyright = "2025, Minnie"
author = "Minnie"
release = "0.1.0"
language = "en"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",        # Google/NumPy style docstrings
    "sphinx_autodoc_typehints",   # pretty type hints in docs
]
autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
}
templates_path = ["_templates"]
exclude_patterns: list[str] = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "alabaster"          # or install/use "sphinx_rtd_theme"
html_static_path = ["_static"]
