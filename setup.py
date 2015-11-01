from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='birdseed',

    version='0.2.0',

    description='Twitter random number seeder/generator',
    long_description=long_description,

    url='https://github.com/ryanmcdermott/birdseed',

    author='Ryan McDermott',
    author_email='ryan.mcdermott@ryansworks.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='random sysadmin development',

    py_modules=['birdseed'],

    install_requires=['twitter>=2.2'],
)