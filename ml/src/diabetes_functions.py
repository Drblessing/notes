# Create diabetes dataset
import sklearn.datasets as datasets
from pathlib import Path
import pandas as pd
import numpy as np


def create_diabetes_dataset(output_path: Path = Path("data/diabetes.csv")):
    """Create and save the diabetes dataset from sklearn to a CSV file."""

    # Current file directory
    cwd = Path.cwd()
    output_path = cwd.parent / output_path

    # Check if the dataset already exists
    if output_path.exists():
        print(f"Dataset already exists at {output_path}. Skipping creation.")
        return

    # Load the diabetes dataset from sklearn
    diabetes = datasets.load_diabetes(as_frame=True)
    df = diabetes["frame"]
    df["patient_id"] = np.arange(1, len(df) + 1, dtype=int)
    df.set_index("patient_id", inplace=True, verify_integrity=True)

    # Save the dataset to a CSV file
    cur_file = Path(__file__)
    DATA_ROOT = cur_file.parent.parent / "data"
    DATA_ROOT.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path)
    print(f"Diabetes dataset saved to {output_path}")


def load_diabetes_dataset(input_path: Path = Path("data/diabetes.csv")) -> pd.DataFrame:
    """Load the diabetes dataset from a CSV file into a pandas DataFrame."""

    # Current file directory
    cwd = Path.cwd()
    output_path = cwd.parent / output_path
    input_path = cwd.parent / input_path
    if not input_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {input_path}. Please create it first."
        )
    df = pd.read_csv(input_path, index_col="patient_id")
    return df


if __name__ == "__main__":
    create_diabetes_dataset()
    df = load_diabetes_dataset()
    print(df.head())
