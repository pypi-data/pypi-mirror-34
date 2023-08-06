class ServerError(Exception):
    pass


class ConfigurationException(Exception):
    def __init__(self, config_file):
        self.msg = f"Configuration file {config_file.name} could not be parsed. Please see documentation."


class MissingRequiredConfigurationParameters(Exception):
    def __init__(self, parameter):
        self.msg = f"Missing required parameter {parameter}."
