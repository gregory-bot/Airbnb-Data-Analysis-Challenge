import pandas as pd
from datetime import datetime, timedelta

def listing_with_best_expected_revenue(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> int:
    """
    Return listing ID with best expected revenue.
    """
    # Create copies to avoid modifying originals
    listings = df_listings.copy()
    reviews = df_reviews.copy()
    
    # Clean price column
    listings['price'] = (
        listings['price']
        .astype(str)
        .str.replace(r'[\$,]', '', regex=True)
        .astype(float)
    )
    
    # Filter for short-stay listings only
    listings = listings[listings['minimum_nights'] <= 7]
    
    # If no listings meet criteria, return 0
    if listings.empty:
        return 0
    
    # Process reviews
    reviews['date'] = pd.to_datetime(reviews['date'], errors='coerce')
    cutoff_date = datetime.now() - timedelta(days=365)
    reviews_last_year = reviews[reviews['date'] >= cutoff_date]
    
    # If no recent reviews, return 0
    if reviews_last_year.empty:
        return 0
    
    # Count reviews per listing in last year
    review_counts = (
        reviews_last_year
        .groupby('listing_id')
        .size()
        .reset_index(name='review_count')
    )
    
    # Merge listings with review counts
    merged_df = pd.merge(
        listings,
        review_counts,
        left_on='id',
        right_on='listing_id',
        how='inner'
    )
    
    # If no matches after merge, return 0
    if merged_df.empty:
        return 0
    
    # Calculate expected revenue
    merged_df['guests'] = merged_df['review_count'] / 0.6
    merged_df['expected_revenue'] = (
        merged_df['guests'] * 
        merged_df['minimum_nights'] * 
        merged_df['price']
    )
    
    # Find listing with maximum expected revenue
    max_revenue = merged_df['expected_revenue'].max()
    best_listings = merged_df[merged_df['expected_revenue'] == max_revenue]
    
    return int(best_listings['id'].min())