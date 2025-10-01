# Load diabetes dataset
import sklearn.datasets as datasets
from pathlib import Path
import pandas as pd
import numpy as np

def load_diabetes_dataset(input_path: Path = Path("data/diabetes.csv")) -> pd.DataFrame: