# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------

project = 'Stingray Notebooks'
author = 'Your Name'

# The full version, including alpha/beta/rc tags
release = '0.1'

# -- General configuration ---------------------------------------------------

extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'

html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------

# nbsphinx options
nbsphinx_execute = 'always'
