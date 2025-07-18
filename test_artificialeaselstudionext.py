# test_artificialeaselstudionext.py
"""
Tests for ArtificialEaselStudioNext module.
"""

import unittest
from artificialeaselstudionext import ArtificialEaselStudioNext

class TestArtificialEaselStudioNext(unittest.TestCase):
    """Test cases for ArtificialEaselStudioNext class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArtificialEaselStudioNext()
        self.assertIsInstance(instance, ArtificialEaselStudioNext)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArtificialEaselStudioNext()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
