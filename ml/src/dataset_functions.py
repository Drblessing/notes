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
    current_dir = Path.cwd()

    # Data directory
    data_dir = current_dir.parent / "data"

    # Create the data directory if it doesn't exist
    data_dir.mkdir(parents=True, exist_ok=True)

    # Full path to the .csv file
    file_path = data_dir / filename

    # Save the DataFrame as a .csv file
    df.to_csv(file_path)

    print(f"DataFrame saved as {file_path}")


# Load a .csv file into a DataFrame
def load_csv(filename: str) -> pd.DataFrame:
    """
    Load a .csv file into a DataFrame. The .csv file should be in the 'data' directory.

    Args:
        filename (str): The name of the .csv file to load.
    Returns:
        pd.DataFrame: The loaded DataFrame.
    """

    # Current directory
    current_dir = Path.cwd()

    # Data directory
    data_dir = current_dir.parent / "data"

    # Full path to the .csv file
    file_path = data_dir / filename

    # Load the .csv file into a DataFrame
    df = pd.read_csv(file_path)

    print(f"DataFrame loaded from {file_path}")
    print(df.head())

    return df
