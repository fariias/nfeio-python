#-*- coding: utf-8 -*-

from setuptools import setup, find_packages


NAME = 'nfeio-python'
VERSION = '1.0.0'
DESCRIPTION = 'NFE.IO Python'
LONG_DESCRIPTION = 'Python Library For NFE.IO API'
URL = 'https://github.com/fariias/nfeio-python'
KEYWORDS = 'invoice, nfe.io'

PACKAGES = find_packages()

AUTHOR = 'Josenildo Junior'
AUTHOR_EMAIL = 'josenildoaf@gmail.com'

setup(name=NAME,
      version=VERSION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      packages=PACKAGES,
      url=URL,
      keywords=KEYWORDS,
      py_modules=[],
      tests_require=['pytest'])