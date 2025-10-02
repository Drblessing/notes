# Generic dataset functions
from pathlib import Path
import pandas as pd


# Create a .csv file from a DataFrame
def create_csv(df: pd.DataFrame, filename: str) -> None:
    """
    Create a .csv file from a DataFrame. Save it in the 'data' directory.

    Args:
        df (pd.DataFrame): The DataFrame to save as a .csv file.
        filename (str): The name of the .csv file.
    """

    # Current directory
    current_dir = Path(__file__).parent

    # Data directory
    data_dir = current_dir.parent / "data"

    # Create the data directory if it doesn't exist
    data_dir.mkdir(parents=True, exist_ok=True)

    # Full path to the .csv file
    file_path = data_dir / filename
