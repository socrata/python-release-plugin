import os
import sys

from pyreleaseplugin import CleanCommand, ReleaseCommand, PyTest
from setuptools import find_packages, setup, Command


def read(fname):
    """Utility function to read the README file into the long_description."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


install_requires_list = ["twine>=1.7"]
tests_require = ["pytest>=2.9"]


version_file = "pyreleaseplugin/_version.py"
with open(version_file) as fp:
    exec(fp.read())

setup(
    name="pyreleaseplugin",
    version=__version__,
    author="The Discovery Team",
    author_email="discovery-l@socrata.com",
    description=("A setuptools plugin for simplifying the release of Python modules"),
    license="TBD",
    url="https://github.com/socrata/python-release-plugin",
    install_requires=install_requires_list,
    tests_require=tests_require,
    include_package_data=True,
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Socrata",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    cmdclass={"test": PyTest, "clean": CleanCommand, "release": ReleaseCommand})
