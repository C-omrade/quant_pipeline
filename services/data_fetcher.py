import os
import pandas as pd
from datetime import datetime

from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame

from core.config import ALPACA_API_KEY, ALPACA_SECRET_KEY


data_client = StockHistoricalDataClient(
    ALPACA_API_KEY, ALPACA_SECRET_KEY
)

def fetch_historical_data(symbol: str, start_date: datetime, end_date: datetime) -> pd.DataFrame:
    request_params = StockBarsRequest(
        symbol_or_symbols=symbol,
        timeframe=TimeFrame.Day,
        start=start_date,
        end=end_date
    )

    bars = data_client.get_stock_bars(request_params)

    df = bars.df
    df.reset_index(inplace=True)
    df = df[['symbol', 'timestamp', 'open', 'high', 'low', 'close', 'volume']]
    return df