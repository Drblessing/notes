# Load diabetes dataset
import sklearn.datasets as datasets
from pathlib import Path
import pandas as pd
import numpy as np


def load_diabetes_dataset(input_path: Path = Path("data/diabetes.csv")) -> pd.DataFrame:
    """Load the diabetes dataset from a CSV file into a pandas DataFrame."""

    # Current file path
    cur_file = Path(__file__)
    cwd = cur_file.parent
    input_path = cwd.parent / input_path
    if not input_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {input_path}. Please create it first."
        )
    df = pd.read_csv(input_path, index_col="patient_id")
    return df


if __name__ == "__main__":
    df = load_diabetes_dataset()
    print(df.head())
