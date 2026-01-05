import unittest
import pandas as pd
import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import task functions
from data_loader import load_data
from task1 import average_listing_price
from task2 import count_short_stay_listings
from task3 import prof_nonprof_host_price_diff
from task4 import reviews_last_year
from task5 import listing_with_best_expected_revenue
from task6 import listings_per_neighbourhood
from task7 import host_with_most_listings

class TestAirbnbDataChallenge(unittest.TestCase):
    """Test suite for Airbnb Data Analytics Challenge"""
    
    @classmethod
    def setUpClass(cls):
        """Load test data once for all tests"""
        cls.listings, cls.reviews = load_data()
    
    def test_task1_average_price(self):
        """Test average listing price calculation"""
        result = average_listing_price(self.listings)
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)
    
    def test_task2_short_stay_count(self):
        """Test short-stay listings count"""
        result = count_short_stay_listings(self.listings)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, len(self.listings))
    
    def test_task3_price_difference(self):
        """Test professional vs non-professional host price difference"""
        result = prof_nonprof_host_price_diff(self.listings, self.reviews)
        self.assertIsInstance(result, float)
    
    def test_task4_recent_reviews(self):
        """Test recent reviews count"""
        result = reviews_last_year(self.reviews)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, len(self.reviews))
    
    def test_task5_best_revenue(self):
        """Test best revenue listing identification"""
        result = listing_with_best_expected_revenue(self.listings, self.reviews)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)
        if result > 0:
            self.assertIn(result, self.listings['id'].values)
    
    def test_task6_neighborhood_distribution(self):
        """Test neighborhood listing distribution"""
        result = listings_per_neighbourhood(self.listings)
        self.assertIsInstance(result, dict)
        self.assertGreater(len(result), 0)
        total_listings = sum(result.values())
        self.assertEqual(total_listings, len(self.listings))
    
    def test_task7_top_host(self):
        """Test top host identification"""
        result = host_with_most_listings(self.listings)
        self.assertIsInstance(result, int)
        self.assertIn(result, self.listings['host_id'].values)

if __name__ == '__main__':
    unittest.main(verbosity=2)