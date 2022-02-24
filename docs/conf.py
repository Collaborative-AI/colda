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
import os
import sys
import sphinx_rtd_theme
# import synspot
# sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


# -- Project information -----------------------------------------------------

project = 'Synspot'
copyright = '2022, Jie_Ding_Group'
author = 'Jie_Ding_Group'

# The full version, including alpha/beta/rc tags
release = '0.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import recommonmark
from recommonmark.transform import AutoStructify
source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
}
source_suffix = ['.rst', '.md']

extensions = [
   'sphinx.ext.todo', 
   'sphinx.ext.viewcode', 
   'sphinx.ext.autodoc',
   'sphinx_copybutton',
   'sphinx_issues',
   'sphinx_removed_in',
   "sphinx.ext.intersphinx",
   "sphinx.ext.viewcode",
   "sphinxext.opengraph",
   'nbsphinx', 
   'recommonmark']

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
# html_static_path = ["resources"]
# The master toctree document.
master_doc = "index"

# -- Options for HTML output -------------------------------------------------

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# html_theme = 'pytorch-sphinx-theme'
html_logo = "resources/Synspot.jpg"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
html_static_path = ["resources"]
# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# If true, Sphinx will warn about all references where the target cannot be found.
# Default is False. You can activate this mode temporarily using the -n command-line
# switch.
nitpicky = True



def setup(app):
    app.add_js_file("js/script.js")
    app.add_css_file("css/styles.css")
    app.add_css_file("css/dark.css")
    app.add_css_file("css/light.css")


# GitHub repo for sphinx-issues
issues_github_path = "python-pillow/Pillow"