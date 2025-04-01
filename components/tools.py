import yfinance as yf
import pandas as pd
import ta  

def fetch_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="3mo")
        data['SMA50'] = ta.trend.sma_indicator(data['Close'], window=50)
        data['SMA200'] = ta.trend.sma_indicator(data['Close'], window=200)
        data['RSI'] = ta.momentum.rsi(data['Close'], window=14)
        data['MACD'] = ta.trend.macd(data['Close'])
        return data
    except Exception as e:
        return f"Error fetching data: {e}"

def analyze_stock(data):
    latest = data.iloc[-1]
    decision = "Hold"

    if latest['Close'] > latest['SMA50'] and latest['RSI'] < 70:
        decision = "Buy"
    elif latest['Close'] < latest['SMA50'] and latest['RSI'] > 70:
        decision = "Sell"

    analysis = (
        f"Latest Price: ${latest['Close']:.2f}\n"
        f"50-Day SMA: ${latest['SMA50']:.2f}\n"
        f"200-Day SMA: ${latest['SMA200']:.2f}\n"
        f"RSI: {latest['RSI']:.2f}\n"
        f"MACD: {latest['MACD']:.2f}\n"
        f"Recommendation: **{decision}**"
    )

    return analysis
