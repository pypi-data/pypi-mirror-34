'''
setup for pypi package
'''
from setuptools import setup
import re
import os

version = "0.2.5"

setup(
    name='xlparser',
    version=version,
    python_requires='>=3.6.1',

    package_dir={"": "."},
    py_modules=['xlparser'], 
    install_requires=['xlrd', 'openpyxl>=2.5.4'],
    scripts=['xlparser.py'],
    description=open('README.md').readlines()[1],
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="ahuigo",
    author_email="ahui132@qq.com",
    license="MIT",
    url="http://github.com/ahuigo/xlparser",
)
