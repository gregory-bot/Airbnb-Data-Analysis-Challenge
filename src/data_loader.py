import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def load_sample_listings():
    """Generate sample listings data for testing."""
    np.random.seed(42)
    
    data = {
        'id': range(1, 101),
        'host_id': np.random.choice([101, 102, 103, 104, 105, 106, 107, 108], 100),
        'price': ['${:,.2f}'.format(np.random.uniform(50, 500)) for _ in range(100)],
        'minimum_nights': np.random.choice([1, 2, 3, 7, 14, 30], 100),
        'neighbourhood_cleansed': np.random.choice(
            ['Downtown', 'Suburbs', 'Beachfront', 'Historic District', 'Business District'], 
            100
        ),
        'calculated_host_listings_count': np.random.choice([1, 2, 3, 8, 12, 15], 100)
    }
    
    return pd.DataFrame(data)

def load_sample_reviews():
    """Generate sample reviews data for testing."""
    np.random.seed(42)
    
    # Generate dates over the past 2 years
    end_date = datetime.now()
    start_date = end_date - timedelta(days=730)
    
    dates = []
    for _ in range(500):
        random_days = np.random.randint(0, 730)
        dates.append(start_date + timedelta(days=random_days))
    
    data = {
        'listing_id': np.random.choice(range(1, 101), 500),
        'date': [d.strftime('%Y-%m-%d') for d in dates]
    }
    
    return pd.DataFrame(data)

def load_data():
    """Main data loading function."""
    listings = load_sample_listings()
    reviews = load_sample_reviews()
    return listings, reviews

if __name__ == "__main__":
    listings_df, reviews_df = load_data()
    print(f"Listings shape: {listings_df.shape}")
    print(f"Reviews shape: {reviews_df.shape}")