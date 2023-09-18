# myapp.py
# My standard for logging in Python.
import logging
import mylib
from pathlib import Path


def main():
    # Get the cwd of this file.
    cwd = Path(__file__).parent
    # Create a path to the log file.
    log_file = cwd / "myapp.log"
    # Configure root logger with a file handler.
    # Also, my preferred log format and level.
    # Overwrite the log file each time myapp.py is run.
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
        filemode="w",
    )
    # Optionaly add a console handler.
    # This will print to the console in addition to the log file.
    # Useful for debugging.
    log_console = False
    if log_console:
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        logging.getLogger("").addHandler(console)

    # Demonstrate logging.
    logging.info("Started myApp.")
    mylib.do_something()
    logging.info("Finished myApp.")


if __name__ == "__main__":
    main()
