"""Loads configuration for setting up a logger"""

from dataclasses import dataclass
from configparser import RawConfigParser
from logging import getLevelNamesMapping

CONSOLE_DEFAULT_LEVEL = "DEBUG"
FILE_DEFAULT_LEVEL = "ERROR"

OUTPUT_FORMAT_DEFAULT = "[%(asctime)s] %(name)-15s [%(levelname)-7s]: %(message)s"
DATE_FORMAT_DEFAULT = "%Y/%m/%d %H:%M:%S"
FILE_PATH_DEFAULT = "./logs/log.txt"


@dataclass
class LoggerConfig:
    """Config class"""

    output_format: str = OUTPUT_FORMAT_DEFAULT
    date_format: str = DATE_FORMAT_DEFAULT
    console_level: int = getLevelNamesMapping()[CONSOLE_DEFAULT_LEVEL]
    file_path: str | None = FILE_PATH_DEFAULT
    file_level: int | None = getLevelNamesMapping()[FILE_DEFAULT_LEVEL]

    def __post_init__(self):

        missing_file_path = self.file_path is None or self.file_path == ""
        if missing_file_path:
            self.file_logging_enabled = False
            self.file_level = None
            self.file_path = None
        else:
            self.file_logging_enabled = True
            if self.file_level is None:
                self.file_level = getLevelNamesMapping()[FILE_DEFAULT_LEVEL]


def get_logger_config(path: None | str = None) -> LoggerConfig:
    """Loads config parameter from file or fallbacks to default values"""

    config = LoggerConfig()

    if path is not None:
        cfg_parser = RawConfigParser()
        cfg_parser.read(path)

        # section general
        output_format = cfg_parser.get(
            section="general", option="format", fallback=None
        )
        date_format = cfg_parser.get(
            section="general", option="date_format", fallback=None
        )

        # section console
        console_level_input = cfg_parser.get(
            section="console", option="level", fallback=None
        )
        if console_level_input is not None:
            console_level = getLevelNamesMapping()[console_level_input.upper()]
        else:
            console_level = None

        # section file
        file_path = cfg_parser.get(section="file", option="filepath", fallback=None)
        file_level_input = cfg_parser.get(section="file", option="level", fallback=None)
        if file_level_input is not None:
            file_level = getLevelNamesMapping()[file_level_input.upper()]
        else:
            file_level = None

        # Replace settings with values from config file
        if output_format is not None:
            config.output_format = output_format

        if date_format is not None:
            config.date_format = date_format

        if console_level is not None:
            config.console_level = console_level

        if file_level is not None:
            config.file_level = file_level

        if file_path is not None or file_path == "":
            config.file_path = file_path

    return config


if __name__ == "__main__":
    config_loaded = get_logger_config("./example_config.cfg")
    print(config_loaded)
    config_default = get_logger_config()
    print(config_default)
