# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

classifiers = [
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
]


setup(
    name='django-geo',
    version='0.0.1',
    description='Geo app for django',
    # long_description=open('README.md').read(),
    author='Troy Grosfield',
    author_email='troy.grosfield@gmail.com',
    url='https://github.com/troygrosfield/django-geo',
    # license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
    setup_requires=[
        'django >= 1.5.1',
    ],
    classifiers=classifiers
)
