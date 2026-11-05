import pandas as pd
import yfinance as yf


def load_price_data(ticker, start_date, end_date):
    data = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        auto_adjust=True
    )

    if data.isna().any().any():
        raise ValueError(f"No market data found for {ticker}.")

    data.columns = data.columns.get_level_values(0)

    return data



if __name__ == "__main__":
    data = load_price_data("SPY", "2020-01-01", "2020-12-31")
    print(data)