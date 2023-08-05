#!/usr/bin/env python

from setuptools import setup


long_description = """
Hap! is an HTML parser and scraping tool written in Python.

The purpose of Hap! is to have a simple and fast way to retrieve certain data from the internet. It uses JSON formatted data as input and output. Input can be either from a local file or from stdin from another process. Output is either printed to stdout or saved to file. If input is provided by file, Hap! names it dataplan ("data planning") and the same file is used when the output is saved.
"""

setup(name="hap",
    packages=[
        "hap",
    ],
    entry_points = {
        "console_scripts": [
            "hap = hap.bootstrap:main"
        ]
    },
    install_requires=[
        "lxml==3.6.4",
        "cssselect==1.0.0",
    ],
    version="1.0.2",
    description="A simple HTML scraping tool",
    long_description=long_description,
    author="Alexandru Catrina",
    author_email="alex@codeissues.net",
    license="MIT",
    url="https://github.com/lexndru/hap",
    download_url="https://github.com/lexndru/hap/archive/v1.0.2.tar.gz",
    keywords=["html", "scraping", "crawler", "tool", "hap"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Text Processing :: Markup :: HTML",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
    ],
)
