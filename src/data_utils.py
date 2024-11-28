import pandas as pd
from pandas_datareader import data as pdr
from datetime import datetime

def fetch_cpi_data(start_date="2015-01-01"):
    """
    Fetches the US CPI data from the Federal Reserve Economic Data (FRED).
    
    Parameters:
        start_date (str): The start date for fetching data (YYYY-MM-DD).
        
    Returns:
        pd.DataFrame: A DataFrame with US CPI data.
    """
    try:
        cpi_data = pdr.DataReader("CPIAUCSL", "fred", start=start_date)
        return cpi_data
    except Exception as e:
        raise RuntimeError(f"Error fetching CPI data: {e}")