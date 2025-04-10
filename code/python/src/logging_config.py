import logging
import logging.config
from pathlib import Path

def setup_logging(log_folder_path: Path):
    """
    Set up logging with logs stores in logs/app.log at log_folder_path

    Args:
        log_folder_path (Path): Path to the folder where logs will be stored
    """
    logs_dir = log_folder_path / 'logs'
    logs_dir.mkdir(parents=True, exist_ok=True)

    config = {
        'version': 1,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'standard',
            },
            'file': {
                'class': 'logging.FileHandler',
                'level': 'DEBUG',
                'formatter': 'standard',
                'filename': logs_dir / 'app.log',
            }
        },
        'loggers': {
            '': {  # Root logger
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': True
            }
        }
    }
    logging.config.dictConfig(config)