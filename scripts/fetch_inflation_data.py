import os
import sys
import pandas as pd

# Add src to the Python path
src_path = os.path.join(os.path.dirname(__file__), "..", "src")
sys.path.append(src_path)

from data_utils import fetch_cpi_data

def calculate_inflation(cpi_data):
    """
    Calculates the inflation rate for the last 4 quarters.
    
    Parameters:
        cpi_data (pd.DataFrame): A DataFrame with CPI data, ideally at monthly or higher frequency.
        
    Returns:
        pd.Series: A Series of inflation rates for the last 4 quarters.
    """
    # Ensure the index is datetime
    cpi_data.index = pd.to_datetime(cpi_data.index)
    
    # Resample to quarterly frequency
    quarterly_cpi = cpi_data["CPIAUCSL"].resample('Q').mean()
    
    # Calculate percentage change for quarterly data
    quarterly_cpi_pct_change = quarterly_cpi.pct_change(periods=1) * 100
    
    # Extract the last 4 quarters' inflation rates
    last_4_quarters = quarterly_cpi_pct_change.dropna().tail(4)
    return last_4_quarters

if __name__ == "__main__":
    print("Fetching CPI data...")
    cpi_data = fetch_cpi_data()
    print("Calculating last 4 quarters' inflation...")
    inflation_rates = calculate_inflation(cpi_data)
    print("\nLast 4 quarters' inflation rates (%):")
    print(inflation_rates)
