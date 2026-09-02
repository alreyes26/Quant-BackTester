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
        
        
class MovingAverageStrategy:
    
    def __init__(self, market_data_analyzer, short_window, long_window):
        self.market_data_analyzer = market_data_analyzer
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self):
        data = self.market_data_analyzer.market_data.get_data()
        short_ma = self.market_data_analyzer.calculate_moving_average(self.short_window)
        long_ma = self.market_data_analyzer.calculate_moving_average(self.long_window)

        singals = [0]
        
        for spot in range[1, len(short_ma)]:
            if short_ma[spot] > long_ma[spot] and short_ma[spot - 1] <= long_ma[spot - 1]:
                singals.append(1)  # Buy signal
            elif short_ma[spot] < long_ma[spot] and short_ma[spot - 1] >= long_ma[spot - 1]:
                singals.append(0)  # Sell signal
            else:
                singals.append(singals[-1])  # Hold signal
        return np.array(singals)

    def plot_signals(self):
        data = self.market_data_analyzer.market_data.get_data()
        signals = self.generate_signals()
        
        plt.figure(figsize=(10, 5))
        plt.plot(data['Close'], label=f'{self.market_data_analyzer.market_data.ticker} Close Price')
        plt.plot(self.market_data_analyzer.calculate_moving_average(self.short_window), label=f'{self.short_window}-Day Moving Average', color='orange')
        plt.plot(self.market_data_analyzer.calculate_moving_average(self.long_window), label=f'{self.long_window}-Day Moving Average', color='green')
        
        buy_signals = np.where(signals == 1)[0]
        sell_signals = np.where(signals == 0)[0]
        
        plt.scatter(data.index[buy_signals], data['Close'].iloc[buy_signals], marker='^', color='g', label='Buy Signal', alpha=1)
        plt.scatter(data.index[sell_signals], data['Close'].iloc[sell_signals], marker='v', color='r', label='Sell Signal', alpha=1)
        
        plt.title(f'{self.market_data_analyzer.market_data.ticker} Trading Signals')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid()
        plt.show()
        
        

        
        
        