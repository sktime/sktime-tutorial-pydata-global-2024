from typing import Tuple

import pandas as pd


def load_stallion(as_period=False) -> Tuple[pd.DataFrame, pd.DataFrame]:
    data = pd.read_csv("data/stallion_data.csv")
    data["date"] = pd.to_datetime(data["date"])
    if as_period:
        data["date"] = data["date"].dt.to_period("M")
    data = data.set_index(["agency", "sku", "date"])
    y = data[["volume"]]
    X = data.drop(columns="volume")
    return X, y
