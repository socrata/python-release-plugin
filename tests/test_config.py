import os
import unittest

from pyreleaseplugin.config import ReleaseConfig

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


class TestReleaseConfig(unittest.TestCase):
    def setUp(self):
        test_cfg_file = os.path.join(THIS_DIR, "resources", "setup.cfg")
        self.config = ReleaseConfig.load(test_cfg_file)

    def test_config_declares_changelog(self):
        self.assertIsNotNone(self.config.changelog_file)

    def test_config_declares_version(self):
        self.assertIsNotNone(self.config.version_file)
