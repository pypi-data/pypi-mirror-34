# -*- coding: utf-8 -*-
from distutils.core import setup

modules = \
['threadop']
setup_kwargs = {
    'name': 'threadop',
    'version': '0.1.0',
    'description': 'Adds a threading operator to Python.',
    'long_description': None,
    'author': 'Bogdan Popa',
    'author_email': 'popa.bogdanp@gmail.com',
    'url': None,
    'py_modules': modules,
}


setup(**setup_kwargs)
