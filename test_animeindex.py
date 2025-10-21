# test_animeindex.py
"""
Tests for AnimeIndex module.
"""

import unittest
from animeindex import AnimeIndex

class TestAnimeIndex(unittest.TestCase):
    """Test cases for AnimeIndex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AnimeIndex()
        self.assertIsInstance(instance, AnimeIndex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AnimeIndex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
