# Python Release Plugin

This release plugin is intended to be used in conjunction with setuptools to enable building and
releasing a Python module with a single setuptools command `release`. Running the command results
in the following:

- building the project (as would be accomplished via `python setup.py clean bdist_wheel`
- update the module version file
- updating the project's changelog to reflect the changes in the latest release
- git committing, tagging, and pushing the changes

## How do I use it?

First, you must include it in your own module's `setup.py` script as a `setup_requires`
dependency. Then the command needs to be added to the `cmd_class` dictionary that gets passed to
the `setup` function. The example snippet below illustrates how you would accomplish these first
two steps:

```python
from pyreleaseplugin import CleanCommand, ReleaseCommand

setup(
    name="awesomepossum",
    version=__version__,
    author="Mr. Awesome Pants",
    author_email="mrawesomepants@theawesomefactory.com",
    description="Everything is awesome",
    license="TBD",
    keywords="awesomeness",
    setup_requires=["pyreleaseplugin>=0.1"],
    cmdclass={"release": ReleaseCommand, "clean": CleanCommand})
```

In addition to setuptools command `ReleaseCommand`, you'll notice that the module includes a
`CleanCommand` command and a `PyTest` command as well. These are for convenience. The clean command
cleans more aggressively than the default setuptools equivalent, which is important for ensuring
that we publish the correct artifacts. The test command allows us to execute tests using `py.test`
with the following one-liner:

```sh
python setup.py test
```

Use the following command at your favorite Unix shell prompt to release your module:

```sh
python setup.py release
```

You may optionally include a version. If none is provided, the module's patch number will be
incremented. You may also provide a description to include in the changelog. If none is provided,
you will be prompted to enter one later.

The command also requires a configuration file to indicate where the changelog and version files lives in the project. An example of a simple configuration file called `setup.cfg` looks as follows:

```
[release]
version-file = awesomepossum/_version.py
changelog-file = CHANGELOG.md
```

The configuration file to be used can be specified as a command-line argument to the release
command. If it is not specified, the default of `setup.cfg` is expected to exist in the current
directory.
