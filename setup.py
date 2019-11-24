#!/usr/bin/env python3

from setuptools import setup

setup(
    name="himblick",
    python_requires=">= 3.7",
    install_requires=['parted', 'progressbar'],
    version="1.0",
    description="Himblick setup and maintenance tool",
    author="Enrico Zini <enrico@enricozini.org>, Ulrike Uhlig <u@451f.org>",
    url="https://github.com/himblick/himblick",
    license="http://www.gnu.org/licenses/gpl-3.0.html",
    packages=["himblib"],
    scripts=['himblick'],
)