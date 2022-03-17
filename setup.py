#!/usr/bin/env python3

import os
from setuptools import setup, find_packages

# get key package details from Synspot/__version__.py
about = {}  # type: ignore
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'Synspot', '__version__.py')) as f:
    exec(f.read(), about)

# load the README file and use it as the long_description for PyPI
with open('README.md', 'r') as f:
    readme = f.read()

# package configuration - for reference see:
# https://setuptools.readthedocs.io/en/latest/setuptools.html#id9
print('-----', find_packages())
setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],

    # 项目主页
    url=about['__url__'],

    # 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
    packages=find_packages(),
    include_package_data=True,
    package_dir={'synspot': 'synspot'},
    # 希望被打包的文件
    package_data={'synspot_Data': ['synspot_Data/*']},

    # entry_points={
    #     'console_scripts': ['synspot=synspot.__init__'],
    # },

    long_description=readme,
    long_description_content_type='text/markdown',
    
    # packages=['synspot'],

    python_requires=">=3.7.*",
    install_requires=[
        'numpy', 
        'requests', 
        'scikit-learn',
        'scipy',
        'matplotlib',
        'torch',
        'pandas',
        ],

    license=about['__license__'],
    zip_safe=False,
    
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='synspot'
)
