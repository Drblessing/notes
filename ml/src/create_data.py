# Generic data creation functions
import sklearn.datasets as datasets
from pathlib import Path
import pandas as pd
import numpy as np

# Create dataset type



# Create a .csv file from an array or DataFrame
def create_dataset(data : pd.DataFrame | np.ndarray, 
                   output_path: Path) -> None:
    """Create and save a dataset to a CSV file."""
    
    # Current file path
    cur_file = Path(__file__)
    cwd = cur_file.parent
    output_path = cwd.parent / output_path

    # Check if the dataset already exists
    if output_path.exists():
        print(f"Dataset already exists at {output_path}. Skipping creation.")
        return

    # Convert numpy array to DataFrame if necessary
    if isinstance(data, np.ndarray):
        data = pd.DataFrame(data)

    # Save the dataset to a CSV file
    DATA_ROOT = cur_file.parent.parent / "data"
    DATA_ROOT.mkdir(parents=True, exist_ok=True)
    data.to_csv(output_path, index=False)
    print(f"Dataset saved to {output_path}")


if __name__ == "__main__":
