import json
import urllib.request
import yfinance as yf

API_KEY = 'c590veqad3idb0atu0eg'

def getStockData(ticker):
    ticker.upper()
    api_url = f'https://finnhub.io/api/v1/quote?symbol={ticker}&token={API_KEY}'
    connection = urllib.request.urlopen(api_url)
    responseString = connection.read().decode()
    return responseString





if __name__ == '__main__':
    run = True
    while run:
        ticker = input("enter a ticker symbol or \'quit\' to quit: ")
        if ticker == "quit":
            break
        res = getStockData(ticker)
        print(res)
        ticker_data = json.loads(res)
        print(f'The current price of {ticker} is: {ticker_data["c"]}')
        print("Stock Quotes retrieved successfully!zz")