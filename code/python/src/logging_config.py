import logging
import logging.config
from pathlib import Path


def setup_logging(log_folder_path: Path):
    """
    Set up logging with logs stores in logs/app.log at log_folder_path

    Args:
        log_folder_path (Path): Path to the folder where logs will be stored
    """
    logs_dir = log_folder_path / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    config = {
        "version": 1,
        "formatters": {
            "standard": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "standard",
            },
            "file": {
                "class": "logging.FileHandler",
                "level": "DEBUG",
                "formatter": "standard",
                "filename": logs_dir / "app.log",
            },
        },
        "loggers": {
            "": {  # Root logger
                "handlers": ["console", "file"],
                "level": "DEBUG",
                "propagate": True,
            }
        },
    }
    logging.config.dictConfig(config)


# ----- Usage Examples -----

# Example 1: Using in the main application entry point (e.g., main.py)
"""
from pathlib import Path
from my_package.logging_utils import setup_logging

def main():
    # Set up logging at the application root directory
    app_dir = Path(__file__).parent
    setup_logging(app_dir)
    
    # Get a logger for this module
    logger = logging.getLogger(__name__)
    
    # Log messages at different levels
    logger.debug("Debug message - will go to file only")
    logger.info("Info message - will go to both console and file")
    logger.warning("Warning message")
    logger.error("Error message")
    
    # Rest of the application code...

if __name__ == "__main__":
    main()
"""

# Example 2: Using in a package with multiple modules
"""
# In your package's __init__.py
from pathlib import Path
from .logging_utils import setup_logging

# Initialize logging when the package is imported
app_dir = Path(__file__).parent.parent  # Go up one level from the package directory
setup_logging(app_dir)

# In other modules of your package:
import logging

# Each module gets its own logger with the module name
logger = logging.getLogger(__name__)

def some_function():
    logger.debug("Starting some_function")
    # Function code...
    logger.info("some_function completed successfully")
"""

# Example 3: Customizing logger for specific modules
"""
# After setting up the root logger with setup_logging
import logging

# Get a logger for a specific component
component_logger = logging.getLogger('my_package.component')

# You can set different log levels for specific loggers
component_logger.setLevel(logging.WARNING)  # This component will only log warnings and above

def component_function():
    # These won't be logged because they're below WARNING level
    component_logger.debug("Debug message from component")
    component_logger.info("Info message from component")
    
    # These will be logged
    component_logger.warning("Warning message from component")
    component_logger.error("Error message from component")
"""
