"""Python Package Definition."""

import os
from setuptools import find_packages, setup


root = os.path.dirname(__file__)
src = os.path.relpath(os.path.join(root, "python"))
readme = open(os.path.join(root, "README.md")).read()

setup(
    name="moet",
    version="0.1.0",
    description="Build a tower of glasses. Fill them with champagne!",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/ylathouris/moet",
    author="Yani Lathouris",
    author_email="ylathouris@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.7, <4",
    keywords="io, load, dump, read, write, parse, format, utils",
    project_urls={
        "Say Thanks!": "http://saythanks.io/to/ylathouris",
        "Source": "https://github.com/ylathouris/moet",
        "Tracker": "https://github.com/ylathouris/moet/issues",
    },
    package_dir={"": src},
    packages=find_packages(src),
    entry_points={
        'console_scripts': [
            'moet = moet.cli:moet',
        ],
    },
    install_requires=[],
)
