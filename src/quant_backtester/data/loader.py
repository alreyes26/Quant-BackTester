import pandas as pd


def load_csv(file_path: str, date_column: str, price_column: str) -> pd.Series:

    data = pd.read_csv(file_path)
    data = data[[date_column, price_column]]
    data[date_column] = pd.to_datetime(data[date_column])

    prices = data.set_index(date_column)[price_column]

    return prices