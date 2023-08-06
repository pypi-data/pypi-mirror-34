import yaml

from ghh.errors import ConfigurationException


REQUIRED_PARAMETERS = ['event_handlers']


class Configuration:
    def __init__(self, config_file=None):
        try:
            raw_config = yaml.load(config_file)
            for key in raw_config:
                setattr(self, key, raw_config[key])
        except Exception as e:
            raise ConfigurationException(config_file)

        for parameter in REQUIRED_PARAMETERS:
            if not hasattr(self, parameter):
                raise ConfigurationException(parameter)
