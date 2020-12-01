# cryptodata
Data wrapper for cryptocurrencies data.

## Content

- All Binance available symbols 
- Binance historical klines (OHLCV data) using a list of symbols

## Installation
To install this package run:
`git clone https://github.com/bonetou/cryptodata`

After that you need to install the requirements using:
`python -m pip install -r requirements.txt`

## Usage

### Configuration
- Insert your API KEY and SECRET KEY in the **secrets.py** file.

You can edit the **main.py** file to specify:

- Which symbols you want
- The period of time ('1 Jan, 2019', '2 Jan, 2019')
- Data interval ('1m', '5m', '1h') as specified in https://python-binance.readthedocs.io/en/latest/constants.html#