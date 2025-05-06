import ssl

# Create an unverified context
ssl._create_default_https_context = ssl._create_unverified_context

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split


def download_MNIST(save_dir):
    x, y = fetch_openml("mnist_784", version=1, data_home="data_cache", return_X_y=True)

    x /= 255.0
    x -= x.mean()
    y = pd.get_dummies(y)

    x_train, x_val, y_train, y_val = train_test_split(
        x, y, test_size=0.15, random_state=42
    )
    save_dir.mkdir(exist_ok=True)
    x_train.to_parquet(save_dir / "x_train.parquet")
    x_val.to_parquet(save_dir / "x_val.parquet")
    np.save(save_dir / "y_train.npy", y_train)
    np.save(save_dir / "y_val.npy", y_val)


if __name__ == "__main__":
    print("Starting")
    save_dir = Path("../data/mnist_784/")
    print(f"Downloading MNIST dataset at {save_dir.resolve()}")
    download_MNIST(save_dir)
