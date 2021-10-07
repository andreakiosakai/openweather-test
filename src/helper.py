import configparser
import os
from pathlib import Path


class Helper:
    
    def get_config():
        path = Path(__file__)
        ROOT_DIR = path.parent.absolute()
        config_path = os.path.join(ROOT_DIR, "config/env.cfg")
        config = configparser.RawConfigParser()
        config.read(config_path)
        config_dict = dict(config.items('OPEN_WEATHER'))
        return config_dict