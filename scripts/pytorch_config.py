from dataclasses import dataclass
import torch
import sys
import os
import pandas as pd
from typing import List, Tuple, Union, Optional, Dict, Any, Callable, Iterable
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import torch
from torch.utils.data import Dataset, DataLoader, TensorDataset
import numpy as np


class PytorchConfig:
    def __init__(
        self,
        use_cpu=False,
        batch_size: int = 256,
        epochs: int = 100,
        data_path: str = "input",
        target: str = "num_sold",
    ):
        self.device = PytorchConfig.get_device(use_cpu)
        self.device_count = PytorchConfig.get_device_count()
        self.batch_size = batch_size
        self.epochs = epochs
        self.data_path = data_path
        self.target = target
        PytorchConfig.get_versions()

    @staticmethod
    def get_device(use_cpu=False):
        """Gets device for pytorch."""
        device = (
            "cuda"
            if torch.cuda.is_available()
            else "mps"
            if torch.backends.mps.is_available()
            else "cpu"
        )
        if use_cpu:
            device = "cpu"
        print(f"Device: {device}")
        return device

    @staticmethod
    def get_device_count():
        """Gets device count for pytorch."""
        device_count = torch.cuda.device_count()
        print(f"Device count: {device_count}")
        return device_count

    @staticmethod
    def get_versions():
        """Prints python and pytorch versions."""
        print(f"Python version: {sys.version}")
        print(f"Pytorch version: {torch.__version__}")

    @staticmethod
    def load_tabular_data(data_path):
        """Loads tabular data from csv files."""
        train_path = os.path.join(data_path, "train.csv")
        test_path = os.path.join(data_path, "test.csv")
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)
        return train_df, test_df

    @staticmethod
    def process_tabular_data(train_df, test_df, target):
        """Standard preprocessing for tabular data."""

        # Remove id column if present
        if "id" in train_df.columns:
            train_df.drop("id", axis=1, inplace=True)
        if "id" in test_df.columns:
            test_df.drop("id", axis=1, inplace=True)


class DataProcessing:
    """Holds sklearn and pytorch data processing objects."""

    def __init__(self, train_df: pd.DataFrame, test_df: pd.DataFrame, target: str):
        self.train_df = train_df
        self.test_df = test_df
        self.target = target
        self.process_data()

    def process_data(self):
        """Modifiable function to processes data for training."""
        PytorchConfig.process_tabular_data(self.train_df, self.test_df, self.target)

        # Date encoding
        self.date_encode(self.train_df, "date")
        self.date_encode(self.test_df, "date")

        # One hot encoding
        ohe_cols = ["country", "store", "product"]
        self.train_df = self.one_hot_encode(self.train_df, ohe_cols)
        self.test_df = self.one_hot_encode(self.test_df, ohe_cols)

        # Train test split
        self.train_val_split()

        # Get all cols except target
        standardize_cols = ["year", "month", "day", "dayofweek", "days_since_min_date"]

        # Standardize feature cols
        self.standardize_feature_cols(self.train_df, standardize_cols)

        # Standardize target col
        self.standardize_target_col(self.train_df, self.target)

    def date_encode(self, df: pd.DataFrame, date_col: str):
        """Encodes date columns."""

        # Turn date columns into datetime objects
        df[date_col] = pd.to_datetime(df[date_col])

        # Create year, month, day, and day of week columns
        df["year"] = df[date_col].dt.year
        df["month"] = df[date_col].dt.month
        df["day"] = df[date_col].dt.day
        df["dayofweek"] = df[date_col].dt.dayofweek

        # Create days since min date column
        min_date = df[date_col].min()
        df["days_since_min_date"] = (df[date_col] - min_date).dt.days

        # Drop original date column
        df.drop(date_col, axis=1, inplace=True)

    def one_hot_encode(self, df: pd.DataFrame, cols: List[str]):
        """One hot encode cols."""
        df = pd.get_dummies(df, columns=cols, dtype=np.float32)
        return df

    def train_val_split(self, val_size: float = 0.2):
        """Splits data into train and validation sets."""
        self.train_df, self.val_df = train_test_split(
            self.train_df, test_size=val_size, random_state=42
        )

        # Reset index
        self.train_df.reset_index(drop=True, inplace=True)
        self.val_df.reset_index(drop=True, inplace=True)

    def standardize_feature_cols(self, df: pd.DataFrame, feature_cols: List[str]):
        """Standardizes feature cols and saves scaler. Input shoudl be train df."""

        # Init scaler
        self.feature_scaler = StandardScaler()

        # Train scaler
        self.feature_scaler.fit(df[feature_cols])

        # Standardize feature cols
        df[feature_cols] = self.feature_scaler.transform(df[feature_cols])

        # Standardize val and test df
        self.val_df[feature_cols] = self.feature_scaler.transform(
            self.val_df[feature_cols]
        )

        self.test_df[feature_cols] = self.feature_scaler.transform(
            self.test_df[feature_cols]
        )

    def standardize_target_col(self, df: pd.DataFrame, target_col: str):
        """Standardizes target col for large target and saves scaler. Need to
        inverse predictions after training. Input should be train df."""

        # Init scaler
        self.target_scaler = StandardScaler()

        # Train scaler
        self.target_scaler.fit(df[[target_col]])

        # Standardize target col
        df[[target_col]] = self.target_scaler.transform(df[[target_col]])

        # Standardize val df
        self.val_df[[target_col]] = self.target_scaler.transform(
            self.val_df[[target_col]]
        )

        # Save inverse scaler
        self.inverse_target_scaler = self.target_scaler.inverse_transform

    def to_pytorch_dataset(self):
        """Turns data into pytorch dataset using TensorDataset."""

        # Trun train,val and test df into float32
        self.train_df = self.train_df.astype(np.float32)
        self.val_df = self.val_df.astype(np.float32)
        self.test_df = self.test_df.astype(np.float32)

        # Unsqueezes target col
        target_train = torch.tensor(self.train_df[self.target].values).unsqueeze(1)
        target_val = torch.tensor(self.val_df[self.target].values).unsqueeze(1)

        train_ds = TensorDataset(
            torch.tensor(self.train_df.drop(self.target, axis=1).values),
            target_train,
        )

        val_ds = TensorDataset(
            torch.tensor(self.val_df.drop(self.target, axis=1).values),
            target_val,
        )

        test_ds = TensorDataset(
            torch.tensor(self.test_df.values), torch.zeros(self.test_df.shape[0])
        )

        return train_ds, val_ds, test_ds


# Constants
DATA_PATH = "input"
TARGET = "num_sold"
BATCH_SIZE = 1000
EPOCHS = 100
pytorch_config = PytorchConfig(
    use_cpu=False,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
    data_path=DATA_PATH,
    target=TARGET,
)


train_df, test_df = pytorch_config.load_tabular_data(DATA_PATH)
dp = DataProcessing(train_df, test_df, TARGET)
train_ds, val_ds, test_ds = dp.to_pytorch_dataset()


# Create a PyTorch data loader
train_loader = DataLoader(
    dataset=train_ds, batch_size=pytorch_config.batch_size, shuffle=True
)
val_loader = DataLoader(dataset=val_ds, batch_size=pytorch_config.batch_size)
test_loader = DataLoader(test_ds, batch_size=len(test_ds))
