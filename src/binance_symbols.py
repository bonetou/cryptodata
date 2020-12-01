from binance.client import Client

class BinanceSymbols:

    def __init__(self, API_KEY, SECRET_KEY):
        self.client = Client(API_KEY, SECRET_KEY)

    def get_all_symbols(self):
        symbols = []
        tickers = self.client.get_all_tickers()
        for ticker in tickers:
            symbols.append(ticker['symbol'])
        return symbols
