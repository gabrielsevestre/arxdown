import setuptools
from arxdown import meta

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name=meta.name,
    version=meta.version,
    author="Gabriel Sevestre",
    author_email="gabriel.sevestre@gmail.com",
    description=meta.description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabrielsevestre/arxdown",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    keywords="arxiv downloader",
    entry_points={"console_scripts": ["arxdown = arxdown.__main__:main"]},
    extras_require={"ZiX": "uncompyle6>=3.5.0"},
)
