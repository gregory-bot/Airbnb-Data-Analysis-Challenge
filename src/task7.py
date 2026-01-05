import pandas as pd

def host_with_most_listings(df_listings: pd.DataFrame) -> int:
    """
    Return host ID with most listings.
    """
    # Count listings per host
    host_counts = df_listings['host_id'].value_counts()
    
    # Get host ID with maximum count
    top_host_id = host_counts.idxmax()
    
    return int(top_host_id)