# Configuration file for the Sphinx documentation builder.
# Docs: https://www.sphinx-doc.org/en/master/usage/configuration.html

from __future__ import annotations
import os
import sys
from pathlib import Path

# ── Make the repo root (where manage.py lives) importable
HERE = Path(__file__).resolve()
ROOT = HERE.parents[2]                     # source -> docs -> REPO_ROOT
sys.path.insert(0, str(ROOT))

# ── Configure Django so autodoc can import your project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "minions_site.settings")

# Best-effort: load local .env (SECRET_KEY, DEBUG, ALLOWED_HOSTS, etc.)
try:
    from dotenv import load_dotenv  # optional; ignore if not installed
    load_dotenv(ROOT / ".env")
except Exception:
    pass

try:
    import django  # type: ignore
    django.setup()
except Exception as e:
    # Avoid hard-failing during edits; the build log will show this message
    print(f"[sphinx/conf.py] Django setup skipped/failed: {e}")

# ── Project information ────────────────────────────────────────────────────────
project = "minions_site"
author = "Minnie"
copyright = "2025, Minnie"
release = "0.1.0"
language = "en"

# ── General configuration ─────────────────────────────────────────────────────
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",        # Google/NumPy style docstrings
    "sphinx_autodoc_typehints",   # nicer type hints in docs
    "sphinx.ext.viewcode",        # add [source] links to documented objects
]

autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "show-inheritance": True,
}
autodoc_typehints = "description"   # keep signatures clean; move hints into text

# Napoleon tweaks (optional, sensible defaults)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_private_with_doc = False
napoleon_use_param = True
napoleon_use_rtype = True

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# ── HTML output ───────────────────────────────────────────────────────────────
html_theme = "alabaster"            # keep default theme (no extra install)
html_static_path = ["_static"]      # leave as-is even if folder is empty
