"""
This module contains functions for managing logs. It initializes a sensible logger setup and provides other methods to access it.
The logger will be named app for all of the modules that log.

Functions:
    - init_logs_dir_and_file: Create the brother log directory, and return a Path object for the desired log file.
    - init_logger: Initialize a logger that outputs to standard output and to a log file in logs/ directory.
    - get_logger: Get the logger named app. Pretty simple. 
"""

from .path_utils import get_module_path, get_logs_dir, make_logs_dir
from pathlib import Path
import logging


def init_logs_dir_and_file(file: str, log_name: str = "app.log") -> Path:
    """Create the brother log directory, and return a Path object
    for the desired log file. `file` shuold be __file__."""

    # Get the path of the log directory
    logs_dir = get_logs_dir(file)
    # Create the log directory
    make_logs_dir(logs_dir)
    # Return the path of the log file
    return logs_dir / log_name


def init_logger(file: str, log_name: str = "app.log"):
    """Initialize a logger that outputs to standard output and to a log file.
    The standard output will only show messages with level ERROR or higher, and
    the log file will show all messages. The log file will be appended to if
    it already exists. `file` shuold be __file__. The logger will be named app for all of the
    modules that log.
    """

    # Init logs directory and file
    log_file = init_logs_dir_and_file(file, log_name)

    # Create the logger
    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG)

    # Create the console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)
    console_formatter_string = "%(levelname)s:%(filename)s:%(lineno)d ❌ %(message)s"
    console_handler.setFormatter(logging.Formatter(console_formatter_string))
    logger.addHandler(console_handler)

    # Create the file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(filename)-15s %(lineno)4d %(levelname)-7s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    logger.addHandler(file_handler)

    # Log an informational message
    logger.info("Logger initialized successfully!")


def get_logger() -> logging.Logger:
    """Get the logger named app."""

    return logging.getLogger("app")
