Flow for Automated Documentation:
1. Navigate to docs/
2. Run: pipenv run sphinx-quickstart
  Separate source and build directories: n
3. Navigate to docs/conf.py
4. Uncommen and Change:
    import os
    import sys
    sys.path.insert(0, os.path.abspath('..'))
5. Change extions=['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc', 'nbsphinx']
6. Add (to support md): import recommonmark
        from recommonmark.transform import AutoStructify
        source_parsers = {
          '.md': 'recommonmark.parser.CommonMarkParser',
        }
source_suffix = ['.rst', '.md']
7. Change html_theme='sphinx_rtd_theme'
8. Navigate to docs/index.rst
9. Add modules, README, demo under :caption: Contents: 
10. Run: sphinx-apidoc -o . ..
11. Run: make clean
12. Run: make html