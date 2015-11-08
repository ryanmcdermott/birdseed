from setuptools import setup

setup(
    name='birdseed',

    version='0.2.3',

    description='Twitter random number seeder/generator',

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

    install_requires=['twitter>=1.17.1'],
)