import unittest

import io
import sys
import re

from mylogger.logger import get_logger
from mylogger.configuration import LoggerConfig


class TestGetLoggerFunction(unittest.TestCase):

    def test_default_logger(self):
        logger = get_logger()
        self.assertIsNotNone(logger)

    def test_named_logger(self):
        logger = get_logger("test_logger")
        self.assertIsNotNone(logger)

    def test_logger_configuration_with_custom_file_path(self):
        logger_config = LoggerConfig(file_path="./logs/mylogfile.log")
        logger = get_logger(logger_config)
        self.assertIsNotNone(logger)

    def test_logger_configuration_with_custom_console_level(self):
        logger_config = LoggerConfig(console_level=20)  # INFO level
        logger = get_logger(logger_config)
        self.assertIsNotNone(logger)

    def test_logger_configuration_with_custom_file_level(self):
        logger_config = LoggerConfig(file_level=30)  # WARNING level
        logger = get_logger(logger_config)
        self.assertIsNotNone(logger)

    def test_logger_configuration_with_invalid_console_level(self):
        logger_config = LoggerConfig(console_level="INVALID_LEVEL")
        with self.assertRaises(ValueError):
            get_logger("test_logger", logger_config)

    def test_logger_configuration_with_invalid_file_level(self):
        logger_config = LoggerConfig(file_level="INVALID_LEVEL")
        with self.assertRaises(ValueError):
            get_logger("test_logger", logger_config)

    # def test_logger_info_output(self):

    #     # Capture the output
    #     captured_output = io.StringIO()
    #     sys.stdout = captured_output

    #     logger = get_logger()
    #     logger.info("Info message")
    #     captured_string = captured_output.getvalue()

    #     # Reset stdout
    #     sys.stdout = sys.__stdout__
    #     print(f"captured_string: {captured_string}")

    #     pattern = r"\[\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}\] UnnamedLogger\s+  \[INFO\s+\]: Test"

    #     assert re.match(pattern, captured_string), (
    #         'The log message format is incorrect: "'
    #         + captured_string
    #         + '" does not match '
    #         + pattern
    #     )


if __name__ == "__main__":
    unittest.main()
