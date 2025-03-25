import pytest
from src.path_utils import get_module_path, get_logs_dir, make_logs_dir
from pathlib import Path


def test_get_module_path():
    """Test get_module_path."""

    # Get the path of this test module
    module_path = get_module_path(__file__)

    # Check that the past is correct up to Github repo name
    correct_module_path = Path("notes", "snippets", "tests", "test_path_utils.py")
    assert str(module_path).endswith(str(correct_module_path))


def test_get_logs_dir():
    """Test get_log_dir."""

    # Get the path of the log directory
    log_dir = get_logs_dir(__file__)

    # Check that the past is correct up to Github repo name
    correct_log_dir = Path("notes", "snippets", "tests", "logs")
    assert str(log_dir).endswith(str(correct_log_dir))


def test_make_logs_dir():
    """Test make_log_dir."""

    # Get the path of the log directory
    log_dir = get_logs_dir(__file__)

    # Create the log directory
    make_logs_dir(log_dir)

    # Check that the directory exists
    assert log_dir.exists()

    # Delete the log directory
    log_dir.rmdir()
