import numpy as np
import pandas as pd
from datetime import datetime
import yfinance as yf

def get_yahoofinancef_ohlc(ticker_: str, start_: str, end_: str, interval_: str) -> pd.DataFrame:
    """
    Parameters
    ----------
    ticker_ : str
        example: "BTC-USD"
    start_ : str
        example: "2023-01-01"
    end_ : str
        example: "2023-06-25"
    interval_ : str
        example: "1h"

    Returns
    -------
    data: pd.DataFrame
        dataframe containing OHLC of the symbol/ticker from start_ date to end_ date with interval interval_
    """
    
    return yf.download(ticker_, 
                       start = start_,
                       end = end_, 
                       interval = interval_)[['Open', 'High', 'Low', 'Close']].reset_index()
