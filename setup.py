#!/usr/bin/env python


from setuptools import setup, find_packages


def parse_requirements(filename):
    with open(filename, "r") as f:
        for line in f:
            if line and line[:2] not in ("#", "-e"):
                yield line.strip()


setup(
    name="router",
    version="0.0.1",
    description="Message Router",
    long_description=open("README.rst", "r").read(),
    author="James Mills",
    author_email="James Mills, prologic at shortcircuit dot net dot au",
    url="https://github.com/openknot/router",
    download_url="https://github.com/openknot/router/archive/master.zip",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2.7",
    ],
    license="TBA",
    keywords="message router",
    platforms="POSIX",
    packages=find_packages("."),
    install_requires=list(parse_requirements("requirements.txt")),
    scripts=["router.py"],
    zip_safe=False
)
