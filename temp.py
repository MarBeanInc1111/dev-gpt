import yfinance as yf
import pandas as pd
import numpy as np

# Install necessary dependencies
# pip install yfinance pandas numpy

def fetch_stock_data(ticker, period="1mo", interval="1d"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    return hist

def calculate_technical_indicators(data):
    # SMA, EMA, RSI, and MACD as before
    calculate_sma_ema_rsi_macd(data)
    # Bollinger Bands
    data['Middle Band'] = data['Close'].rolling(window=20).mean()
    data['Upper Band'] = data['Middle Band'] + 1.96 * data['Close'].rolling(window=20).std()
    data['Lower Band'] = data['Middle Band'] - 1.96 * data['Close'].rolling(window=20).std()
    # Volume (Normalized)
    data['Volume_norm'] = data['Volume'] / data['Volume'].max()

def calculate_sma_ema_rsi_macd(data):
    data['SMA'] = data['Close'].rolling(window=20).mean()
    data['EMA'] = data['Close'].ewm(span=20, adjust=False).mean()
    delta = data['Close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    exp1 = data['Close'].ewm(span=12, adjust=False).mean()
    exp2 = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = exp1 - exp2
    data['Signal_Line'] = data['MACD'].ewm(span=9, adjust=False).mean()

def alert_buy_sell(data):
    # Enhanced strategy considering Bollinger Bands and Volume
    if (data['MACD'].iloc[-1] > data['Signal_Line'].iloc[-1] and
        data['RSI'].iloc[-1] < 70 and
        data['Close'].iloc[-1] > data['Upper Band'].iloc[-1] and
        data['Volume_norm'].iloc[-1] > 0.8):  # High volume
        print("Strong Buy Signal: Breakout with high volume.")
    elif (data['MACD'].iloc[-1] < data['Signal_Line'].iloc[-1] and
          data['RSI'].iloc[-1] > 30 and
          data['Close'].iloc[-1] < data['Lower Band'].iloc[-1]):
        print("Strong Sell Signal: Breakdown.")
    else:
        print("Hold: No clear buy/sell signal.")

def main():
    ticker = "BTC-USD"  # Focusing on crypto
    period = "3mo"  # Increased period for more data
    interval = "1d"
    
    stock_data = fetch_stock_data(ticker, period, interval)
    calculate_technical_indicators(stock_data)
    alert_buy_sell(stock_data)
    
    print(stock_data.tail())

if __name__ == "__main__":
    main()
