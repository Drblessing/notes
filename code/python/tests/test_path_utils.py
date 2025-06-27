import pytest
from src.path_utils import get_module_path, get_logs_dir, make_logs_dir
from pathlib import Path


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
