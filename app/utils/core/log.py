import logging

from app.configs.config import load_config
from .singleton import Singleton

class Logger(metaclass=Singleton):
    '''
    Initializes the logger according to the 
    settings.yaml
    '''
    
    def __init__(self):
        self.logger = self.__configure_logger()

    def __configure_logger(self):
        config = load_config()['logging']
        logger = logging.getLogger(__name__)
        log_level = self.__get_level(config['level'])
        log_format = config['format']
        logging.basicConfig(
            level=log_level,
            format=log_format,
            force=True
            )
        return logger

    def __get_level(self, level_name):
        try:
            if level_name == 'DEBUG':
                return logging.DEBUG
            elif level_name == 'ERROR':
                return logging.ERROR
            else:
                return logging.INFO
        except KeyError:
            return logging.INFO
    
    def get_logger(self):
        return self.logger