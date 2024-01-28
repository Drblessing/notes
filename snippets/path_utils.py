"""This module contains functions to handle paths.

Functions: 
    get_module_path: Get the path of the current module.
    get_log_dir: Gets the path of a "logs" directory in the same
        directory as the current module, i.e. as a brother directory.
    make_log_dir: Create the brother log directory if it doesn't exist.
"""

from pathlib import Path


def get_module_path() -> Path:
    """Get the path of the current module."""

    return Path(__file__)


def get_log_dir() -> Path:
    """Gets the path of a "logs" directory in the same
    directory as the current module, i.e. as a brother directory.
    """

    return get_module_path().parent / "logs"


def make_log_dir(log_dir: Path) -> None:
    """Create the brother log directory if it doesn't exist."""

    log_dir.mkdir(parents=True, exist_ok=True)
