"""
Perpixility - Indian Markets Dashboard

This module provides a simple skeleton for a market dashboard application. It
includes functions to fetch mock market data, compute basic technical
indicators like moving averages, and placeholder functions to generate charts.

In a complete application, you would replace the mock data with real API calls
(e.g., to NSE/BSE or brokerage data), and implement interactive dashboards
using frameworks such as Plotly Dash or Streamlit.
"""

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Tuple
import random

@dataclass
class MarketData:
    """Container for market price data."""
    date: datetime
    open: float
    high: float
    low: float
    close: float
    volume: int

def fetch_market_data(symbol: str, days: int = 30) -> List[MarketData]:
    """Generate mock OHLCV data for the past `days` trading days.

    Args:
        symbol: The ticker symbol to fetch data for.
        days: Number of days of data to generate.

    Returns:
        A list of MarketData objects containing synthetic price and volume data.
    """
    data: List[MarketData] = []
    price = 100.0  # starting price for mock data
    for i in range(days):
        date = datetime.now() - timedelta(days=days - i)
        # Simulate random price movements
        open_price = price + random.uniform(-1, 1)
        high_price = open_price + random.uniform(0, 2)
        low_price = open_price - random.uniform(0, 2)
        close_price = low_price + (high_price - low_price) * random.random()
        volume = random.randint(1000, 10000)
        data.append(MarketData(date=date, open=open_price, high=high_price, low=low_price, close=close_price, volume=volume))
        price = close_price  # update price for next day
    print(f"Fetched {len(data)} days of mock data for {symbol}")
    return data

def calculate_moving_average(values: List[float], window: int) -> List[float]:
    """Compute a simple moving average for a series of values.

    Args:
        values: Sequence of numeric values (e.g., closing prices).
        window: The lookback period for the moving average.

    Returns:
        A list of moving average values. The first (window - 1) values will be None.
    """
    if window <= 0:
        raise ValueError("Window size must be positive")
    ma: List[float] = []
    for i in range(len(values)):
        if i + 1 < window:
            ma.append(float('nan'))
        else:
            window_values = values[i + 1 - window : i + 1]
            ma.append(sum(window_values) / window)
    print(f"Calculated {window}-day moving average for {len(values)} data points")
    return ma

def plot_price_and_ma(data: List[MarketData], moving_avg: List[float]) -> None:
    """Placeholder function to plot price and moving average.

    In a full application, you might use matplotlib or Plotly to create
    interactive charts. This function currently just prints a summary.

    Args:
        data: List of MarketData objects.
        moving_avg: Corresponding moving average values.
    """
    print("Price and Moving Average plot would be generated here.")
    # Example: use matplotlib to plot candlesticks and moving average
    # import matplotlib.pyplot as plt
    # ...

def main() -> None:
    """Demonstrate fetching data and computing a moving average."""
    symbol = "NIFTY50"
    data = fetch_market_data(symbol, days=30)
    closing_prices = [d.close for d in data]
    ma = calculate_moving_average(closing_prices, window=5)
    plot_price_and_ma(data, ma)

if __name__ == "__main__":
    main()
