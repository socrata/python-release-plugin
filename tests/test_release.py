import os
import shutil
import tempfile
import unittest
from datetime import datetime

from pyreleaseplugin.release import add_changelog_entry
from pyreleaseplugin.release import bump_patch_version
from pyreleaseplugin.release import current_version_from_version_file
from pyreleaseplugin.release import update_version_file

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


def copy_to_tempfile(src_filename, tmp_filename):
    with open(src_filename) as infile:
        with open(tmp_filename, 'w') as outfile:
            shutil.copyfileobj(infile, outfile)


class TestRelease(unittest.TestCase):
    def setUp(self):
        self.version_file = os.path.join(THIS_DIR, "resources", "_version.py")
        self.changelog_file = os.path.join(THIS_DIR, "resources", "CHANGELOG.md")

    def test_current_version_from_version_file(self):
        self.assertEquals("0.2.5", current_version_from_version_file(self.version_file))

    def test_bump_patch_version(self):
        version = "0.1.0"
        expected = "0.1.1"
        actual = bump_patch_version(version)
        self.assertEquals(expected, actual)

    def test_updpate_version_file(self):
        tmp = tempfile.NamedTemporaryFile(mode='r')
        copy_to_tempfile(self.version_file, tmp.name)
        version_file = tmp.name
        update_version_file(version_file, "7.8.9")
        try:
            self.assertEquals("7.8.9", current_version_from_version_file(version_file))
        except:
            tmp.close()
            raise

    def test_add_changelog_entries(self):
        tmp = tempfile.NamedTemporaryFile(mode='r')    
        copy_to_tempfile(self.changelog_file, tmp.name)
        changelog_file = tmp.name
        new_version = "0.1.0"
        add_changelog_entry(changelog_file, new_version, "Initial release")
        today = datetime.today().strftime("%Y-%m-%d")
        expected = "# Changelog\n\n" + \
                   "All notable changes to this project will be documented in this file.\n\n" + \
                   "0.1.0 ({})\n------------------\nInitial release".format(today)
        with open(changelog_file, "r") as infile:
            changelog_contents = infile.read()
            try:
                self.assertEquals(expected, changelog_contents)
            except:
                tmp.close()
                raise

        # test adding again
        new_version = "0.1.1"
        add_changelog_entry(changelog_file, new_version, "First patch release")
        expected = "# Changelog\n\n" + \
                   "All notable changes to this project will be documented in this file.\n\n" + \
                   "0.1.1 ({})\n------------------\nFirst patch release\n\n".format(today) + \
                   "0.1.0 ({})\n------------------\nInitial release".format(today)
        with open(changelog_file, "r") as infile:
            changelog_contents = infile.read()
            try:
                self.assertEquals(expected, changelog_contents)
            except:
                tmp.close()
                raise
