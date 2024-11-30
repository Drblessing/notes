import logging
from src.log_manager import init_logger, get_logger
from pathlib import Path
import os
import sys
import pytest


# Define a fixture for createing the log directory
@pytest.fixture()
def manage_logs_dir():
    """Create the log directory before the test, and delete it after."""

    # Get the path of the log directory
    log_dir = Path(__file__).parent / "logs"

    # Create the log directory
    log_dir.mkdir(parents=True, exist_ok=True)

    # Yield the log directory
    yield log_dir

    # Delete the log directory
    log_dir.rmdir()


def test_init_logger(manage_logs_dir):
    """Test init_logger, and a info message."""

    # Initialize the logger
    log_file = "test.log"
    init_logger(__file__, log_file)

    # Get the logger
    logger = get_logger()

    # Check that the logger has the correct level
    assert logger.level == logging.DEBUG

    # Check that the logger has two handlers
    assert len(logger.handlers) == 2

    # Check that the console handler has the correct level and formatter
    console_handler = logger.handlers[0]
    assert console_handler.level == logging.ERROR
    assert isinstance(console_handler.formatter, logging.Formatter)

    # Check that the file handler has the correct level and formatter
    file_handler = logger.handlers[1]
    assert file_handler.level == logging.DEBUG
    assert isinstance(file_handler.formatter, logging.Formatter)

    # Check that the log file exists
    log_dir = Path(__file__).parent / "logs"
    assert (log_dir / log_file).exists()

    # Log an info message
    logger.info("Running the test_log_manager.py test")

    # Verify the last line of the log file
    with open(log_dir / log_file, "r") as f:
        lines = f.readlines()
        assert lines[-1].endswith("Running the test_log_manager.py test\n")

    # Clean up the log file
    (log_dir / log_file).unlink()


def test_error_logging(manage_logs_dir, capsys):
    """Test error logging to the console."""

    # Initialize the logger
    log_file = "test.log"
    init_logger(__file__, log_file)

    # Get the logger
    logger = get_logger()
    log_dir = Path(__file__).parent / "logs"

    # Log an error message
    logger.error("This is an error message")

    # Verify the error message was logged to console
    captured = capsys.readouterr()
    assert captured.err == "ERROR:test_log_manager.py:81 ❌ This is an error message\n"

    # Verify the error message was logged to the log file
    with open(log_dir / log_file, "r") as f:
        lines = f.readlines()
        assert lines[-1].endswith("This is an error message\n")

    # Clean up the log file
    (log_dir / log_file).unlink()
