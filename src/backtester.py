class Backtester:
    def __init__(self, market_data, strategy):
        self.market_data = market_data
        self.strategy = strategy
        self.inital_cash = initial_cash
        
        self.cash = initial_cash
        self.shares = 0
        self.portfolio_value = initial_cash
        
    def run_backtest(self):
        data = self.market_data.get_data()
        signals = self.strategy.generate_signals()
        
        for i in range(len(data)):
            if signals[i] == 1:  # Buy signal
                self.shares += self.cash // data['Close'].iloc[i]
                self.cash -= self.shares * data['Close'].iloc[i]
            elif signals[i] == 0:  # Sell signal
                self.cash += self.shares * data['Close'].iloc[i]
                self.shares = 0
            
            self.portfolio_value = self.cash + (self.shares * data['Close'].iloc[i])
        
        return self.portfolio_value
    
    
    backtester = Backtester(market_data, strategy, 10000)
    backtester.run_backtest()