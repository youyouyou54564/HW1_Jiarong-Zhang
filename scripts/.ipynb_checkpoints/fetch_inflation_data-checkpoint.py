import os
import sys

# Add src to the Python path
src_path = os.path.join(os.path.dirname(__file__), "..", "src")
sys.path.append(src_path)

from data_utils import fetch_cpi_data

def calculate_inflation(cpi_data):
    """
    Calculates the inflation rate for the last 4 quarters.
    
    Parameters:
        cpi_data (pd.DataFrame): A DataFrame with CPI data.
        
    Returns:
        list: A list of inflation rates for the last 4 quarters.
    """
    cpi_data["pct_change"] = cpi_data["CPIAUCSL"].pct_change(periods=3) * 100
    last_4_quarters = cpi_data["pct_change"].dropna().tail(4)
    return last_4_quarters

if __name__ == "__main__":
    print("Fetching CPI data...")
    cpi_data = fetch_cpi_data()
    print("Calculating last 4 quarters' inflation...")
    inflation_rates = calculate_inflation(cpi_data)
    print("\nLast 4 quarters' inflation rates (%):")
    print(inflation_rates)