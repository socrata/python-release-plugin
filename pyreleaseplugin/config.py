from configparser import ConfigParser


class ReleaseConfig:
    def __init__(self, config):
        self._config = config

    @property
    def version_file(self):
        """
        str: The version specifier file
        """
        return self._config["python-file-with-version"]

    @property
    def changelog_file(self):
        """
        str: The changelog file
        """
        return self._config["changelog-file"]

    @classmethod
    def load(cls, filename):
        """
        Instantiate a Config from the config file at the path specfied in `filename`.

        It is expected that the config file specified by `filename` has a section named "release".

        Args:
            filename (str): The path to the config file

        Returns:
            configparser.ConfigParser
        """
        config = ConfigParser()
        config.read(filename)        
        return cls(config["release"])
