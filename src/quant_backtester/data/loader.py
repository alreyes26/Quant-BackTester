import pandas as pd
import yfinance as yf


def load_price_data(ticker, start_date, end_date):

yf.download(

    ticker, start=start_date, end=end_date
    return data

)


