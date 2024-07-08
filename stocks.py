import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    return data['Time Series (Daily)']

def preprocess_data(data):
    df = pd.DataFrame(data).T
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)
    return df

def analyze_data(df):
    df['Daily Returns'] = df['4. close'].pct_change()
    df['50-Day Moving Average'] = df['4. close'].rolling(window=50).mean()
    df['200-Day Moving Average'] = df['4. close'].rolling(window=200).mean()
    return df

def visualize_data(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['4. close'], label='Close Price')
    plt.plot(df.index, df['50-Day Moving Average'], label='50-Day Moving Average')
    plt.plot(df.index, df['200-Day Moving Average'], label='200-Day Moving Average')
    plt.title('Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def main():
    api_key = "Your_API_KEY"
    symbol = input("Enter the stock symbol: ")
    stock_data = fetch_stock_data(symbol, api_key)
    df = preprocess_data(stock_data)
    df = analyze_data(df)
    visualize_data(df)

if __name__ == "__main__":
    main()
