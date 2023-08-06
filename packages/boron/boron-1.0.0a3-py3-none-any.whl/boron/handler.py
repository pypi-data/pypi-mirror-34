from ghh import configuration


class Handler:
    def __init__(self, config_file=None):
        self.configuration = configuration.Configuration(config_file)
