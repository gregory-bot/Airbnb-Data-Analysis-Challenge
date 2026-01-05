import pandas as pd
from datetime import datetime, timedelta

def reviews_last_year(df_reviews: pd.DataFrame) -> int:
    """
    Count reviews in the last 365 days.
    """
    reviews = df_reviews.copy()
    
    # Convert date column to datetime
    reviews['date'] = pd.to_datetime(reviews['date'], errors='coerce')
    
    # Calculate cutoff date (365 days ago)
    cutoff_date = datetime.now() - timedelta(days=365)
    
    # Filter reviews from last year
    recent_reviews = reviews[reviews['date'] >= cutoff_date]
    
    return int(len(recent_reviews))