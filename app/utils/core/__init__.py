import os
import yaml
import logging
from typing import Any


def mkdir(path:str)-> None:
    '''
    Takes a valid path and creates directories
    recursively.
        params:
            - path : /pathto/file.js [it will create pathto folder]
    '''
    directory = os.path.dirname(path)
    try:
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            logging.info(f"Created dir [{directory}]")
    except Exception as e:
        logging.error(f"Issue occurred while creating dir [{directory}] : {e}")
        raise Exception(e)

def read_yaml(path:str)->Any:
    '''
    Loads the yaml and returns the data
        params:
            - path : path to yaml
    '''
    logging.info(f"Reading [{path}]...")
    try:
        with open(path, 'r') as f:
            file = yaml.safe_load(f)
        return file
    except Exception as e:
        logging.error(f"Issue occurred while reading [{path}] : {e}")
        raise Exception(e)