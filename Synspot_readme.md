Cur Template:
https://github.com/AlexIoannides/py-package-template


scikit-learn = "*"
scipy = "*"
matplotlib = "*"
torch = "*"
torvision

Call Function before Ctrl+C:
1. https://stackoverflow.com/questions/368927/call-a-function-when-the-program-is-finished-with-ctrl-c/376059
2. https://qminghe.com/post/2019/06/08/dive-into-python-signal

Accept Logic:
Another thread:
1. getNotification()
2. if active: show in terminal
3. user select(Y/N) to accept the request


4. user can call get_pending_requests() => show list of requests with information


private(__), public, protected(_) in python.

1. send request
2. import

--
1. Package:


unittest:
1. run command: pytest


Flow for Automated Documentation:
1. Navigate to docs/
2. Run: pipenv run sphinx-quickstart
  Separate source and build directories: n

3. Navigate to docs/conf.py
4. Uncommen and Change:
    import os
    import sys
    sys.path.insert(0, os.path.abspath('..'))
5. Change extions=['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']
5. Change html_theme='sphinx_rtd_theme'
6. Navigate to docs/index.rst
7. Add modules under :caption: Contents:
8. Run: sphinx-apidoc -o . ..
9. Run: make html
