# pylint: disable=missing-docstring
import unittest

# import io
# import sys
# import re

from mylogger.logger import get_default_logger, get_logger, get_logger_by_config
from mylogger.configuration import get_logger_config, LoggerConfig


class TestGetLoggerFunction(unittest.TestCase):

    def test_default_logger(self):
        logger = get_default_logger()
        self.assertIsNotNone(logger)

    def test_named_logger(self):
        logger = get_default_logger("test_logger")
        self.assertIsNotNone(logger)


class TestGetDefaultLoggerFunction(unittest.TestCase):

    def test_defatul_logger(self):
        logger = get_logger()
        self.assertIsNotNone(logger)

    def test_named_logger(self):
        logger = get_logger("Test logger")
        self.assertIsNotNone(logger)

    def test_logger_with_config(self):
        logger = get_logger(logger_config_path="./tests/test_config.cfg")
        self.assertIsNotNone(logger)

    def test_named_logger_with_config(self):
        logger = get_logger(
            name="Test logger", logger_config_path="./tests/test_config.cfg"
        )
        self.assertIsNotNone(logger)


class TestGetLoggerWithConfig(unittest.TestCase):

    def test_logger_configuration_with_custom_file_path(self):
        logger_config = get_logger_config(path="./tests/test_config.cfg")
        logger = get_logger_by_config("Test logger", logger_config)
        self.assertIsNotNone(logger)

    def test_logger_configuration_with_custom_console_level(self):
        logger_config = LoggerConfig(console_level=20)  # INFO level
        logger = get_logger_by_config("Test logger", logger_config)
        self.assertIsNotNone(logger)

    def test_logger_configuration_with_custom_file_level(self):
        logger_config = LoggerConfig(file_level=30)  # WARNING level
        logger = get_logger_by_config("Test logger", logger_config)
        self.assertIsNotNone(logger)

    def test_logger_configuration_with_invalid_console_level(self):
        logger_config = LoggerConfig(console_level="INVALID_LEVEL")
        with self.assertRaises(ValueError):
            get_logger_by_config("Test logger", logger_config)

    def test_logger_configuration_with_invalid_file_level(self):
        logger_config = LoggerConfig(file_level="INVALID_LEVEL")
        with self.assertRaises(ValueError):
            get_logger_by_config("test_logger", logger_config)


# class TestLogger(unittest.TestCase):

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
