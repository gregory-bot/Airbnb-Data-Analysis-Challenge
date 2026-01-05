import pandas as pd

def count_short_stay_listings(df_listings: pd.DataFrame) -> int:
    """
    Count listings with minimum_nights <= 7.
    """
    # Create boolean mask for short stays
    short_stay_mask = df_listings['minimum_nights'] <= 7
    
    # Count True values
    return int(short_stay_mask.sum())