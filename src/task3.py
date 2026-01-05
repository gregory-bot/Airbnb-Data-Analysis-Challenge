import pandas as pd

def prof_nonprof_host_price_diff(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> float:
    """
    Return difference in average price between professional and non-professional hosts.
    
    Professional host: calculated_host_listings_count >= 5
    Difference: avg_price_professional - avg_price_nonprofessional
    """
    listings = df_listings.copy()
    
    # Clean price column
    listings['price'] = (
        listings['price']
        .astype(str)
        .str.replace(r'[\$,]', '', regex=True)
        .astype(float)
    )
    
    # Identify professional hosts
    listings['is_professional'] = listings['calculated_host_listings_count'] >= 5
    
    # Group by professional status and calculate averages
    avg_prices = listings.groupby('is_professional')['price'].mean()
    
    # Get averages with default values if group doesn't exist
    avg_professional = avg_prices.get(True, 0.0)
    avg_nonprofessional = avg_prices.get(False, 0.0)
    
    # Calculate difference
    difference = avg_professional - avg_nonprofessional
    
    return float(difference)