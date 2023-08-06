import logging as log
import json
import os

DEFAULT_CONFIG = {
    "beamng_binary": "BeamNG.research.x64.exe",
    "beamng_extension": "util_researchAdapter",
    "ipc_host": "127.0.0.1",
    "ipc_port": 64256,
}


class Config(dict):
    """
    Configuration class which mainly wraps around a dictionary to offer access
    to keys as members. Instead of `spam["eggs"]`, it"s possible to simply go
    `spam.eggs`.
    """

    def __getstate__(self):
        return self.__dict__.items()

    def __setstate__(self, items):
        for key, val in items:
            self.__dict__[key] = val

    def __getattr__(self, key):
        return super().__getitem__(key)

    def __setattr__(self, key, val):
        return super().__setitem__(key, val)

    def load_values(self, dic):
        """
        Loads every key-value pair from the given dictionary into the config.
        """
        for key, val in dic.items():
            self[key] = val

    def load(self, cfg_file):
        """
        Loads every key-value pair in the given json file into the config.
        """
        with open(cfg_file) as in_file:
            cfg_str = in_file.read()
            cfg_json = json.loads(cfg_str)
        self.load_values(cfg_json)

    def save(self, cfg_file):
        """
        Saves every key-value pair of this config into the given json file.
        """
        with open(cfg_file, "w") as out_file:
            cfg_str = json.dumps(self, indent=4, sort_keys=True)
            out_file.write(cfg_str)


def get_default():
    """
    Creates and returns an instance of the `Config` class with the default
    value for each option.
    """
    default = Config()
    default.load_values(DEFAULT_CONFIG)
    return default


def ensure_config(cfg_file):
    """
    Tests if the given cfg_file path points to a configuration file. If not, a
    default configuration will be written to that file. The file is then loaded
    into the `CFG` field.
    """
    if not os.path.exists(cfg_file):
        default = get_default()
        default.save(cfg_file)
        log.debug("Saved fresh default cfg to: %s", cfg_file)

    CFG.load(cfg_file)


CFG = get_default()
