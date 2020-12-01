from src.config.secrets import API_KEY, SECRET_KEY
from src.binance_symbols import BinanceSymbols
from src.binance_historical_klines import BinanceHistoricalKlines

if __name__=="__main__":
    symbols = BinanceSymbols(API_KEY, SECRET_KEY).get_all_symbols()
    KlinesWrapper = BinanceHistoricalKlines(API_KEY, SECRET_KEY)
    KlinesWrapper.get_historical_klines_multiple_symbols(symbols=symbols, start_time='1 Jan, 2016', kline_interval='1d')
