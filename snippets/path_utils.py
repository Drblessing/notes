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


def get_log_dir(file: str) -> Path:
    """Gets the path of a "logs" directory in the same
    directory as the current module, i.e. as a brother directory.
    """

    return get_module_path(file).parent / "logs"


def make_log_dir(log_dir: Path) -> None:
    """Create the brother log directory if it doesn't exist."""

    log_dir.mkdir(parents=True, exist_ok=True)


# Example
if __name__ == "__main__":
    # Create the log directory here
    log_dir = get_log_dir(__file__)
    # Check that the directory exists
    make_log_dir(log_dir)
    assert log_dir.exists()
    # Delete the log directory
    log_dir.rmdir()
    # Check that the directory doesn't exist
    assert not log_dir.exists()
