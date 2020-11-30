import pandas as pd
from binance.client import Client
from secrets import API_KEY, SECRET_KEY

from pandas.core.frame import DataFrame

class BinanceHistoricalKlines:

    def __init__(self, API_KEY, SECRET_KEY):
        self.API_KEY = API_KEY
        self.API_SECRET = SECRET_KEY
        self.client = Client(api_key=self.API_KEY, api_secret=self.API_SECRET)
        self.saving_default_dir = 'data/'

    def get_historical_klines_multiple_symbols(self, symbols: str, start_time: str, final_time=None, kline_interval='1d'):
        if final_time is None:
            for symbol in symbols:
                filename = f'{self.saving_default_dir}{symbol}_{start_time}_{kline_interval}.csv'.replace(' ', '').replace(',','')
                self.data = self.client.get_historical_klines(symbol, kline_interval, start_time)
                self.data_configured = self.config_data(self.data)
                self.save_data(self.data_configured, filename)
        else:
            for symbol in symbols:
                filename = f'{self.saving_default_dir}{symbol}_{start_time}_{final_time}{kline_interval}.csv'.replace(' ', '').replace(',','')
                self.data = self.client.get_historical_klines(symbol, kline_interval, start_time, final_time)
                self.save_data(self.data, filename)

    def config_data(self, data):
        column_names = [\
            'open_time',
            'open',
            'high',
            'low',
            'close',
            'volume',
            'close_time',
            'quote_asset_volume',
            'number_of_trades',
            'taker_buy_base_asset_volume',
            'taker_buy_quote_asset_volume',
            'ignore'
            ]

        df = pd.DataFrame(data=data, columns=column_names)
        df['date_open_time'] = pd.to_datetime(df['open_time'], unit='ms')
        df['date_close_time'] = pd.to_datetime(df['close_time'], unit='ms')

        return df

    def save_data(self, data: DataFrame, filename: str):
        data.to_csv(filename, index=False)


