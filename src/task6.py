import pandas as pd

def listings_per_neighbourhood(df_listings: pd.DataFrame) -> dict:
    """
    Return dict of neighbourhood -> count of listings.
    """
    # Count listings per neighborhood
    neighborhood_counts = df_listings['neighbourhood_cleansed'].value_counts()
    
    # Convert to dictionary
    return neighborhood_counts.to_dict()