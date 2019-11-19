# Changelog

All notable changes to this project will be documented in this file.

0.2.11 (2019-11-19)
-------------------
""

0.2.10 (2018-11-30)
-------------------
"update es client and models with latest mapping changes"

0.2.9 (2018-04-16)
------------------
- Fixed to check for changes before attempting to commit (since `git commit` w/o changes exits non-zero)

0.2.8 (2018-04-13)
------------------
- Added `no-update-changelog` option to support releases with no CHANGELOG file

0.2.7 (2018-04-12)
------------------
- Testing release again

0.2.6 (2018-04-12)
------------------
- Testing the release process

0.2.4 (2018-04-11)
------------------
- Added "--no-bump-version" option to support projects that manually set version

0.2.3 (2017-01-10)
------------------
- Remove twine in favor of setuptools upload

0.2.2 (2016-12-06)
------------------
"Initial release from Jenkins"

0.2.1 (2016-12-06)
------------------
- Specify branch name when pushing to support pushing from Jenkins

0.2.0 (2016-12-02)
------------------
- Parameterized release options so that releases can happen from Jenkins in non-interactive mode

0.1.1 (2016-07-22)
------------------
- Now using in setup.py the clean and test commands defined in the module
- Added PyTest command

0.1.0 (2016-07-21)
------------------
Initial release