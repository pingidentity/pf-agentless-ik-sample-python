import configparser
import os
from urllib.parse import urlparse

from sample_applications.AgentlessSpSample.Utils.SpConstants import SpConstants


class ConfigurationManager:

    configuration = dict()

    def __init__(self):
        self.load_configuration()

    @classmethod
    def load_configuration(cls):
        current_dir = os.path.dirname(__file__)
        rel_path = "sp-adapter-configuration.ini"
        config_dir = os.path.join(current_dir, rel_path)

        config = configparser.ConfigParser()
        config.optionxform = str
        config.read(config_dir)
        for sect in config.sections():
            cls.configuration = dict(config.items(sect))

    @classmethod
    def save_configuration(cls, request):
        current_dir = os.path.dirname(__file__)
        rel_path = "sp-adapter-configuration.ini"
        config_dir = os.path.join(current_dir, rel_path)

        config = configparser.ConfigParser(allow_no_value=True)
        config.optionxform = str
        config.read(config_dir)

        config.set(SpConstants.CONFIG_SECTION, "# SP adapter configuration for the SP Sample")
        config.set(SpConstants.CONFIG_SECTION, "# For sample simplicity, configuration information in project")
        config.set(SpConstants.CONFIG_SECTION, "# Never leave credentials in area accessible in production")

        for config_key in request.form:
            if config_key != "submit":
                if cls.is_config_valid(config_key, request.form[config_key]):
                    config.set(SpConstants.CONFIG_SECTION, config_key, request.form[config_key])
                else:
                    raise Exception('Please check configuration of ' + config_key)

        with open(config_dir, 'w') as config_file:
            config.write(config_file)

    @classmethod
    def get_configuration(cls, key):
        return cls.configuration.get(key)

    @staticmethod
    def is_config_valid(key, value):
        if key == SpConstants.BASE_PF_URL:
            parsed_url = urlparse(value)
            return all([parsed_url.scheme in ["http", "https"], parsed_url.netloc])
        elif key == SpConstants.ADAPTER_USERNAME:
            return value
        elif key == SpConstants.ADAPTER_PASSWORD:
            return value
        elif key == SpConstants.ADAPTER_ID:
            return value
        elif key == SpConstants.TARGET_URL:
            parsed_url = urlparse(value)
            return all([parsed_url.scheme in ["http", "https"], parsed_url.netloc])
        elif key == SpConstants.PARTNER_ENTITY_ID:
            return value
        else:
            return False
