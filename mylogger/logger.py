"""Provides a simple logger and the setup methods"""

import logging

from typing import List

from .utils import check_and_create_directory
from .configuration import LoggerConfig

# Init root logger (once at first import)
root_logger = logging.getLogger("")
root_logger.setLevel(logging.DEBUG)  # Set to DEBUG to see all messages


def get_logger(
    name: str,
    logger_config: LoggerConfig,
):
    """
    Wrapper for logging in python to create logging according to a given configuration
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
        # Create folder if it does not exist
        check_and_create_directory(file_path)

        if logger_config.file_level is None:
            raise ValueError("File level cannot be None")

        file_handler = logging.FileHandler(file_path)
        file_handler.setLevel(logger_config.file_level)
        file_handler.setFormatter(formatter)

        handler_list.append(file_handler)

    for handler in handler_list:
        new_logger.addHandler(handler)

    return new_logger
