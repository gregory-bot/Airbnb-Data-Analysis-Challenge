#!/usr/bin/env python3
"""
Airbnb Data Analytics Challenge - Main Execution Script
"""

from src.data_loader import load_data
from src.task1 import average_listing_price
from src.task2 import count_short_stay_listings
from src.task3 import prof_nonprof_host_price_diff
from src.task4 import reviews_last_year
from src.task5 import listing_with_best_expected_revenue
from src.task6 import listings_per_neighbourhood
from src.task7 import host_with_most_listings

def print_header(text):
    """Print formatted header"""
    print("\n" + "=" * 50)
    print(f" {text}")
    print("=" * 50)

def main():
    """Main execution function"""
    print("🏠 Airbnb Data Analytics Challenge")
    print("=" * 50)
    
    # Load data
    print("📊 Loading data...")
    listings_df, reviews_df = load_data()
    print(f"✓ Loaded {len(listings_df)} listings")
    print(f"✓ Loaded {len(reviews_df)} reviews")
    
    # Task 1: Average Price
    print_header("Task 1: Average Listing Price")
    avg_price = average_listing_price(listings_df)
    print(f"Average price: ${avg_price:.2f}")
    
    # Task 2: Short-Stay Listings
    print_header("Task 2: Short-Stay Listings")
    short_stay_count = count_short_stay_listings(listings_df)
    print(f"Listings with minimum_nights ≤ 7: {short_stay_count}")
    
    # Task 3: Professional Host Price Difference
    print_header("Task 3: Professional vs Non-Professional Hosts")
    price_diff = prof_nonprof_host_price_diff(listings_df, reviews_df)
    print(f"Price difference (professional - non-professional): ${price_diff:.2f}")
    
    # Task 4: Recent Reviews
    print_header("Task 4: Recent Reviews")
    recent_reviews = reviews_last_year(reviews_df)
    print(f"Reviews in last 365 days: {recent_reviews}")
    
    # Task 5: Best Revenue Opportunity
    print_header("Task 5: Best Revenue Opportunity")
    best_listing = listing_with_best_expected_revenue(listings_df, reviews_df)
    if best_listing > 0:
        print(f"Listing with highest expected revenue: ID {best_listing}")
    else:
        print("No listings meet the revenue calculation criteria")
    
    # Task 6: Neighborhood Distribution
    print_header("Task 6: Neighborhood Distribution")
    neighborhood_counts = listings_per_neighbourhood(listings_df)
    print(f"Found listings in {len(neighborhood_counts)} neighborhoods:")
    for neighborhood, count in sorted(neighborhood_counts.items(), key=lambda x: x[1], reverse=True)[:3]:
        print(f"  {neighborhood}: {count} listings")
    
    # Task 7: Top Host
    print_header("Task 7: Top Host")
    top_host = host_with_most_listings(listings_df)
    print(f"Host with most listings: ID {top_host}")
    
    print("\n" + "=" * 50)
    print("✅ All tasks completed successfully!")
    print("=" * 50)

if __name__ == "__main__":
    main()