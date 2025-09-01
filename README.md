# Perpixility

Perpixility is a prototype dashboard for Indian stock market enthusiasts. It aims to provide interactive charts, technical indicators and streaming data with integration to TradingView or local brokers.

## Features

- **Market data fetcher:** Placeholder functions to fetch historical OHLCV data; you can replace them with APIs from NSE, BSE or your brokerage.
- **Technical indicators:** Basic moving average calculation as an example; extend with RSI, MACD, Bollinger Bands and more.
- **Charting hooks:** Stubs for integrating with charting libraries like Plotly, matplotlib or TradingView widgets.
- **Extensible design:** Built with data classes and modular functions for easy extension and integration with UI frameworks such as Streamlit or Dash.

## Getting Started

Clone the repository and run the sample script:

```bash
git clone https://github.com/TanveerBakshii/Perpixility.git
cd Perpixility
python app.py
```

The sample script generates mock data and computes a 5‑day moving average. In a real application, implement `fetch_market_data` to call actual market APIs.

## Project Structure

```
Perpixility/
├── app.py          # Example script demonstrating data fetch and indicator
├── README.md       # Project overview and setup instructions
```

## Contributing

Contributions are welcome! Feel free to open issues for ideas and improvements, or submit pull requests with new features. Please follow standard Python style guidelines and add docstrings to new functions.

## License

This project is licensed under the MIT License.
