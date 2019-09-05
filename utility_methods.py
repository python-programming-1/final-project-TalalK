import configparser
import functools
import logging
import time


def init_config(config_file_path):
    path = config_file_path.split('.')
    assert(path[len(path)-1] == 'ini')

    config = configparser.ConfigParser()
    config.read(config_file_path)
    return config
 
