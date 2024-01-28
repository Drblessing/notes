"""This module contains functions to handle paths. 

Functions: 
    get_module_path: Get the path of the current module.
    get_log_dir: Gets the path of a "logs" directory in the same
        directory as the current module, i.e. as a brother directory.
    make_log_dir: Create the brother log directory if it doesn't exist.
"""

from pathlib import Path


def get_module_path(file: str) -> Path:
    """Get the path of the current module.
    Pass __file__ as argument."""

    return Path(file)


def get_logs_dir(file: str) -> Path:
    """Gets the path of a "logs" directory in the same
    directory as the current module, i.e. as a brother directory.
    """

    return get_module_path(file).parent / "logs"


def make_logs_dir(log_dir: Path):
    """Create the brother log directory if it doesn't exist."""

    log_dir.mkdir(parents=True, exist_ok=True)


# Example
if __name__ == "__main__":
    # Create the log directory here
    logs_dir = get_logs_dir(__file__)
    # Check that the directory exists
    make_logs_dir(logs_dir)
    assert logs_dir.exists()
    # Delete the log directory
    logs_dir.rmdir()
    # Check that the directory doesn't exist
    assert not logs_dir.exists()
