# This Package Introduction File is Divided into Following Parts:
* Package Basic Structure
* How to Manage Package Environment
* How to Generate Documentation
* How to Polish Documentation
* How to Package Package
* Some Notable Points

-------------------------------------

## 1. Package Basic Stucture

- Basic package structure can be found in [Github repository](https://github.com/AlexIoannides/py-package-template)

- Compared to the Basic package structure, ``docs/`` will contain different element. But at this point, you can follow the template.

- ``py-pkg`` is the main part of the package, you can add more modules (with ``__init__.py``) in this part. For example, if you add ``temp`` module, you can import ``temp`` module by:

> ```bash
import temp from py-pkg
> ```

- **This package structure can be improved by learning [PyTorch](https://github.com/pytorch/pytorch) package structure.**

- Basic Structure: 

> ```bash
py-package-tempate/
 |-- docs/
 |-- |-- build_html/
 |-- |-- build_latex/
 |-- |-- source/
 |-- py-pkg/
 |-- |-- __init__.py
 |-- |-- __version__.py
 |-- |-- curves.py
 |-- |-- entry_points.py
 |-- tests/
 |-- |-- test_data/
 |-- |   |-- supply_demand_data.json
 |-- |   __init__.py
 |-- |   conftest.py
 |-- |   test_curves.py
 |-- .env
 |-- .gitignore
 |-- Pipfile
 |-- Pipfile.lock
 |-- README.md
 |-- setup.py
> ```

---------------------------------------------

## 2. How to Manage Package Environment

- ``pipenv`` is used to manage package. You can install ``pipenv`` by:
> ```bash
pip3 install pipenv
> ```

- Use ``pipenv`` to install package. The first command is to install the package for development. The second command is to install the package for production.

> ```bash
pipenv install --dev
pipenv install 
> ```

- Use ``pipenv`` to uninstall package:
> ```bash
pipenv uninstall
> ```

#### Pipenv Shells

- Entering into a Pipenv-managed shell. Remeber doing this **every time** before running the project. 

> ```bash
cd py-package-tempate
pipenv install
pipenv shell
> ```

---------------------------------------------

## 3. How to Generate Documentation

- We will use ``Sphinx`` to generate documentation.

- From part 1, now you may have  build_html, build_latex, source in your ``docs/`` file. You can delete them all. 

- ``docs/`` folder stores all the files we need to modify documentation. Mostly, We need to modify ``.rst`` file to manipulate the structure. Here are some information about the ``.rst`` grammar:
  1. [Yehuo](https://ebf-contribute-guide.readthedocs.io/_/downloads/zh_CN/stable/pdf/)
  2. [Quick reStructuredText](https://docutils.sourceforge.io/docs/user/rst/quickref.html)

- **The documentation style is refer to [Pillow](https://pillow.readthedocs.io/en/stable/reference/index.html), and the [Pillow Code](https://github.com/python-pillow/Pillow). If this introduction is unclear, you can find the display you want ([Pillow](https://pillow.readthedocs.io/en/stable/reference/index.html)) and find the corresponding code in ([Pillow Code](https://github.com/python-pillow/Pillow))**.

#### Flow to generate documentation:
> 1. **Navigate** to ``docs/``
> 2. **Execute**: 
>> ```bash
pipenv run sphinx-quickstart
>> ```
  Separate source and build directories: n
> 3. **Navigate** to ``docs/conf.py``
> 4. You can replace the conf.py directly with the uploaded ``conf.py`` and jump to step 12
> 5. **Uncommen** and **Change**:
>>    import os
>>    import sys
>>    sys.path.insert(0, os.path.abspath('..'))

> 6. **Change**:
>> extensions=['sphinx.ext.todo', 
>>             'sphinx.ext.viewcode', 
>>             'sphinx.ext.autodoc',
>>             'sphinx_copybutton',
>>             'sphinx_issues',
>>             'sphinx_removed_in',
>>             'sphinx.ext.intersphinx',
>>             'sphinx.ext.viewcode',
>>             'sphinxext.opengraph',
>>             'nbsphinx', 
>>             'recommonmark']

> 7.  **Install** some dependencies:
>>       pipenv install --dev sphinx-copybutton
>>       pipenv install --dev sphinx
>>       pipenv install --dev sphinx-issues
>>       pipenv install --dev sphinx-removed-in
>>       pipenv install --dev sphinxext-opengraph

> 8. **Add** (to support md file):  
>> import recommonmark
>> from recommonmark.transform import AutoStructify
>> source_parsers = {
>>    '.md': 'recommonmark.parser.CommonMarkParser',
>> }
>> source_suffix = ['.rst', '.md']

> 9. **Change** or **Add**:  
>> html_theme='sphinx_rtd_theme'
>> html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
>> html_static_path = ["resources"]

> 10. **Add**:
>>  def setup(app):
             app.add_js_file("js/script.js")
>>           app.add_css_file("css/styles.css")
>>           app.add_css_file("css/dark.css")
>>           app.add_css_file("css/light.css")

> 11. **Put** the uploaded ``resources/`` folder under the ``docs/``
> 12. **Note that at this point, you have the conf.py that meets the minimum requirement. If you want to add more options, refer to [Pillow conf.py](https://github.com/python-pillow/Pillow/blob/main/docs/conf.py)**
> 13. **Navigate** to ``docs/index.rst``. index.rst is similar to ``__init__.py`` in python, which is needed in every module.
> 14. **Modify** the toctree:: part:
>>     .. toctree::
>>        :maxdepth: 2
>>        installation.rst
>>        handbook/index.rst
>>        reference/index.rst
>>        porting.rst
>>        about.rst
>>        releasenotes/index.rst
>>        deprecations.rst
>>        README.md

> 15. Explanation for step 13:
       **Note that you can leave these parts as the placeholders, or delete them if you dont need them.**
       ``installation.rst`` is to introduce the environment requirement and package installation
       ``handbook/index.rst`` is a directory
       ``reference/index.rst`` is the introduction of functions and classes.
       ``porting.rst`` contains information about compatible transactions.
       ``about.rst`` is a quick introduction
       ``releasenotes/index.rst`` records the information about the old version package.
       ``deprecations.rst`` records the deprecated functions.
       ``README.md``: You can add anything you want in this file
> 16. **Modify** ``.rst`` files. I offer 2 simple rst for function and class for your reference. One is ``function.rst``, the other one is ``class.rst``
> 17. **Execute**: make clean
> 18. **Execute**: make html

---------------------------------------------

## 4. How to Polish Documentation

- **Follow** the comment style for functions and classes:
> """
> Short introduction about the function or class
>
> :param a: introduction about a
> :param b: introduction about b
> 
> :returns: introduction about returning parameter
> 
> :exception OSError: introduction about raising error.
> """

- Here are some commanly used grammar in comment, you can test it using ``sphinx``
> """
> \`\`testing_text\`\` becomes red
> \*\*testing_text\*\* becomes bold
> :py:func:\`testing_text\` becomes text block
> """

- Here are some commanly used ``rst`` grammar:
> :file:\`testing_text\` => add text block to testing_text and text turns red
> .. code-block:: python => python code block
> .. note:: => Note block
> .. warning:: => Warning block

---------------------------------------------

## 5. How to Package Package

The whl file will be generated under ``dist/`` by executing following commands:

> ```bash
cd py-package-tempate
pipenv install wheel
python setup.py bdist_wheel
> ```


---------------------------------------------

## 5. Some Notable Points

1. You can modify correlated information in ``__version__.py``
2. The production packages needs to be listed in ``install_requires`` in ``setup.py``. For example, 
> install_requires=[
        'numpy', 
        'requests', 
        'scikit-learn',
        'scipy',
        'matplotlib',
        'torch',
        'pandas',
> ],