# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os
import sys
import glob

# -- Add current project where running from
sys.path.append(os.path.abspath(".."))

# -- Project information -----------------------------------------------------

project = 'mini-project'

import time
copyright = u'%s, Ruben De Campos / Samuel Michel' % time.strftime("%Y")
author = 'Ruben De Campos / Samuel Michel'


# -- General configuration ---------------------------------------------------

needs_sphinx = "1.3"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.graphviz",
    "sphinx.ext.napoleon"
]

# Be picky about warnings
nitpicky = False

# Ignores stuff we can't easily resolve on other project's sphinx manuals
nitpick_ignore = []

autosummary_generate = True

# If we are on OSX, the 'dvipng' path maybe different
dvipng_osx = "/opt/local/libexec/texlive/binaries/dvipng"
if os.path.exists(dvipng_osx):
    pngmath_dvipng = dvipng_osx



# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = ".rst"

master_doc = "index"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'bizstyle'


# Default processing flags for sphinx
autoclass_content = "class"
autodoc_member_order = "bysource"
autodoc_default_flags = [
    "members",
    "undoc-members",
    "show-inheritance",
]


intersphinx_mapping = dict(
    python=('https://docs.python.org/3', None),
    numpy=("https://numpy.org/doc/stable/", None),
    scipy=("https://docs.scipy.org/doc/scipy/reference", None),
)