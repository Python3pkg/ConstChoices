# coding=utf8

from __future__ import unicode_literals


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import ConstChoices


lib_classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
]

setup(name="ConstChoices",
      version='0.1.0',
      author="kinegratii",
      author_email="kinegratii@gmail.com",
      url="https://github.com/kinegratii/ConstChoices",
      keyword="choices const",
      tests_require=["pytest"],
      py_modules=["ConstChoices"],
      install_requires=['six'],
      description="A enhance module using class-style define for const choices.",
      license="MIT",
      classifiers=lib_classifiers
      )
