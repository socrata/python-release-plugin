import os
import sys
from setuptools import find_packages, setup, Command
from setuptools.command.test import test as TestCommand


def read(fname):
    """Utility function to read the README file into the long_description."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


install_requires_list = []
tests_require = ["pytest>=2.9"]


class CleanCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')


class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


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
    cmdclass={"test": PyTest, "clean": CleanCommand})
