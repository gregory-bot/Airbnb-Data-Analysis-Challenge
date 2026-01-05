import pandas as pd

def average_listing_price(df_listings: pd.DataFrame) -> float:
    """
    Return the average price of all listings.
    """
    listings = df_listings.copy()
    
    # Clean price column: remove $ and commas, convert to float
    listings['price'] = (
        listings['price']
        .astype(str)
        .str.replace(r'[\$,]', '', regex=True)
        .astype(float)
    )
    
    # Calculate and return average
    return float(listings['price'].mean())