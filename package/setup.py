import os
from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    readme = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'colda', '__version__.py')) as f:
    exec(f.read(), about)

print('-----', find_packages())
setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],
    url=about['__url__'],
    license=about['__license__'],
    packages=find_packages(),
    package_dir={'colda': 'colda'},
    long_description=readme,
    long_description_content_type='text/markdown',
    python_requires='>=3.7',
    install_requires=requirements,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
    ],
    keywords='colda, collaborative data analysis, data science, machine learning',
)


