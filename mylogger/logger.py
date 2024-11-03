"""Provides a simple logger and the setup methods"""

import logging
import os

from typing import List

from .utils import check_and_create_directory
from .configuration import LoggerConfig, get_logger_config

# Init root logger (once at first import)
root_logger = logging.getLogger("")
root_logger.setLevel(logging.DEBUG)  # Set to DEBUG to see all messages

DEFAULT_LOGGER_NAME = "Unnamed Logger"


def get_default_logger(
    name: str = DEFAULT_LOGGER_NAME,
) -> logging.Logger:
    """
    Returns a logger from python's logging module with a specific configuration
    """

    logger_config = LoggerConfig()
    return get_logger_by_config(name, logger_config)


def get_logger(
    name: str = DEFAULT_LOGGER_NAME, logger_config_path: str | None = None
) -> logging.Logger:
    """
    Returns a logger from python's logging module which
    can be configured through a config file
    """

    if logger_config_path is None:
        return get_default_logger()
    else:
        logger_config = get_logger_config(logger_config_path)
        return get_logger_by_config(name, logger_config)


def get_logger_by_config(
    name: str,
    logger_config: LoggerConfig,
) -> logging.Logger:
    """
    Returns logger from logging module with a given configuration
    """

    # Create a new logger
    new_logger = logging.getLogger(name)
    handler_list: List[logging.Handler] = []

    formatter = logging.Formatter(
        fmt=logger_config.output_format, datefmt=logger_config.date_format
    )

    # create console handler and set level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logger_config.console_level)
    console_handler.setFormatter(formatter)

    handler_list.append(console_handler)

    # create file  handler and set level
    if logger_config.file_logging_enabled:

        if logger_config.file_path is None:
            raise ValueError("File path cannot be None")

        file_path = logger_config.file_path
        dir_path = os.path.dirname(file_path)

        # Create folder if it does not exist
        check_and_create_directory(dir_path)

        if logger_config.file_level is None:
            raise ValueError("File level cannot be None")

        file_handler = logging.FileHandler(file_path)
        file_handler.setLevel(logger_config.file_level)
        file_handler.setFormatter(formatter)

        handler_list.append(file_handler)

    for handler in handler_list:
        new_logger.addHandler(handler)

    return new_logger
