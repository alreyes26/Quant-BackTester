import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

class MarketData:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def get_data(self):
        data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
        return data
    
    def get_latest_price(self):
        data = self.get_data()
        latest_price = data['Close'].iloc[-1]
        return latest_price
    def plot_data(self):
        data = self.get_data()
        plt.figure(figsize=(10, 5))
        plt.plot(data['Close'], label=f'{self.ticker} Close Price')
        plt.title(f'{self.ticker} Stock Price from {self.start_date} to {self.end_date}')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()
        
        
class MarketDataAnalyzer:
    
    def __init__(self, market_data):
        self.market_data = market_data

    def calculate_moving_average(self, window):
        data = self.market_data.get_data()
        moving_average = data['Close'].rolling(window=window).mean()
        return moving_average

    def plot_moving_average(self, window):
        data = self.market_data.get_data()
        moving_average = self.calculate_moving_average(window)
        
        plt.figure(figsize=(10, 5))
        plt.plot(data['Close'], label=f'{self.market_data.ticker} Close Price')
        plt.plot(moving_average, label=f'{window}-Day Moving Average', color='orange')
        plt.title(f'{self.market_data.ticker} Stock Price and {window}-Day Moving Average')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()
        
        
        