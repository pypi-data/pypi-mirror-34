from __future__ import print_function, absolute_import, division


from ast import literal_eval
from setuptools import setup


def get_version(source='petl/__init__.py'):
    with open(source) as f:
        for line in f:
            if line.startswith('__version__'):
                return literal_eval(line.split('=')[-1].lstrip())
    raise ValueError("__version__ not found")


setup(
    name='petl',
    version=get_version(),
    author='Alistair Miles',
    author_email='alimanfoo@googlemail.com',
    package_dir={'': '.'},
    packages=['petl', 'petl.io', 'petl.transform', 'petl.util',
              'petl.test', 'petl.test.io', 'petl.test.transform',
              'petl.test.util'],
    scripts=['bin/petl'],
    url='https://github.com/alimanfoo/petl',
    license='MIT License',
    description='A Python package for extracting, transforming and loading '
                'tables of data.',
    long_description=open('README.txt').read(),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=['Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Topic :: Software Development :: Libraries :: Python Modules'
                 ]
)
