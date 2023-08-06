#!/usr/bin/env python

from setuptools import setup

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945
import codecs
try:
    codecs.lookup('mbcs')
except LookupError:
    ascii = codecs.lookup('ascii')
    codecs.register(lambda name, enc=ascii: {True: enc}.get(name == 'mbcs'))

VERSION = '0.5.3'

setup(
    name='pygraphenelib',
    version=VERSION,
    description='Python library for graphene-based blockchains',
    long_description=open('README.md').read(),
    download_url='http://pygraphenelib' + VERSION,
    author='Starry Zhang',
    author_email='463834772@qq.com',
    maintainer='Starry Zhang',
    maintainer_email='463834772@qq.com',
    url='http://pygraphenelib',
    keywords=[
        'graphene',
        'api',
        'rpc',
        'ecdsa',
        'secp256k1'
    ],
    packages=["grapheneapi",
              "graphenebase",
              ],
    install_requires=["ecdsa",
                      "requests",
                      "websocket-client",
                      "pylibscrypt",
                      "pycryptodome",
                      ],
    classifiers=['License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3',
                 'Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    include_package_data=True,
)
