from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="s_test",
    version="0.0.3",
    author="shudarong",
    author_email="610780856@qq.com",
    description="A Python library for test.",
    long_description=open("README.rst").read(),
    license="MIT",
    url="https://github.com/shudarong/s_test",
    packages=['s_test'],
    classifiers=[
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
		'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: Multimedia :: Video',
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    zip_safe=True,
)